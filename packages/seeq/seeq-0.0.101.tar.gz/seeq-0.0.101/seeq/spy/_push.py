import datetime
import json
import re
import six
import time

import pandas as pd
import numpy as np

from seeq.sdk import *
from seeq.sdk.rest import ApiException

from . import _common
from . import _config
from . import _login

from ._common import DependencyNotFound
from ._common import Status


def push(data=None, *, metadata=None, workbook=_common.DEFAULT_WORKBOOK_PATH,
         worksheet='From Data Lab', datasource=None, archive=False, type_mismatches='raise', errors='raise',
         quiet=False, status=None):
    """
    Imports metadata and/or data into Seeq Server, possibly scoped to a 
    workbook and/or datasource.

    The 'data' and 'metadata' arguments work together. Signal and condition 
    data cannot be mixed together in a single call to spy.push().

    Successive calls to 'push()' with the same 'metadata' but different 'data' 
    will update the items (rather than overwrite them); however, pushing a new 
    sample with the same timestamp as a previous one will overwrite the old 
    one.

    Metadata can be pushed without accompanying data. This is common after 
    having invoked the spy.assets.build() function. In such a case, the 
    'metadata' DataFrame can contain signals, conditions, scalars or assets.

    Parameters
    ----------
    data : pandas.DataFrame, optional
        A DataFrame that contains the signal or condition data to be pushed. 
        If 'metadata' is also supplied, it will have specific formatting 
        requirements depending on the type of data being pushed.

        For signals, 'data' must have a pandas.Timestamp-based index with a 
        column for each signal.

        For conditions, 'data' must have an integer index and two 
        pandas.Timestamp columns named 'Capsule Start' and 'Capsule End'.

    metadata : pandas.DataFrame, optional
        A DataFrame that contains the metadata for signals, conditions, 
        scalars, or assets. If 'metadata' is supplied, in conjunction with a 
        'data' DataFrame, it has specific requirements depending on the kind 
        of data supplied.

        For signals, the 'metadata' index (ie, rows) must have the same names 
        as the column names of the 'data' DataFrame.

        For conditions, the 'metadata' DataFrame must have only one row with 
        metadata for the condition.

        Metadata for each object type includes:

        Type Key: Si = Signal, Sc = Scalar, C = Condition, A = Asset

        ===================== ==================================== ============
        Metadata Term         Definition                           Types
        ===================== ==================================== ============
        Name                  Name of the signal                   Si, Sc, C, A
        Description           Description of the signal            Si, Sc, C, A
        Maximum Interpolation Maximum interpolation between        Si
                              samples
        Unit of Measure       Unit of measure of the values, or    Si, Sc, C
                              keys for conditions
        Formula               Formula for a calculated item        Si, Sc, C
        Formula Parameters    Parameters for a formula             Si, Sc, C
        Interpolation Method  Interpolation method between points  Si
                              Options are Linear, Step, PILinear
        Maximum Duration      Maximum expected duration for a      C
                              capsule
        Number Format         Formatting string ECMA-376           Si, Sc
        Path                  Asset tree path where the item's     Si, Sc, C, A
                              parent asset resides
        Asset                 Parent asset name. Parent asset      Si, Sc, C, A
                              must be in the tree at the
                              specified path, or listed in
                              'metadata' for creation.
        ===================== ==================================== ============

    workbook : {str, None}, default 'Data Lab >> Data Lab Analysis'
        The path to a workbook (in the form of 'Folder >> Path >> Workbook
        Name') or an ID that all pushed items will be 'scoped to'. Items scoped
        to a certain workbook will not be visible/searchable using the data
        panel in other workbooks. If None, items can also be 'globally scoped',
        meaning that they will be visible/searchable in all workbooks. Global
        scoping should be used judiciously to prevent search results becoming
        cluttered in all workbooks. The ID for a workbook is visible in the URL
        of Seeq Workbench, directly after the "workbook/" part.

    worksheet : str, default 'From Data Lab'
        The name of a worksheet within the workbook to create/update that will
        render the data that has been pushed so that you can see it in Seeq
        easily.

    datasource : dict, optional
        A dictionary defining the datasource within which to contain all the
        pushed items. By default, all pushed items will be contained in a "Seeq
        Data Lab" datasource. Do not create new datasources unless you really
        want to and you have permission from your administrator. The dictionary
        must have 'Datasource Class' and 'Datasource Name' keys.

    archive : bool, default False
        If 'True', archives any items in the datasource that previously existed
        but were not part of this push call. This can only be used if you also
        specify a 'datasource' argument.

    type_mismatches : {'raise', 'drop', 'invalid'}, default 'raise'
        If 'raise' (default), any mismatches between the type of the data and
        its metadata will cause an exception. For example, if string data is
        found in a numeric time series, an error will be raised. If 'drop' is
        specified, such data will be ignored while pushing. If 'invalid' is
        specified, such data will be replaced with an INVALID sample, which
        will interrupt interpolation in calculations and displays.


    errors : {'raise', 'catalog'}, default 'raise'
        If 'raise', any errors encountered will cause an exception. If
        'catalog', errors will be added to a 'Push Result' column in the
        passed-in 'items' DataFrame.

    quiet : bool, default False
        If True, suppresses progress output.

    status : spy.Status, optional
        If supplied, this Status object will be updated as the command
        progresses.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with the metadata for the items pushed, along with any
        errors and statistics about the operation.

    """
    _common.validate_argument_types([
        (data, 'data', pd.DataFrame),
        (metadata, 'metadata', pd.DataFrame),
        (workbook, 'workbook', str),
        (worksheet, 'worksheet', str),
        (datasource, 'datasource', dict),
        (archive, 'archive', bool),
        (type_mismatches, 'type_mismatches', str),
        (errors, 'errors', str),
        (quiet, 'quiet', bool),
        (status, 'status', _common.Status)
    ])

    status = Status.validate(status, quiet)
    _common.validate_errors_arg(errors)

    workbooks_api = WorkbooksApi(_login.client)
    signals_api = SignalsApi(_login.client)
    conditions_api = ConditionsApi(_login.client)
    datasources_api = DatasourcesApi(_login.client)

    if type_mismatches not in ['drop', 'raise', 'invalid']:
        raise RuntimeError("'type_mismatches' must be either 'drop', 'raise' or 'invalid'")

    if data is not None:
        if not isinstance(data, pd.DataFrame):
            raise RuntimeError("'data' must be a DataFrame")

    if metadata is not None:
        if not isinstance(metadata, pd.DataFrame):
            raise RuntimeError('"metadata" must be a DataFrame')

    if archive and datasource is None:
        raise RuntimeError('"datasource" must be supplied when "archive" is true')

    item_type = 'Signal'
    if data is not None:
        if 'Capsule Start' in data.columns or 'Capsule End' in data.columns:
            item_type = 'Condition'

    if datasource is not None:
        if not isinstance(datasource, dict):
            raise RuntimeError('"datasource" parameter must be dict')

        if 'Datasource Class' not in datasource:
            raise RuntimeError('"Datasource Class" required for datasource. This is the type of data being pushed. '
                               'For example, "WITSML"')

        if 'Datasource Name' not in datasource:
            raise RuntimeError('"Datasource Name" required for datasource. This is the specific data set being pushed. '
                               'For example, "Permian Basin Well Data"')

        datasource_input = DatasourceInputV1()
        _dict_to_datasource_input(datasource, datasource_input)

        if datasource_input.datasource_id is None:
            datasource_input.datasource_id = datasource_input.name
    else:
        datasource_input = _common.get_data_lab_datasource_input()

    datasource_output = datasources_api.create_datasource(body=datasource_input)  # type: DatasourceOutputV1

    workbook_id = None
    workstep_json = None
    if workbook is not None:
        if worksheet is None or not isinstance(worksheet, str):
            raise RuntimeError('When workbook is supplied, worksheet must also be supplied as a string')

        if _common.is_guid(workbook):
            workbook_id = _common.sanitize_guid(workbook)
        else:
            workbook_id = reify_workbook(workbook)

        worksheets_output = workbooks_api.get_worksheets(workbook_id=workbook_id,
                                                         limit=10000)  # type: WorksheetOutputListV1

        existing_worksheet = None
        for worksheet_output in worksheets_output.worksheets:  # type: WorksheetOutputV1
            if worksheet_output.name == worksheet:
                existing_worksheet = worksheet_output
                break

        if not existing_worksheet:
            worksheet_input = WorksheetInputV1()
            worksheet_input.name = worksheet
            existing_worksheet = workbooks_api.create_worksheet(workbook_id=workbook_id,
                                                                body=worksheet_input)  # type: WorksheetOutputV1

        worksheet_id = existing_worksheet.id

        workstep_input = WorkstepInputV1()
        if existing_worksheet.workstep:
            workstep_id = existing_worksheet.workstep.split('/')[-1]
            workstep_output = workbooks_api.get_workstep(workbook_id=workbook_id,
                                                         worksheet_id=worksheet_id,
                                                         workstep_id=workstep_id)  # type: WorkstepOutputV1
            workstep_input.data = workstep_output.data

        if workstep_input.data:
            workstep_json = json.loads(workstep_input.data)

        _now = int(round(time.time() * 1000))
        if not workstep_json:
            workstep_json = {
                "version": 24,
                "state": {
                    "stores": {
                        "sqTrendSeriesStore": {
                            "items": [
                            ]
                        },
                        "sqDurationStore": {
                            "autoUpdate": {
                                "mode": "OFF",
                                "offset": 0,
                                "manualInterval": {
                                    "value": 1,
                                    "units": "min"
                                }
                            },
                            "displayRange": {
                                "start": _now - (24 * 60 * 60 * 1000),
                                "end": _now
                            },
                            "investigateRange": {
                                "start": _now - (24 * 60 * 60 * 1000),
                                "end": _now
                            }
                        }
                    }
                }
            }

    push_result_df = pd.DataFrame()
    if metadata is not None:
        push_result_df = _push_metadata(metadata, workbook_id, datasource_output, archive, errors, status)

    if data is not None:
        earliest_sample = None
        latest_sample = None

        def _put_item_defaults(d):
            if 'Datasource Class' not in d:
                d['Datasource Class'] = datasource_output.datasource_class

            if 'Datasource ID' not in d:
                d['Datasource ID'] = datasource_output.datasource_id

            if 'Type' not in d:
                d['Type'] = item_type

            d['Data ID'] = _get_scoped_data_id(d, workbook_id)

        status_columns = list()
        if 'ID' in push_result_df:
            status_columns.append('ID')
        if 'Path' in push_result_df:
            status_columns.append('Path')
        if 'Asset' in push_result_df:
            status_columns.append('Asset')
        if 'Name' in push_result_df:
            status_columns.append('Name')

        status.df = push_result_df[status_columns].copy()
        status.df['Count'] = 0
        status.df['Time'] = 0
        status.df['Result'] = 'Pushing'
        status_columns.extend(['Count', 'Time', 'Result'])

        push_result_df['Push Count'] = np.int64(0)
        push_result_df['Push Time'] = 0
        push_result_df['Push Result'] = ''

        def _update_push_data_status():
            status.update(
                'Pushing data to datasource <strong>%s [%s]</strong> scoped to workbook ID <strong>%s</strong>' % (
                    datasource_output.name, datasource_output.datasource_id, workbook_id),
                Status.RUNNING)

        _update_push_data_status()

        if item_type == 'Signal':
            for column in data:
                try:
                    index = column
                    if index in push_result_df.index:
                        signal_metadata = push_result_df.loc[index].to_dict()
                    else:
                        ad_hoc_status_df = pd.DataFrame({'Count': 0, 'Time': 0, 'Result': 'Pushing'}, index=[index])
                        status.df = status.df.append(ad_hoc_status_df, sort=True)
                        signal_metadata = dict()

                    if 'Name' not in signal_metadata:
                        if '>>' in column:
                            raise RuntimeError('Paths in column name not currently supported. Supply a metadata '
                                               'argument if you would like to put signal(s) directly in an asset tree.')

                        signal_metadata['Name'] = column

                    _put_item_defaults(signal_metadata)

                    earliest_sample, latest_sample, signal_id = _push_signal(column, signal_metadata, data,
                                                                             earliest_sample, latest_sample,
                                                                             signals_api, workstep_json,
                                                                             type_mismatches, index, status,
                                                                             _update_push_data_status)

                    if signal_id is None:
                        # This can happen if the column has only nan values. In that case, we don't know whether it's
                        # a string or numeric signal and we couldn't create the signal item.
                        # Check to see if it was created by push_metadata.
                        if 'ID' in signal_metadata:
                            signal_id = signal_metadata['ID']

                    push_result_df.at[column, 'Push Result'] = 'Success' if signal_id is not None else 'No Data'
                    push_result_df.at[column, 'Push Count'] = status.df.at[index, 'Count']
                    push_result_df.at[column, 'Push Time'] = status.df.at[index, 'Time']
                    push_result_df.at[column, 'ID'] = signal_id
                    push_result_df.at[column, 'Type'] = 'StoredSignal'
                    push_result_df.at[column, 'Name'] = signal_metadata['Name']

                except Exception as e:
                    if errors == 'raise':
                        raise

                    push_result_df.at[column, 'Push Result'] = e

        elif item_type == 'Condition':
            try:
                if metadata is None or len(metadata) != 1:
                    raise RuntimeError('Condition requires "metadata" input of DataFrame with single row')

                condition_metadata = metadata.iloc[0].to_dict()

                if 'Name' not in condition_metadata or 'Maximum Duration' not in condition_metadata:
                    raise RuntimeError('Condition metadata requires "Name" and "Maximum Duration" columns')

                if 'Capsule Start' not in data or 'Capsule End' not in data:
                    raise RuntimeError('Condition data requires "Capsule Start" and "Capsule End" columns')

                _put_item_defaults(condition_metadata)
                earliest_sample, latest_sample, condition_id = _push_condition(condition_metadata, conditions_api, data,
                                                                               earliest_sample, latest_sample,
                                                                               metadata.index[0], status,
                                                                               _update_push_data_status)
                push_result_df.at[0, 'Push Result'] = 'Success'
                push_result_df.at[0, 'Push Count'] = status.df.at[0, 'Count']
                push_result_df.at[0, 'Push Time'] = status.df.at[0, 'Time']
                push_result_df.at[0, 'ID'] = condition_id
                push_result_df.at[0, 'Type'] = 'StoredCondition'

            except Exception as e:
                if errors == 'raise':
                    raise

                push_result_df.at[0, 'Push Result'] = str(e)

        if workbook_id and earliest_sample is not None and latest_sample is not None:
            workstep_json['state']['stores']['sqDurationStore']['displayRange']['start'] = earliest_sample
            workstep_json['state']['stores']['sqDurationStore']['displayRange']['end'] = latest_sample
            workstep_json['state']['stores']['sqDurationStore']['investigateRange']['start'] = earliest_sample
            workstep_json['state']['stores']['sqDurationStore']['investigateRange']['end'] = latest_sample

        url_string = ''
        if workbook_id:
            workstep_input.data = json.dumps(workstep_json)

            workstep_output = workbooks_api.create_workstep(workbook_id=workbook_id,
                                                            worksheet_id=worksheet_id,
                                                            body=workstep_input)  # type: WorkstepOutputV1

            workbooks_api.set_current_workstep(workbook_id=workbook_id,
                                               worksheet_id=worksheet_id,
                                               workstep_id=workstep_output.id)

            url = '%s/%s/workbook/%s/worksheet/%s' % (_config.get_api_url().replace('/api', ''),
                                                      workstep_output.id,
                                                      workbook_id,
                                                      worksheet_id)

            url_string = '<br>Click the following link to see your pushed data in Seeq:<br><a href="%s" ' \
                         'target="_new">%s</a>' \
                         % (url, url)

        status.update(
            'Pushed data successfully to datasource <strong>%s [%s]</strong> scoped to workbook ID '
            '<strong>%s</strong>%s' % (
                datasource_output.name, datasource_output.datasource_id, workbook_id, url_string),
            Status.SUCCESS)

    return push_result_df


