import re

import pandas as pd
import numpy as np

from seeq.sdk import *

from . import _common
from . import _config
from . import _login
from . import _push

from ._common import Status

from seeq import spy


def search(query, *, all_properties=False, workbook=_common.DEFAULT_WORKBOOK_PATH, recursive=True, quiet=False,
           status=None):
    """
    Issues a query to the Seeq Server to retrieve metadata for signals,
    conditions, scalars and assets. This metadata can be used to retrieve
    samples, capsules for a particular time range.

    Parameters
    ----------
    query : {dict, list, pd.DataFrame, pd.Series}
        A mapping of property / match-criteria pairs.

        If you supply a dict or list of dicts, then the matching
        operations are "contains" (instead of "equal to").

        If you supply a DataFrame or a Series, then the matching
        operations are "equal to" (instead of "contains").

        Match criteria uses the same syntax as the Data tab in Seeq. Available
        options are:

        =================== ===================================================
        Property            Description
        =================== ===================================================
        Name                Name of the item
        Path                Asset tree path of the item
        Type                The item type. One of 'Signal', 'Condition',
                              'Scalar', 'Asset', 'Histogram' or 'Metric'
        Description         The description of th item
        Datasource Name     The name of the datasource
        Datasource ID       The datasource ID
        Datasource Class    The datasource class
        Cache Enabled       If data caching is enabled
        Archived            If the item is archived
        Scoped To           The Seeq ID of the scoped workbook. Is overridden
                              by the 'workbook' argument
        =================== ===================================================


    all_properties : bool, default False
        True if all item properties should be retrieved. This currently makes
        the search operation much slower as retrieval of properties for an item
        requires a separate call.

    workbook : {str, None}
        A path string (with ' >> ' delimiters) or an ID to indicate a workbook
        to which the scope of the search should be limited. Note that globally
        scoped items will still be returned. The ID for a workbook is visible
        in the URL of Seeq Workbench, directly after the "workbook/" part.

    recursive : bool, default True
        If True, searches that include a Path entry will include items at and
        below the specified location in an asset tree. If False, the query
        dictionary can only contain a Path entry and only items at the
        specified level will be returned.

    quiet : bool, default False
        If True, suppresses progress output.

    status : spy.Status, optional
        If supplied, this Status object will be updated as the command
        progresses.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with rows for each item found and columns for each
        property.

    Examples
    --------
    Search for signals with the name 'Humid' on the asset tree under
    'Example >> Cooling Tower 1', retrieving all properties on the results:

    >>> spy.search({'Name': 'Humid', 'Path': 'Example >> Cooling Tower 1'}, all_properties=True)

    Using a pandas.DataFrame as the input:

    >>> my_items = pd.DataFrame(
    >>>     {'Name': ['Area A_Temperature', 'Area B_Compressor Power', 'Optimize' ],
    >>>      'Datasource Name': 'Example Data'})
    >>> spy.search(my_items)
    """
    _common.validate_argument_types([
        (query, 'query', (dict, list, pd.DataFrame, pd.Series)),
        (all_properties, 'all_properties', bool),
        (workbook, 'workbook', str),
        (recursive, 'recursive', bool),
        (quiet, 'quiet', bool),
        (status, 'status', _common.Status)
    ])

    status = Status.validate(status, quiet)
    try:
        return _search(query, all_properties=all_properties, workbook=workbook, recursive=recursive, quiet=quiet,
                       status=status)

    except KeyboardInterrupt:
        status.update('Search canceled', Status.CANCELED)


