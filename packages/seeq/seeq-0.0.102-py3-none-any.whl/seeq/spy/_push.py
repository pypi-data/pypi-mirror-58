import json
import re
import six
import time

import pandas as pd
import numpy as np

from seeq.sdk import *

from . import _common
from . import _config
from . import _login
from . import _metadata

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
        _metadata.dict_to_datasource_input(datasource, datasource_input)

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
        push_result_df = _metadata.push(metadata, workbook_id, datasource_output, archive, errors, status)

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

            d['Data ID'] = _metadata.get_scoped_data_id(d, workbook_id)

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


def _push_signal(column, signal_metadata, data, earliest_sample, latest_sample, signals_api, workstep_json,
                 type_mismatches, status_index, status, update_status):
    signal_input = SignalInputV1()
    _metadata.dict_to_signal_input(signal_metadata, signal_input)
    put_samples_input = PutSamplesInputV1()
    put_samples_input.samples = list()
    count = 0
    is_string = None
    # noinspection PyTypeChecker
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


def _push_condition(condition_metadata, conditions_api, data, earliest_sample, latest_sample, status_index, status,
                    update_status):
    condition_batch_input = ConditionBatchInputV1()
    condition_input = ConditionInputV1()
    _metadata.dict_to_condition_input(condition_metadata, condition_input)
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


def _dict_to_capsule(d, capsule):
    _metadata.dict_to_input(d, capsule, 'properties', {
        'Capsule Start': None,
        'Capsule End': None
    })