def _push_metadata(metadata, workbook_id, datasource_output, archive, errors, status):
    items_api = ItemsApi(_login.client)
    trees_api = TreesApi(_login.client)
    datasources_api = DatasourcesApi(_login.client)

    metadata_df = metadata  # type: pd.DataFrame

    if 'Type' not in metadata_df:
        raise RuntimeError('Type column required when pushing metadata')

    sync_token = datetime.datetime.utcnow().isoformat()

    status_columns = [
        'Signal',
        'Scalar',
        'Condition',
        'Threshold Metric',
        'Asset',
        'Relationship',
        'Overall'
    ]

    status_dict = dict()
    for status_column in status_columns:
        status_dict[status_column] = 0

    status.df = pd.DataFrame([status_dict], index=['Items pushed'])

    status.update('Pushing metadata to datasource <strong>%s [%s]</strong> scoped to workbook ID '
                  '<strong>%s</strong>' % (
                      datasource_output.name, datasource_output.datasource_id, workbook_id),
                  Status.RUNNING)

    total = len(metadata_df)

    def _print_push_progress():
        status.update('Pushing metadata to datasource <strong>%s [%s]</strong> scoped to workbook ID '
                      '<strong>%s</strong>' % (
                          datasource_output.name, datasource_output.datasource_id, workbook_id),
                      Status.RUNNING)

    flush_now = False
    cache = dict()
    roots = dict()
    batch_size = 1000
    put_signals_input = PutSignalsInputV1()
    put_signals_input.signals = list()
    put_scalars_input = PutScalarsInputV1()
    put_scalars_input.scalars = list()
    condition_batch_input = ConditionBatchInputV1()
    condition_batch_input.conditions = list()
    threshold_metric_inputs = list()
    asset_batch_input = AssetBatchInputV1()
    asset_batch_input.assets = list()
    tree_batch_input = AssetTreeBatchInputV1()
    tree_batch_input.relationships = list()
    tree_batch_input.parent_host_id = datasource_output.id
    tree_batch_input.child_host_id = datasource_output.id
    last_scalar_datasource = None

    if not metadata_df.index.is_unique:
        raise RuntimeError("The metadata DataFrame's index must be unique. Use metadata.reset_index(drop=True, "
                           "inplace=True) before passing in to spy.push().")

    push_results_df = metadata_df.copy()
    if 'Push Result' in push_results_df:
        push_results_df = push_results_df.drop(columns=['Push Result'])

    while True:
        dependencies_not_found = list()
        at_least_one_item_created = False

        for index, row in push_results_df.iterrows():
            if 'Push Result' in row and not pd.isna(row['Push Result']):
                continue

            status.df['Overall'] += 1

            try:
                flush_now, last_scalar_datasource = \
                    _process_push_row(asset_batch_input, cache, condition_batch_input, status, datasource_output,
                                      flush_now, index, last_scalar_datasource, push_results_df, put_scalars_input,
                                      put_signals_input, roots, row, sync_token, tree_batch_input,
                                      workbook_id, threshold_metric_inputs)

            except DependencyNotFound as e:
                dependencies_not_found.append((index, e.identifier))
                continue

            except Exception as e:
                if errors == 'raise':
                    raise

                total -= 1
                push_results_df.at[index, 'Push Result'] = str(e)
                continue

            at_least_one_item_created = True

            if int(status.df['Overall']) % batch_size == 0 or flush_now:
                _print_push_progress()

                _flush(put_signals_input, put_scalars_input, condition_batch_input, threshold_metric_inputs,
                       asset_batch_input, tree_batch_input, push_results_df, errors)

                flush_now = False

        _print_push_progress()

        _flush(put_signals_input, put_scalars_input, condition_batch_input, threshold_metric_inputs,
               asset_batch_input, tree_batch_input, push_results_df, errors)

        if len(dependencies_not_found) == 0:
            break

        if not at_least_one_item_created:
            for not_found_index, not_found_data_id in dependencies_not_found:
                push_results_df.at[not_found_index, 'Push Result'] = 'Could not find dependency %s' % not_found_data_id

    for asset_input in roots.values():
        results = items_api.search_items(filters=['Datasource Class==%s && Datasource ID==%s && Data ID==%s' % (
            datasource_output.datasource_class, datasource_output.datasource_id,
            asset_input.data_id)])  # type: ItemSearchPreviewPaginatedListV1
        if len(results.items) == 0:
            raise RuntimeError('Root item "%s" not found' % asset_input.name)
        item_id_list = ItemIdListInputV1()
        item_id_list.items = [results.items[0].id]
        trees_api.move_nodes_to_root_of_tree(body=item_id_list)

    if archive:
        status.update('Archiving obsolete items in datasource <strong>%s [%s]</strong>' % (
            datasource_output.name, datasource_output.datasource_id),
                      Status.RUNNING)

        datasource_clean_up_input = DatasourceCleanUpInputV1()
        datasource_clean_up_input.sync_token = sync_token
        datasources_api.clean_up(id=datasource_output.id, body=datasource_clean_up_input)

    status.update('Pushed metadata successfully to datasource <strong>%s [%s]</strong> scoped to workbook ID '
                  '<strong>%s</strong>' % (datasource_output.name,
                                           datasource_output.datasource_id,
                                           workbook_id),
                  Status.SUCCESS)

    return push_results_df