def _search(query, *, all_properties=False, workbook=_common.DEFAULT_WORKBOOK_PATH, recursive=True, quiet=False,
            status=None):
    status = Status.validate(status, quiet)

    items_api = ItemsApi(_login.client)
    trees_api = TreesApi(_login.client)
    signals_api = SignalsApi(_login.client)
    conditions_api = ConditionsApi(_login.client)
    scalars_api = ScalarsApi(_login.client)

    if isinstance(query, pd.DataFrame):
        queries = query.to_dict(orient='records')
        comparison = '=='
    elif isinstance(query, pd.Series):
        queries = [query.to_dict()]
        comparison = '=='
    elif isinstance(query, list):
        queries = query
        comparison = '~='
    else:
        queries = [query]
        comparison = '~='

    #
    # This function makes use of a lot of inner function definitions that utilize variables from the outer scope.
    # In order to keep things straight, all variables confined to the inner scope are prefixed with an underscore.
    #

    metadata = list()
    columns = list()
    warnings = set()

    status.metrics({
        'Results': {
            'Time': 0,
            'Count': 0
        }
    })
    status.update('Initializing', Status.RUNNING)

    timer = _common.timer_start()

    def _add_to_dict(_dict, _key, _val):
        _dict[_key] = _common.none_to_nan(_val)

        # We want the columns to appear in a certain order (the order we added them in) for readability
        if _key not in columns:
            columns.append(_key)

    def _get_warning_string():
        if len(warnings) == 0:
            return ''

        return '\nWarning(s):\n' + '\n'.join(warnings)

    def _add_all_properties(_id, _prop_dict):
        _item = items_api.get_item_and_all_properties(id=_id)  # type: ItemOutputV1
        for _prop in _item.properties:  # type: PropertyOutputV1
            _add_to_dict(_prop_dict, _prop.name, _prop.value)

        # Name and Type don't seem to appear in additional properties
        _add_to_dict(_prop_dict, 'Name', _item.name)
        _add_to_dict(_prop_dict, 'Type', _item.type)
        _add_to_dict(_prop_dict, 'Scoped To', _common.none_to_nan(_item.scoped_to))

        if _item.type == 'CalculatedSignal':
            _signal_output = signals_api.get_signal(id=_item.id)  # type: SignalOutputV1
            _add_to_dict(_prop_dict, 'Formula Parameters', [
                '%s=%s' % (_p.name, _p.item.id if _p.item else _p.formula) for _p in _signal_output.parameters
            ])

        if _item.type == 'CalculatedCondition':
            _condition_output = conditions_api.get_condition(id=_item.id)  # type: ConditionOutputV1
            _add_to_dict(_prop_dict, 'Formula Parameters', [
                '%s=%s' % (_p.name, _p.item.id if _p.item else _p.formula) for _p in _condition_output.parameters
            ])

        if _item.type == 'CalculatedScalar':
            _scalar_output = scalars_api.get_scalar(id=_item.id)  # type: CalculatedItemOutputV1
            _add_to_dict(_prop_dict, 'Formula Parameters', [
                '%s=%s' % (_p.name, _p.item.id if _p.item else _p.formula) for _p in _scalar_output.parameters
            ])

        return _prop_dict

    for current_query in queries:
        if _common.present(current_query, 'ID'):
            # If ID is specified, short-circuit everything and just get the item directly
            metadata.append(_add_all_properties(current_query['ID'], dict()))
            continue

        if not recursive:
            if len(current_query) != 1 or not _common.present(current_query, 'Path'):
                raise ValueError(
                    'When recursive=False, query dictionary must contain only a Path entry. Use Pandas operations '
                    'on the returned DataFrame to pare down results.')

        allowed_properties = ['Type', 'Name', 'Description', 'Path', 'Asset', 'Datasource Class', 'Datasource ID',
                              'Datasource Name', 'Cache Enabled', 'Archived', 'Scoped To']

        for key, value in current_query.items():
            if key not in allowed_properties:
                warnings.add('Property "%s" is not an indexed property and will be ignored. Use any of the '
                             'following searchable properties and then filter further using DataFrame '
                             'operations:\n"%s"' % (key, '", "'.join(allowed_properties)))

        item_types = list()
        clauses = list()

        if _common.present(current_query, 'Type'):
            item_type_specs = list()
            if isinstance(current_query['Type'], list):
                item_type_specs.extend(current_query['Type'])
            else:
                item_type_specs.append(current_query['Type'])

            for item_type_spec in item_type_specs:
                if item_type_spec == 'Signal':
                    item_types.extend(['StoredSignal', 'CalculatedSignal'])
                elif item_type_spec == 'Condition':
                    item_types.extend(['StoredCondition', 'CalculatedCondition'])
                elif item_type_spec == 'Scalar':
                    item_types.extend(['StoredScalar', 'CalculatedScalar'])
                elif item_type_spec == 'Metric':
                    item_types.extend(['ThresholdMetric'])
                else:
                    item_types.append(item_type_spec)

            del current_query['Type']

        if _common.present(current_query, 'Datasource Name'):
            _filters = ['Name == %s' % _common.get(current_query, 'Datasource Name')]
            if _common.present(current_query, 'Datasource ID'):
                _filters.append('Datasource ID == %s' % _common.get(current_query, 'Datasource ID'))
            if _common.present(current_query, 'Datasource Class'):
                _filters.append('Datasource Class == %s' % _common.get(current_query, 'Datasource Class'))

            datasource_results = items_api.search_items(filters=[' && '.join(_filters)],
                                                        types=['Datasource'],
                                                        limit=100000)  # type: ItemSearchPreviewPaginatedListV1

            if len(datasource_results.items) > 1:
                raise RuntimeError(
                    'Multiple datasources found that match "%s"' % _common.get(current_query, 'Datasource Name'))
            elif len(datasource_results.items) == 0:
                raise RuntimeError(
                    'No datasource found that matches "%s"' % _common.get(current_query, 'Datasource Name'))
            else:
                datasource = datasource_results.items[0]  # type: ItemSearchPreviewV1
                current_query['Datasource ID'] = items_api.get_property(id=datasource.id,
                                                                        property_name='Datasource ID').value
                current_query['Datasource Class'] = items_api.get_property(id=datasource.id,
                                                                           property_name='Datasource Class').value

            del current_query['Datasource Name']

        # Store these off for use during Path filtering
        datasource_dict = {key: value for key, value in current_query.items() if
                           key in ['Datasource Class', 'Datasource ID']}

        for prop_name in ['Name', 'Description', 'Datasource Class', 'Datasource ID', 'Data ID']:
            if prop_name in current_query and not pd.isna(current_query[prop_name]):
                clauses.append(prop_name + comparison + current_query[prop_name])
                del current_query[prop_name]

        filters = [' && '.join(clauses)] if len(clauses) > 0 else []

        kwargs = {
            'filters': filters,
            'types': item_types,
            'limit': _config.options.search_page_size
        }

        if workbook:
            if _common.is_guid(workbook):
                workbook_id = _common.sanitize_guid(workbook)
            else:
                workbook_id = _push.reify_workbook(workbook, create=False)

            if workbook_id:
                kwargs['scope'] = workbook_id
            elif workbook != _common.DEFAULT_WORKBOOK_PATH:
                raise RuntimeError('Workbook "%s" not found, or is not accessible by you' % workbook)

        if _common.present(current_query, 'Scoped To'):
            kwargs['scope'] = current_query['Scoped To']
            kwargs['filters'].append('@excludeGloballyScoped')

        if _common.present(current_query, 'Asset') and not _common.present(current_query, 'Path'):
            raise ValueError('"Path" query parameter must be present when "Asset" parameter present')

        path_to_query = None
        if _common.present(current_query, 'Path'):
            path_to_query = current_query['Path']
            if _common.present(current_query, 'Asset'):
                path_to_query = path_to_query + ' >> ' + current_query['Asset']

        def _do_search(_offset):
            kwargs['offset'] = _offset
            status.metrics({
                'Results': {
                    'Time': _common.timer_elapsed(timer),
                    'Count': len(metadata)
                }
            })
            status.update('Querying Seeq Server for items' + _get_warning_string(), Status.RUNNING)

            if recursive:
                return items_api.search_items(**kwargs)
            else:
                _kwargs2 = {
                    'id': kwargs['asset'],
                    'offset': kwargs['offset'],
                    'limit': kwargs['limit']
                }

                if 'scope' in kwargs:
                    _kwargs2['scoped_to'] = kwargs['scope']

                return trees_api.get_tree(**_kwargs2)

        def _gather_results_item_search(_result):
            _item_search_preview = _result  # type: ItemSearchPreviewV1
            _prop_dict = dict()

            _add_to_dict(_prop_dict, 'ID', _item_search_preview.id)
            if len(_item_search_preview.ancestors) > 1:
                _add_to_dict(_prop_dict, 'Path', ' >> '.join([_a.name for _a in _item_search_preview.ancestors[0:-1]]))
                _add_to_dict(_prop_dict, 'Asset', _item_search_preview.ancestors[-1].name)
            elif len(_item_search_preview.ancestors) == 1:
                _add_to_dict(_prop_dict, 'Path', np.nan)
                _add_to_dict(_prop_dict, 'Asset', _item_search_preview.ancestors[0].name)

            _add_to_dict(_prop_dict, 'Name', _item_search_preview.name)
            _add_to_dict(_prop_dict, 'Description', _item_search_preview.description)
            _add_to_dict(_prop_dict, 'Type', _item_search_preview.type)
            _uom = _item_search_preview.value_unit_of_measure if _item_search_preview.value_unit_of_measure \
                else _item_search_preview.source_value_unit_of_measure
            _add_to_dict(_prop_dict, 'Value Unit Of Measure', _uom)
            _datasource_item_preview = _item_search_preview.datasource  # type: ItemPreviewV1
            _add_to_dict(_prop_dict, 'Datasource Name',
                         _datasource_item_preview.name if _datasource_item_preview else None)
            if all_properties:
                _add_all_properties(_item_search_preview.id, _prop_dict)

            metadata.append(_prop_dict)

        def _gather_results_get_tree(_result):
            _tree_item_output = _result  # type: TreeItemOutputV1
            _prop_dict = dict()

            _add_to_dict(_prop_dict, 'ID', _tree_item_output.id)
            _path_parts = re.split(r'\s*>>\s*', path_to_query)
            if len(_path_parts) > 1:
                _add_to_dict(_prop_dict, 'Path', ' >> '.join(_path_parts[0:-1]))
                _add_to_dict(_prop_dict, 'Asset', _path_parts[-1])
            elif len(_path_parts) == 1:
                _add_to_dict(_prop_dict, 'Path', np.nan)
                _add_to_dict(_prop_dict, 'Asset', _path_parts[0])

            _add_to_dict(_prop_dict, 'Name', _tree_item_output.name)
            _add_to_dict(_prop_dict, 'Description', _tree_item_output.description)
            _add_to_dict(_prop_dict, 'Type', _tree_item_output.type)
            _add_to_dict(_prop_dict, 'Value Unit Of Measure', _tree_item_output.value_unit_of_measure)
            if all_properties:
                _add_all_properties(_tree_item_output.id, _prop_dict)

            metadata.append(_prop_dict)

        def _iterate_over_output(output_func, collection_name, action_func):
            _offset = 0
            while True:
                _output = output_func(_offset)

                _collection = getattr(_output, collection_name)

                for _item in _collection:
                    action_func(_item)

                if len(_collection) != _output.limit:
                    break

                _offset += _output.limit

        def _go():
            if recursive:
                _iterate_over_output(_do_search, 'items', _gather_results_item_search)
            else:
                _iterate_over_output(_do_search, 'children', _gather_results_get_tree)

        if not _common.present(current_query, 'Path'):
            _go()
        else:
            # We define a function here so we can use recursion through the path
            def _process_path_part(_path, _asset_id=None):
                _path_parts = re.split(r'\s*>>\s*', _path)

                _path_part = _path_parts[0]

                _tree_kwargs = dict()
                _tree_kwargs['limit'] = kwargs['limit']
                _tree_kwargs['offset'] = 0

                if 'scope' in kwargs:
                    _tree_kwargs['scoped_to'] = kwargs['scope']

                while True:
                    if not _asset_id:
                        _tree_output = trees_api.get_tree_root_nodes(**_tree_kwargs)  # type: AssetTreeOutputV1
                    else:
                        _tree_kwargs['id'] = _asset_id
                        _tree_output = trees_api.get_tree(**_tree_kwargs)  # type: AssetTreeOutputV1

                    for _child in _tree_output.children:  # type: TreeItemOutputV1
                        if not _asset_id:
                            # We only filter out datasource at the top level, in case the tree is mixed
                            _datasource_ok = True
                            _child_item_output = items_api.get_item_and_all_properties(
                                id=_child.id)  # type: ItemOutputV1
                            for _prop in ['Datasource Class', 'Datasource ID']:
                                if _prop in datasource_dict and datasource_dict[_prop]:
                                    _p_list = [_p.value for _p in _child_item_output.properties if
                                               _p.name == _prop]
                                    if len(_p_list) == 0 or _p_list[0] != datasource_dict[_prop]:
                                        _datasource_ok = False

                            if not _datasource_ok:
                                continue

                        if _common.does_query_fragment_match(_path_part, _child.name):
                            if len(_path_parts) == 1:
                                kwargs['asset'] = _child.id
                                _go()
                            else:
                                _process_path_part(' >> '.join(_path_parts[1:]), _child.id)

                    if len(_tree_output.children) < _tree_kwargs['limit']:
                        break

                    _tree_kwargs['offset'] += _tree_kwargs['limit']

            _process_path_part(path_to_query)

    status.metrics({
        'Results': {
            'Time': _common.timer_elapsed(timer),
            'Count': len(metadata)
        }
    })

    status.update('Query successful' + _get_warning_string(), Status.SUCCESS)

    search_df = pd.DataFrame(data=metadata, columns=columns)

    return search_df.drop_duplicates(subset='ID')