def _process_push_row(asset_batch_input, cache, condition_batch_input, status, datasource_output, flush_now, index,
                      last_scalar_datasource, push_results_df, put_scalars_input, put_signals_input, roots, row,
                      sync_token, tree_batch_input, workbook_id, threshold_metric_inputs):
    d = row.to_dict()

    if not _common.present(d, 'Name'):
        raise RuntimeError('Metadata must have a "Name" column.')

    if _common.get(d, 'Reference') is True:
        if not _common.present(d, 'ID'):
            raise RuntimeError('"ID" column required when "Reference" column is True')
        _build_reference(d)

    scoped_data_id = _get_scoped_data_id(d, workbook_id)
    if not _common.present(d, 'Datasource Class'):
        d['Datasource Class'] = datasource_output.datasource_class

    if not _common.present(d, 'Datasource ID'):
        d['Datasource ID'] = datasource_output.datasource_id

    if 'Signal' in d['Type']:
        signal_input = SignalInputV1() if _common.present(d, 'ID') else SignalWithIdInputV1()

        _dict_to_signal_input(d, signal_input)

        signal_input.formula_parameters = _process_formula_parameters(signal_input.formula_parameters,
                                                                      workbook_id,
                                                                      push_results_df)
        if len(signal_input.formula_parameters) > 0:
            push_results_df.at[index, 'Formula Parameters'] = signal_input.formula_parameters

        if signal_input.formula:
            # There are lots of calculated properties that must be None for Appserver to accept our input
            signal_input.maximum_interpolation = None
            signal_input.interpolation_method = None
            signal_input.key_unit_of_measure = None
            signal_input.value_unit_of_measure = None

        if _common.present(d, 'ID'):
            status.df['Signal'] += 1
            try:
                signals_api = SignalsApi(_login.client)
                signal_output = signals_api.put_signal(id=d['ID'], body=signal_input)  # type: SignalOutputV1
                push_results_df.at[index, 'Push Result'] = 'Success'
                push_results_df.at[index, 'ID'] = signal_output.id
                push_results_df.at[index, 'Type'] = signal_output.type
            except ApiException as e:
                push_results_df.at[index, 'Push Result'] = e
        else:
            signal_input.datasource_class = d['Datasource Class']
            signal_input.datasource_id = d['Datasource ID']
            signal_input.data_id = scoped_data_id
            signal_input.sync_token = sync_token
            setattr(signal_input, 'dataframe_index', index)
            status.df['Signal'] += _add_no_dupe(put_signals_input.signals, signal_input)

    elif 'Scalar' in d['Type']:
        scalar_input = ScalarInputV1()

        _dict_to_scalar_input(d, scalar_input)

        scalar_input.parameters = _process_formula_parameters(scalar_input.parameters, workbook_id, push_results_df)
        if len(scalar_input.parameters) > 0:
            push_results_df.at[index, 'Formula Parameters'] = scalar_input.parameters

        if _common.present(d, 'ID'):
            items_api = ItemsApi(_login.client)
            ignored_properties = ['ID', 'Type', 'Formula', 'Formula Parameters', 'Key Unit Of Measure']
            props = [
                ScalarPropertyV1(name=_name, value=_value) for _name, _value in d.items()
                if _name not in ignored_properties and (isinstance(_value, list) or not pd.isna(_value))
            ]
            items_api.set_properties(id=d['ID'], body=props)
            if _common.present(d, 'Formula'):
                items_api.set_formula(id=d['ID'], body=FormulaInputV1(
                    formula=d['Formula'], parameters=d['Formula Parameters']))
        else:
            put_scalars_input.datasource_class = d['Datasource Class']
            put_scalars_input.datasource_id = d['Datasource ID']
            scalar_input.data_id = scoped_data_id
            scalar_input.sync_token = sync_token
            setattr(scalar_input, 'dataframe_index', index)
            status.df['Scalar'] += _add_no_dupe(put_scalars_input.scalars, scalar_input)

            # Since with scalars we have to put the Datasource Class and Datasource ID on the batch, we have to
            # recognize if it changed and, if so, flush the current batch.
            if last_scalar_datasource is not None and \
                    last_scalar_datasource != (d['Datasource Class'], d['Datasource ID']):
                flush_now = True

            last_scalar_datasource = (d['Datasource Class'], d['Datasource ID'])

    elif 'Condition' in d['Type']:
        condition_input = ConditionInputV1()
        _dict_to_condition_input(d, condition_input)

        condition_input.parameters = _process_formula_parameters(condition_input.parameters, workbook_id,
                                                                 push_results_df)
        if len(condition_input.parameters) > 0:
            push_results_df.at[index, 'Formula Parameters'] = condition_input.parameters

        if condition_input.formula is None and condition_input.maximum_duration is None:
            raise RuntimeError('"Maximum Duration" column required for stored conditions')

        if _common.present(d, 'ID'):
            items_api = ItemsApi(_login.client)
            ignored_properties = ['ID', 'Type', 'Formula', 'Formula Parameters', 'Key Unit Of Measure']
            props = [
                ScalarPropertyV1(name=_name, value=_value) for _name, _value in d.items()
                if _name not in ignored_properties and (isinstance(_value, list) or not pd.isna(_value))
            ]
            items_api.set_properties(id=d['ID'], body=props)
            if _common.present(d, 'Formula'):
                items_api.set_formula(id=d['ID'], body=FormulaInputV1(
                    formula=d['Formula'], parameters=d['Formula Parameters']))
        else:
            condition_input.datasource_class = d['Datasource Class']
            condition_input.datasource_id = d['Datasource ID']
            condition_input.data_id = scoped_data_id
            condition_input.sync_token = sync_token
            setattr(condition_input, 'dataframe_index', index)
            status.df['Condition'] += _add_no_dupe(condition_batch_input.conditions, condition_input)

    elif d['Type'] == 'Asset':
        asset_input = AssetInputV1()
        _dict_to_asset_input(d, asset_input)
        asset_input.data_id = scoped_data_id
        asset_input.sync_token = sync_token
        setattr(asset_input, 'dataframe_index', index)
        status.df['Asset'] += _add_no_dupe(asset_batch_input.assets, asset_input, overwrite=True)
        asset_batch_input.host_id = datasource_output.id

    elif 'Metric' in d['Type']:
        threshold_metric_input = ThresholdMetricInputV1()
        _dict_to_threshold_metric_input(d, threshold_metric_input)
        _set_threshold_levels_from_system(threshold_metric_input)
        threshold_metric_input.measured_item = _item_id_from_dict_value(
            threshold_metric_input.measured_item, workbook_id, push_results_df)
        if threshold_metric_input.bounding_condition:
            threshold_metric_input.bounding_condition = _item_id_from_dict_value(
                threshold_metric_input.bounding_condition, workbook_id, push_results_df)
        threshold_metric_input.thresholds = _convert_thresholds_dict_to_input(threshold_metric_input.thresholds,
                                                                              workbook_id, push_results_df)

        if _common.present(d, 'Statistic'):
            threshold_metric_input.aggregation_function = \
                '%s()' % _common.statistic_to_aggregation_function(d['Statistic'])
        threshold_metric_input.datasource_class = d['Datasource Class']
        threshold_metric_input.datasource_id = d['Datasource ID']
        threshold_metric_input.data_id = scoped_data_id
        setattr(threshold_metric_input, 'dataframe_index', index)
        status.df['Threshold Metric'] += 1
        threshold_metric_inputs.append(threshold_metric_input)
        push_results_df.at[index, 'Push Result'] = 'Success'

    path = _determine_path(d)
    if path:
        _reify_path(path, workbook_id, datasource_output, scoped_data_id, cache, roots,
                    asset_batch_input, tree_batch_input, sync_token, status)
    return flush_now, last_scalar_datasource


def _determine_path(d):
    path = list()
    if _common.present(d, 'Path'):
        path.append(_common.get(d, 'Path'))

    _type = _common.get(d, 'Type')

    if _type != 'Asset' and _common.present(d, 'Asset'):
        path.append(_common.get(d, 'Asset'))

    return ' >> '.join(path)


def _get_scoped_data_id(d, workbook_id):
    path = _determine_path(d)

    if not _common.present(d, 'Data ID'):
        if path:
            scoped_data_id = '%s >> %s' % (path, d['Name'])
        else:
            scoped_data_id = d['Name']
    else:
        scoped_data_id = d['Data ID']

    if not _is_scoped_data_id(scoped_data_id):
        if not _common.present(d, 'Type'):
            raise RuntimeError('Type is required for all item definitions')

        if workbook_id:
            guid = workbook_id
            if 'Scoped To' not in d:
                d['Scoped To'] = workbook_id
        else:
            guid = '00000000-0000-0000-0000-000000000000'

        _type = d['Type'].replace('Stored', '').replace('Calculated', '')

        # Need to scope the Data ID to the workbook so it doesn't collide with other workbooks
        scoped_data_id = '[%s] {%s} %s' % (guid, _type, six.text_type(scoped_data_id))

    return scoped_data_id.strip()


def _is_scoped_data_id(data_id):
    return re.match(r'^\[%s\] {\w+}.*' % _common.GUID_REGEX, data_id) is not None


def _get_unscoped_data_id(scoped_data_id):
    return re.sub(r'^\[%s\] {\w+}\s*' % _common.GUID_REGEX, '', scoped_data_id)


def _dict_to_input(d, _input, properties_attr, attr_map):
    for k, v in d.items():
        if k in attr_map:
            if attr_map[k] is not None:
                v = _common.get(d, k)
                if isinstance(v, list) or not pd.isna(v):
                    setattr(_input, attr_map[k], v)
        elif properties_attr is not None:
            p = ScalarPropertyV1()
            p.name = _common.ensure_unicode(k)

            if p.name in ['Push Result', 'Push Count', 'Push Time',
                          'Pull Result', 'Pull Count', 'Pull Time',
                          'Build Path', 'Build Asset', 'Build Template',
                          'Build Result', 'ID']:
                continue

            uom = None
            if isinstance(v, dict):
                uom = _common.get(v, 'Unit Of Measure')
                v = _common.get(v, 'Value')
            else:
                v = _common.get(d, k)

            if not pd.isna(v):
                if isinstance(v, np.number):
                    v = v.item()

                p.value = _common.ensure_unicode(v)

                if uom is not None:
                    p.unit_of_measure = _common.ensure_unicode(uom)
                _properties = getattr(_input, properties_attr)
                if _properties is None:
                    _properties = list()
                _properties.append(p)
                setattr(_input, properties_attr, _properties)


def _set_threshold_levels_from_system(threshold_input):
    # type: (ThresholdMetricInputV1) -> None
    """
    Read the threshold limits from the systems endpoint and update the values in the threshold limits. Allows users
    to set thresholds as those defined in the system endpoint such as 'Lo', 'LoLo', 'Hi', 'HiHi', etc.

    :param threshold_input: A Threshold Metric input with a dict in the thresholds with keys of the priority level and
    values of the threshold. Keys are either a numeric value of the threshold, or strings contained in the
    systems/configuration. Values are either scalars or metadata dataframes. If a key is a string that maps to a number
    that is already used in the limits, a RuntimeError will be raised.
    :return: The threshold input with a limits dict with the string values replaced with numbers.
    """
    system_api = SystemApi(_login.client)

    # get the priority names and their corresponding levels
    system_settings = system_api.get_configuration()  # type: SystemConfigurationOutputV1
    priority_levels = {p.name: p.level for p in system_settings.priorities}

    # check provided limits are unique
    if isinstance(threshold_input.thresholds, dict):
        for k in threshold_input.thresholds.keys():
            if list(threshold_input.thresholds).count(k) > 1:
                raise RuntimeError('Threshold priorities are not unique {}'.format(threshold_input.thresholds.keys()))

        # translate the string thresholds to numeric values
        updated_threshold_limits = dict()
        for k, v in threshold_input.thresholds.items():
            if k in priority_levels:
                if str(priority_levels[k]) in threshold_input.thresholds:
                    raise RuntimeError('String threshold priorities cannot map to a current numeric threshold {}:{}'
                                       .format(k, priority_levels[k]))
                updated_threshold_limits[priority_levels[k]] = v
            else:
                try:
                    int(k)
                except ValueError:
                    raise RuntimeError('The threshold {} could not be converted to a number for metric {}'.format(
                        k, threshold_input.name))
                if int(k) != float(k):
                    raise RuntimeError(
                        'Priority levels must be integers. The value {} in threshold {} is invalid'.format(
                            k, threshold_input.name))
                updated_threshold_limits[int(k)] = v
        threshold_input.thresholds = updated_threshold_limits


def _dict_to_datasource_input(d, datasource_input):
    _dict_to_input(d, datasource_input, None, {
        'Name': 'name',
        'Description': 'description',
        'Datasource Name': 'name',
        'Datasource Class': 'datasource_class',
        'Datasource ID': 'datasource_id'
    })


def _dict_to_asset_input(d, asset_input):
    _dict_to_input(d, asset_input, 'properties', {
        'Type': None,
        'Name': 'name',
        'Description': 'description',
        'Datasource Class': 'datasource_class',
        'Datasource ID': 'datasource_id',
        'Data ID': 'data_id',
        'Scoped To': 'scoped_to'
    })


def _dict_to_signal_input(d, signal_input):
    _dict_to_input(d, signal_input, 'additional_properties', {
        'Type': None,
        'Name': 'name',
        'Description': 'description',
        'Datasource Class': 'datasource_class',
        'Datasource ID': 'datasource_id',
        'Data ID': 'data_id',
        'Data Version Check': 'data_version_check',
        'Formula': 'formula',
        'Formula Parameters': 'formula_parameters',
        'Interpolation Method': 'interpolation_method',
        'Maximum Interpolation': 'maximum_interpolation',
        'Scoped To': 'scoped_to',
        'Key Unit Of Measure': 'key_unit_of_measure',
        'Value Unit Of Measure': 'value_unit_of_measure',
        'Number Format': 'number_format'
    })


def _dict_to_scalar_input(d, scalar_input):
    _dict_to_input(d, scalar_input, 'properties', {
        'Type': None,
        'Name': 'name',
        'Description': 'description',
        'Datasource Class': 'datasource_class',
        'Datasource ID': 'datasource_id',
        'Data ID': 'data_id',
        'Data Version Check': 'data_version_check',
        'Formula': 'formula',
        'Formula Parameters': 'parameters',
        'Scoped To': 'scoped_to',
        'Number Format': 'number_format'
    })


def _dict_to_condition_input(d, signal_input):
    _dict_to_input(d, signal_input, 'properties', {
        'Type': None,
        'Name': 'name',
        'Description': 'description',
        'Datasource Class': 'datasource_class',
        'Datasource ID': 'datasource_id',
        'Data ID': 'data_id',
        'Data Version Check': 'data_version_check',
        'Formula': 'formula',
        'Formula Parameters': 'parameters',
        'Maximum Duration': 'maximum_duration',
        'Scoped To': 'scoped_to'
    })


def _dict_to_capsule(d, capsule):
    _dict_to_input(d, capsule, 'properties', {
        'Capsule Start': None,
        'Capsule End': None
    })


def _dict_to_threshold_metric_input(d, metric_input):
    _dict_to_input(d, metric_input, None, {
        'Type': None,
        'Name': 'name',
        'Duration': 'duration',
        'Bounding Condition Maximum Duration': 'bounding_condition_maximum_duration',
        'Period': 'period',
        'Thresholds': 'thresholds',
        'Measured Item': 'measured_item',
        'Number Format': 'number_format',
        'Bounding Condition': 'bounding_condition',
        'Measured Item Maximum Duration': 'measured_item_maximum_duration',
        'Scoped To': 'scoped_to',
        'Aggregation Function': 'aggregation_function'
    })


def reify_workbook(workbook_path, create=True):
    workbooks_api = WorkbooksApi(_login.client)
    folders_api = FoldersApi(_login.client)
    items_api = ItemsApi(_login.client)

    workbook_path = re.split(r'\s*>>\s*', workbook_path.strip())

    parent_id = None
    workbook_id = None
    for i in range(0, len(workbook_path)):
        existing_content_id = None
        content_name = workbook_path[i]
        content_type = 'Workbook' if i == len(workbook_path) - 1 else 'Folder'
        if parent_id:
            folders = folders_api.get_folders(filter='owner',
                                              folder_id=parent_id,
                                              limit=10000)  # type: FolderOutputListV1
        else:
            folders = folders_api.get_folders(filter='owner',
                                              limit=10000)  # type: FolderOutputListV1

        for content in folders.content:
            if content_type == content.type and content_name == content.name:
                existing_content_id = content.id
                break

        if not existing_content_id:
            if not create:
                return None

            if content_type == 'Folder':
                folder_input = FolderInputV1()
                folder_input.name = content_name
                folder_input.description = 'Created by Seeq Data Lab'
                folder_input.owner_id = _login.user.id
                folder_input.parent_folder_id = parent_id
                folder_output = folders_api.create_folder(body=folder_input)  # type: FolderOutputV1
                existing_content_id = folder_output.id
            else:
                workbook_input = WorkbookInputV1()
                workbook_input.name = content_name
                workbook_input.description = 'Created by Seeq Data Lab'
                workbook_input.owner_id = _login.user.id
                workbook_input.folder_id = parent_id
                workbook_output = workbooks_api.create_workbook(body=workbook_input)  # type: WorkbookOutputV1
                existing_content_id = workbook_output.id
                items_api.set_property(id=workbook_output.id,
                                       property_name='workbookState',
                                       body=PropertyInputV1(
                                           unit_of_measure='string', value=_common.DEFAULT_WORKBOOK_STATE
                                       )
                                       )

        parent_id = existing_content_id
        workbook_id = existing_content_id

    return workbook_id


def _push_condition(condition_metadata, conditions_api, data, earliest_sample, latest_sample, status_index, status,
                    update_status):
    condition_batch_input = ConditionBatchInputV1()
    condition_input = ConditionInputV1()
    _dict_to_condition_input(condition_metadata, condition_input)
    condition_batch_input.conditions = [condition_input]
    condition_input.datasource_class = condition_metadata['Datasource Class']
    condition_input.datasource_id = condition_metadata['Datasource ID']
    items_batch_output = conditions_api.put_conditions(body=condition_batch_input)  # type: ItemBatchOutputV1
    item_update_output = items_batch_output.item_updates[0]  # type: ItemUpdateOutputV1
    capsules_input = CapsulesInputV1()
    capsules_input.capsules = list()
    capsules_input.key_unit_of_measure = 'ns'
    count = 0
    timer = _common.timer_start()
    for index, row in data.iterrows():
        capsule = CapsuleV1()
        _dict_to_capsule(row.to_dict(), capsule)
        capsule.start = row['Capsule Start'].value
        capsule.end = row['Capsule End'].value
        capsules_input.capsules.append(capsule)
        # noinspection PyTypeChecker
        key_in_ms = capsule.start / 1000000
        earliest_sample = min(key_in_ms, earliest_sample) if earliest_sample is not None else key_in_ms
        # noinspection PyTypeChecker
        key_in_ms = capsule.end / 1000000
        latest_sample = max(key_in_ms, latest_sample) if latest_sample is not None else key_in_ms

        if len(capsules_input.capsules) > _config.options.push_page_size:
            conditions_api.add_capsules(id=item_update_output.item.id, body=capsules_input)
            count += len(capsules_input.capsules)
            status.df.at[status_index, 'Count'] = count
            status.df.at[status_index, 'Time'] = _common.timer_elapsed(timer)
            status.df.at[status_index, 'Result'] = 'Pushed to %s' % index
            update_status()
            capsules_input.capsules = list()

    if len(capsules_input.capsules) > 0:
        conditions_api.add_capsules(id=item_update_output.item.id, body=capsules_input)
        count += len(capsules_input.capsules)

    status.df.at[status_index, 'Count'] = count
    status.df.at[status_index, 'Time'] = _common.timer_elapsed(timer)
    status.df.at[status_index, 'Result'] = 'Success'
    update_status()

    return earliest_sample, latest_sample, item_update_output.item.id


def axis_number_from_string(axis):
    axis_number = 0
    exponent = 0
    while len(axis) > 0:
        alpha = axis[0]
        value = ord(alpha) - 65
        axis_number += value * 26 ** exponent
        exponent += 1
        axis = axis[0:-1]

    return axis_number


def string_from_axis_number(axis_number):
    axis = ''
    exponent = 0
    while axis_number > 0:
        axis = chr(int(axis_number % 26) + 65) + axis
        exponent += 1
        axis_number = axis_number / 26 ** exponent

    return axis


def _push_signal(column, signal_metadata, data, earliest_sample, latest_sample, signals_api, workstep_json,
                 type_mismatches, status_index, status, update_status):
    signal_input = SignalInputV1()
    _dict_to_signal_input(signal_metadata, signal_input)
    put_samples_input = PutSamplesInputV1()
    put_samples_input.samples = list()
    count = 0
    is_string = None
    signal_output = None
    timer = _common.timer_start()
    for index, row in data.iterrows():
        if pd.isna(row[column]):
            continue

        # noinspection PyUnresolvedReferences
        if not isinstance(index, pd.Timestamp):
            raise RuntimeError('data index must only be pd.Timestamp objects, but %s found instead' %
                               type(index))

        sample_value = row[column]

        if is_string is None:
            if 'Value Unit Of Measure' in signal_metadata:
                is_string = (signal_metadata['Value Unit Of Measure'] == 'string')
            else:
                is_string = isinstance(sample_value, six.string_types)

        if is_string != isinstance(sample_value, six.string_types):
            # noinspection PyBroadException
            try:
                if is_string:
                    sample_value = six.text_type(sample_value)
                else:
                    if data[column].dtype.name == 'int64':
                        sample_value = int(sample_value)
                    else:
                        sample_value = float(sample_value)
            except BaseException:
                # Couldn't convert it, fall through to the next conditional
                pass

        if is_string != isinstance(sample_value, six.string_types):
            if type_mismatches == 'drop':
                continue
            elif type_mismatches == 'raise':
                raise RuntimeError('Column "%s" was detected as %s, but %s value at (%s, %s) found. Supply '
                                   'type_mismatches parameter as "drop" to ignore the sample entirely or '
                                   '"invalid" to insert an INVALID sample in its place.' %
                                   (column, 'string-valued' if is_string else 'numeric-valued',
                                    'numeric' if is_string else 'string',
                                    index, sample_value))
            else:
                sample_value = None

        if isinstance(sample_value, np.number):
            sample_value = sample_value.item()

        if not signal_output:
            if is_string:
                signal_input.value_unit_of_measure = 'string'

            signal_output = signals_api.put_signal_by_data_id(datasource_class=signal_metadata['Datasource Class'],
                                                              datasource_id=signal_metadata['Datasource ID'],
                                                              data_id=signal_metadata['Data ID'],
                                                              body=signal_input)  # type: SignalOutputV1

        sample_input = SampleInputV1()
        key_in_ms = index.value / 1000000
        earliest_sample = min(key_in_ms, earliest_sample) if earliest_sample is not None else key_in_ms
        latest_sample = max(key_in_ms, latest_sample) if latest_sample is not None else key_in_ms

        sample_input.key = index.value
        sample_input.value = sample_value
        put_samples_input.samples.append(sample_input)

        if len(put_samples_input.samples) >= _config.options.push_page_size:
            signals_api.put_samples(id=signal_output.id,
                                    body=put_samples_input)
            count += len(put_samples_input.samples)
            status.df.at[status_index, 'Count'] = count
            status.df.at[status_index, 'Time'] = _common.timer_elapsed(timer)
            status.df.at[status_index, 'Result'] = 'Pushed to %s' % index
            update_status()

            put_samples_input.samples = list()

        if workstep_json and len(workstep_json['state']['stores']['sqTrendSeriesStore']['items']) < 15:
            highest_lane = 1
            highest_axis = 0
            found = False
            for item in workstep_json['state']['stores']['sqTrendSeriesStore']['items']:
                if item['id'] == signal_output.id:
                    found = True

                if 'lane' in item:
                    highest_lane = max(item['lane'], highest_lane)

                if 'axisAlign' in item:
                    highest_axis = max(axis_number_from_string(item['axisAlign']), highest_axis)

            if not found:
                workstep_json['state']['stores']['sqTrendSeriesStore']['items'].append({
                    "axisAlign": string_from_axis_number(highest_axis + 1),
                    "axisAutoScale": True,
                    "id": signal_output.id,
                    "lane": highest_lane + 1
                })

    if len(put_samples_input.samples) > 0:
        signals_api.put_samples(id=signal_output.id,
                                body=put_samples_input)
        count += len(put_samples_input.samples)

    status.df.at[status_index, 'Count'] = count
    status.df.at[status_index, 'Time'] = _common.timer_elapsed(timer)
    status.df.at[status_index, 'Result'] = 'Success'
    update_status()

    return earliest_sample, latest_sample, signal_output.id if signal_output is not None else None


def _build_reference_signal(definition):
    definition['Type'] = 'CalculatedSignal'
    definition['Formula'] = '$signal'

    if _common.present(definition, 'Interpolation Method'):
        definition['Formula'] += ".to%s()" % definition['Interpolation Method']

    definition['Formula Parameters'] = 'signal=%s' % definition['ID']
    definition['Cache Enabled'] = False

    for key in ['ID', 'Datasource Class', 'Datasource ID', 'Data ID', 'Value Unit Of Measure',
                'Interpolation Method']:
        if _common.present(definition, key) and not _common.present(definition, 'Referenced ' + key):
            definition['Referenced ' + key] = definition[key]
            del definition[key]


def _build_reference_condition(definition):
    definition['Type'] = 'CalculatedCondition'
    definition['Formula'] = '$condition'
    definition['Formula Parameters'] = 'condition=%s' % definition['ID']
    definition['Cache Enabled'] = False

    for key in ['ID', 'Datasource Class', 'Datasource ID', 'Data ID', 'Unit Of Measure', 'Maximum Duration']:
        if _common.present(definition, key) and not _common.present(definition, 'Referenced ' + key):
            definition['Referenced ' + key] = definition[key]
            del definition[key]


def _build_reference_scalar(definition):
    definition['Type'] = 'CalculatedScalar'
    definition['Formula'] = '$scalar'
    definition['Formula Parameters'] = 'scalar=%s' % definition['ID']
    definition['Cache Enabled'] = False

    for key in ['ID', 'Datasource Class', 'Datasource ID', 'Data ID', 'Unit Of Measure']:
        if _common.present(definition, key) and not _common.present(definition, 'Referenced ' + key):
            definition['Referenced ' + key] = definition[key]
            del definition[key]


def _build_reference(definition):
    {
        'StoredSignal': _build_reference_signal,
        'CalculatedSignal': _build_reference_signal,
        'StoredCondition': _build_reference_condition,
        'CalculatedCondition': _build_reference_condition,
        'CalculatedScalar': _build_reference_scalar
    }[definition['Type']](definition)


def _process_formula_parameters(parameters, workbook_id, push_results_df):
    if parameters is None:
        return list()

    if isinstance(parameters, dict):
        parameters_dict = parameters  # type: dict
        return _parameters_dict_to_list(parameters_dict, workbook_id, push_results_df)

    if not isinstance(parameters, list):
        return [parameters]
    else:
        return parameters


def _parameters_dict_to_list(parameters_dict, workbook_id, push_results_df):
    parameters_list = list()
    for k, v in parameters_dict.items():
        # Strip off leading dollar-sign if it's there
        parameter_name = re.sub(r'^\$', '', k)
        try:
            parameter_id = _item_id_from_dict_value(v, workbook_id, push_results_df)
        except RuntimeError as e:
            raise RuntimeError('Error processing {}: {}'.format(parameter_name, e))
        parameters_list.append('%s=%s' % (parameter_name, parameter_id))
    return parameters_list


def _item_id_from_dict_value(dict_value, workbook_id, push_results_df):
    if isinstance(dict_value, pd.DataFrame):
        if len(dict_value) == 0:
            raise RuntimeError('The parameter had an empty dataframe')
        if len(dict_value) > 1:
            raise RuntimeError('The parameter had multiple entries in the dataframe')
        return dict_value.iloc[0]['ID']
    elif isinstance(dict_value, (dict, pd.Series)):
        if _common.present(dict_value, 'ID') and not _common.get(dict_value, 'Reference', default=False):
            return dict_value['ID']
        else:
            try:
                scoped_data_id = _get_scoped_data_id(dict_value, workbook_id)
            except RuntimeError:
                # This can happen if the dependency didn't get pushed and therefore doesn't have a proper Type
                raise DependencyNotFound(dict_value)
            if 'Data ID' in push_results_df:
                pushed_row_i_need = push_results_df[push_results_df['Data ID'] == scoped_data_id]
                if not pushed_row_i_need.empty:
                    return pushed_row_i_need.iloc[0]['ID']
                else:
                    raise DependencyNotFound(scoped_data_id)
            else:
                raise DependencyNotFound(scoped_data_id)
    else:
        return dict_value


def _flush(put_signals_input, put_scalars_input, condition_batch_input, threshold_metric_inputs, asset_batch_input,
           tree_batch_input, push_results_df, errors):
    items_api = ItemsApi(_login.client)
    signals_api = SignalsApi(_login.client)
    scalars_api = ScalarsApi(_login.client)
    conditions_api = ConditionsApi(_login.client)
    assets_api = AssetsApi(_login.client)
    trees_api = TreesApi(_login.client)
    metrics_api = MetricsApi(_login.client)

    def _set_push_result_string(dfi, iuo):
        _result_string = 'Success'
        if isinstance(iuo, ItemUpdateOutputV1):
            if iuo.error_message is not None:
                if errors == 'raise':
                    raise RuntimeError('Error pushing "%s": %s' % (iuo.data_id, iuo.error_message))
                _result_string = iuo.error_message
            push_results_df.at[dfi, 'Datasource Class'] = iuo.datasource_class
            push_results_df.at[dfi, 'Datasource ID'] = iuo.datasource_id
            push_results_df.at[dfi, 'Data ID'] = iuo.data_id
            push_results_df.at[dfi, 'ID'] = iuo.item.id
            push_results_df.at[dfi, 'Type'] = iuo.item.type
        elif isinstance(iuo, ThresholdMetricOutputV1):
            _item_output = items_api.get_item_and_all_properties(id=iuo.id)  # type: ItemOutputV1
            _item_properties = {p.name: p.value for p in _item_output.properties}
            push_results_df.at[dfi, 'Datasource Class'] = _item_properties['Datasource Class']
            push_results_df.at[dfi, 'Datasource ID'] = _item_properties['Datasource ID']
            push_results_df.at[dfi, 'Data ID'] = _item_properties['Data ID']
            push_results_df.at[dfi, 'ID'] = iuo.id
            push_results_df.at[dfi, 'Type'] = iuo.type
        else:
            raise TypeError('Unrecognized output type from API: %s' % type(iuo))

        push_results_df.at[dfi, 'Push Result'] = _result_string

    if len(put_signals_input.signals) > 0:
        item_batch_output = signals_api.put_signals(body=put_signals_input)  # type: ItemBatchOutputV1
        for i in range(0, len(put_signals_input.signals)):
            signal_input = put_signals_input.signals[i]
            item_update_output = item_batch_output.item_updates[i]  # type: ItemUpdateOutputV1
            _set_push_result_string(signal_input.dataframe_index, item_update_output)

        put_signals_input.signals = list()

    if len(put_scalars_input.scalars) > 0:
        item_batch_output = scalars_api.put_scalars(body=put_scalars_input)  # type: ItemBatchOutputV1
        for i in range(0, len(put_scalars_input.scalars)):
            scalar_input = put_scalars_input.scalars[i]
            item_update_output = item_batch_output.item_updates[i]  # type: ItemUpdateOutputV1
            _set_push_result_string(scalar_input.dataframe_index, item_update_output)

        put_scalars_input.scalars = list()

    if len(condition_batch_input.conditions) > 0:
        item_batch_output = conditions_api.put_conditions(body=condition_batch_input)  # type: ItemBatchOutputV1
        for i in range(0, len(condition_batch_input.conditions)):
            condition_input = condition_batch_input.conditions[i]
            item_update_output = item_batch_output.item_updates[i]  # type: ItemUpdateOutputV1
            _set_push_result_string(condition_input.dataframe_index, item_update_output)

        condition_batch_input.conditions = list()

    if len(threshold_metric_inputs) > 0:
        for tm in threshold_metric_inputs:
            # check if th metric already exists
            metric_search = items_api.search_items(
                filters=['Datasource Class == {} && Datasource ID == {} && Data ID == {}'.format(tm.datasource_class,
                                                                                                 tm.datasource_id,
                                                                                                 tm.data_id),
                         '@includeUnsearchable'])
            if metric_search.total_results > 1:
                raise RuntimeError('More than one metric had the data triplet {}, {}, {}'.format(tm.datasource_class,
                                                                                                 tm.datasource_id,
                                                                                                 tm.data_id))
            elif metric_search.total_results == 1:
                tm_push_output = metrics_api.put_threshold_metric(id=metric_search.items[0].id,
                                                                  body=tm)
            else:
                tm_push_output = metrics_api.create_threshold_metric(body=tm)
                _add_data_properties(tm_push_output, tm.datasource_class, tm.datasource_id, tm.data_id)
            _set_push_result_string(tm.dataframe_index, tm_push_output)

        threshold_metric_inputs.clear()

    if len(asset_batch_input.assets) > 0:
        item_batch_output = assets_api.batch_create_assets(body=asset_batch_input)  # type: ItemBatchOutputV1
        for i in range(0, len(asset_batch_input.assets)):
            asset_input = asset_batch_input.assets[i]
            if not hasattr(asset_input, 'dataframe_index'):
                continue
            item_update_output = item_batch_output.item_updates[i]  # type: ItemUpdateOutputV1
            _set_push_result_string(asset_input.dataframe_index, item_update_output)

        asset_batch_input.assets = list()

    if len(tree_batch_input.relationships) > 0:
        trees_api.batch_move_nodes_to_parents(body=tree_batch_input)  # type: ItemBatchOutputV1
        tree_batch_input.relationships = list()


def _add_data_properties(item, datasource_class, datasource_id, data_id):
    """
    Add a property with a Data ID for items that do not take a data id in their input

    :param item: The output of item creation containing the item's seeq ID
    :param datasource_class: The datasource class to apply to the item
    :param datasource_id: The datasource id to apply to the item
    :param data_id: The data id to add to the item
    :return:
    """
    items_api = ItemsApi(_login.client)
    properties_input = [
        ScalarPropertyV1(unit_of_measure='string', name='Datasource Class', value=datasource_class),
        ScalarPropertyV1(unit_of_measure='string', name='Datasource ID', value=datasource_id),
        ScalarPropertyV1(unit_of_measure='string', name='Data ID', value=data_id)
    ]
    items_api.set_properties(id=item.id, body=properties_input)


def _convert_thresholds_dict_to_input(thresholds_dict, workbook_id, push_results_df):
    """
    Convert a dictionary with keys threshold levels and values of either scalars or metadata to a list of strings
    with level=value/ID of the threshold.

    :param thresholds_dict: A dictionary with keys of threshold levels and values of either number of metadata
    dataframes
    :return:  A list of strings 'level=value' or 'level=ID'
    """

    thresholds_list = list()
    if thresholds_dict:
        for k, v in thresholds_dict.items():
            if isinstance(v, pd.DataFrame) or isinstance(v, dict):
                thresholds_list.append('{}={}'.format(k, _item_id_from_dict_value(v, workbook_id, push_results_df)))
            else:
                thresholds_list.append('{}={}'.format(k, v))
    return thresholds_list


def _add_no_dupe(lst, obj, attr='data_id', overwrite=False):
    for i in range(0, len(lst)):
        o = lst[i]
        if hasattr(o, attr):
            if getattr(o, attr) == getattr(obj, attr):
                if overwrite:
                    lst[i] = obj
                return 0

    lst.append(obj)
    return 1


def _reify_path(path, workbook_id, datasource_output, scoped_data_id, cache, roots, asset_batch_input,
                tree_batch_input, sync_token, status):
    path_items = re.split(r'\s*>>\s*', path.strip())

    root_data_id = _get_scoped_data_id({
        'Name': '',
        'Type': 'Asset'
    }, workbook_id)

    path_so_far = list()

    parent_data_id = root_data_id
    child_data_id = root_data_id
    for path_item in path_items:
        if len(path_item) == 0:
            raise ValueError('Path contains blank / zero-length segments: "%s"' % path)

        asset_input = AssetInputV1()
        asset_input.name = path_item
        asset_input.scoped_to = workbook_id
        asset_input.host_id = datasource_output.id
        asset_input.sync_token = sync_token

        tree_input = AssetTreeSingleInputV1()
        tree_input.parent_data_id = parent_data_id

        path_so_far.append(path_item)

        child_data_id = _get_scoped_data_id({
            'Name': path_so_far[-1],
            'Path': ' >> '.join(path_so_far[0:-1]),
            'Type': 'Asset'
        }, workbook_id)

        asset_input.data_id = child_data_id
        tree_input.child_data_id = child_data_id

        if asset_input.data_id not in cache:
            if tree_input.parent_data_id != root_data_id:
                status.df['Relationship'] += 1
                tree_batch_input.relationships.append(tree_input)
            else:
                roots[asset_input.data_id] = asset_input

            status.df['Asset'] += _add_no_dupe(asset_batch_input.assets, asset_input)

            cache[asset_input.data_id] = True

        parent_data_id = child_data_id

    tree_input = AssetTreeSingleInputV1()
    tree_input.parent_data_id = child_data_id
    tree_input.child_data_id = scoped_data_id
    status.df['Relationship'] += _add_no_dupe(tree_batch_input.relationships, tree_input, 'child_data_id')
