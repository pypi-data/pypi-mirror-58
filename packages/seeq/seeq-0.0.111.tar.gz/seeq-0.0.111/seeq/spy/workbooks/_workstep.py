import json
import os
import re
import pytz

import pandas as pd
import numpy as np

from seeq.sdk import *

from . import _item
from ._data import StoredOrCalculatedItem
from ._item import Item, Reference

from .. import _common
from .. import _login


class Workstep(Item):
    def __new__(cls, *args, **kwargs):
        if cls is Workstep:
            raise TypeError("Workstep may not be instantiated directly, create either AnalysisWorkstep or "
                            "TopicWorkstep")

        return object.__new__(cls)

    def __init__(self, worksheet, definition=None):
        super().__init__(definition)

        self.worksheet = worksheet
        self.worksheet.worksteps[self.definition['ID']] = self
        if 'Data' not in self.definition:
            self.definition['Data'] = json.loads(_common.DEFAULT_WORKBOOK_STATE)

    @staticmethod
    def _instantiate(worksheet, workstep_id):
        if worksheet.workbook['Workbook Type'] == 'Analysis':
            return AnalysisWorkstep(worksheet, {'ID': workstep_id})
        else:
            return TopicWorkstep(worksheet, {'ID': workstep_id})

    @staticmethod
    def pull(workstep_tuple, *, worksheet=None):
        # Note that worksteps from other workbooks/worksheets can be referenced in Journals due to copy/paste
        # operations, so we can't assume that this workstep's self.worksheet actually represents the one to pull.
        workbook_id, worksheet_id, workstep_id = workstep_tuple
        workstep = Workstep._instantiate(worksheet, workstep_id)
        workstep._pull(workstep_tuple)
        return workstep

    def _pull(self, workstep_tuple):
        workbook_id, worksheet_id, workstep_id = workstep_tuple
        workbooks_api = WorkbooksApi(_login.client)
        workstep_output = workbooks_api.get_workstep(workbook_id=workbook_id,
                                                     worksheet_id=worksheet_id,
                                                     workstep_id=workstep_id)  # type: WorkstepOutputV1

        self.definition['Data'] = json.loads(workstep_output.data)

    def push_to_specific_worksheet(self, pushed_workbook_id, pushed_worksheet_id, item_map):
        workbooks_api = WorkbooksApi(_login.client)

        item_map = item_map if item_map is not None else dict()

        workstep_input = WorkstepInputV1()
        if self.data:
            workstep_input.data = _item.replace_items(json.dumps(self.data), item_map)

        workstep_output = workbooks_api.create_workstep(
            workbook_id=pushed_workbook_id, worksheet_id=pushed_worksheet_id,
            body=workstep_input)  # type: WorkstepOutputV1

        item_map[self.id.upper()] = workstep_output.id.upper()

        # Look at all referenced items on this workstep to see if there ancillaries and if so, push them. Note that
        # we only push ancillaries that are actually referenced by a workstep so that we conserve on how many
        # StoredSignals we actually touch.
        for referenced_item in self.referenced_items:  # type: Reference
            if referenced_item.id not in self.worksheet.workbook.item_inventory:
                # There are lots of IDs in a workstep that may not be relevant items for export
                continue

            item = self.worksheet.workbook.item_inventory[referenced_item.id]
            if 'Ancillaries' in item:
                if isinstance(item, StoredOrCalculatedItem):
                    try:
                        item.push_ancillaries(self.worksheet.workbook.id, pushed_workbook_id, item_map)
                    except KeyboardInterrupt:
                        raise
                    except BaseException as e:
                        self.worksheet.workbook.item_errors.add((item, _common.format_exception(e)))

        return workstep_output.id

    @property
    def data(self):
        return _common.get(self.definition, 'Data', default=dict())

    @property
    def referenced_items(self):
        referenced_items = list()

        matches = re.finditer(_common.GUID_REGEX, json.dumps(self.data), re.IGNORECASE)

        for match in matches:
            referenced_items.append(Reference(match.group(0).upper(), Reference.DETAILS, self.worksheet))

        return referenced_items

    def get_workstep_stores(self):
        workstep_data = _common.get(self.definition, 'Data', default=dict(), assign_default=True)
        workstep_state = _common.get(workstep_data, 'state', default=dict(), assign_default=True)
        return _common.get(workstep_state, 'stores', default=dict(), assign_default=True)

    @staticmethod
    def _get_workstep_json_file(workbook_folder, worksheet_id, workstep_id):
        return os.path.join(workbook_folder, 'Worksheet_%s_Workstep_%s.json' % (worksheet_id, workstep_id))

    def save(self, workbook_folder):
        workstep_json_file = Workstep._get_workstep_json_file(workbook_folder, self.worksheet.id, self.id)
        with open(workstep_json_file, 'w', encoding='utf-8') as f:
            json.dump(self.definition, f, indent=4)

    def _load(self, workbook_folder, workstep_id):
        workstep_json_file = Workstep._get_workstep_json_file(workbook_folder, self.worksheet.id, workstep_id)

        with open(workstep_json_file, 'r', encoding='utf-8') as f:
            self.definition = json.load(f)

    @staticmethod
    def load_from_workbook_folder(worksheet, workbook_folder, workstep_id):
        workstep = Workstep._instantiate(worksheet, workstep_id)
        workstep._load(workbook_folder, workstep_id)
        return workstep

    def _get_store(self, store_name):
        workstep_stores = self.get_workstep_stores()
        return _common.get(workstep_stores, store_name, default=dict(), assign_default=True)


class AnalysisWorkstep(Workstep):
    def __init__(self, worksheet, definition=None):
        super().__init__(worksheet, definition)

        # initialize displayed items
        if self.display_items.empty:
            display_items_stores = self._store_map_from_type('all')
            stores = self.get_workstep_stores()
            for store in display_items_stores:
                current_store = _common.get(stores, store, default=dict(), assign_default=True)
                current_store['items'] = []

        # initialize the display and investigate ranges
        if self.display_range is None and self.investigate_range is None:
            self._set_display_range({'Start': pd.datetime.now() - pd.Timedelta(days=1), 'End': pd.datetime.now()},
                                    check_investigate=False)
            self._set_investigate_range({'Start': pd.datetime.now() - pd.Timedelta(days=7), 'End': pd.datetime.now()},
                                        check_display=False)
        # initialize the view
        if self.view is None:
            self._set_view_key()

    @property
    def display_items(self):
        return self._get_display_items()

    @display_items.setter
    def display_items(self, value):
        self._set_display_items(value)

    @property
    def display_range(self):
        return self._get_display_range()

    @display_range.setter
    def display_range(self, value):
        self._set_display_range(value)

    @property
    def investigate_range(self):
        return self._get_investigate_range()

    @investigate_range.setter
    def investigate_range(self, value):
        self._set_investigate_range(value)

    @property
    def view(self):
        return self._get_view_key()

    @view.setter
    def view(self, value):
        self._set_view_key(value)

    @property
    def timezone(self):
        return self._get_timezone()

    @timezone.setter
    def timezone(self, value):
        self._set_timezone(value)

    def _get_timezone(self):
        worksheet_store = self._get_store('sqWorksheetStore')
        timezone = _common.get(worksheet_store, 'timezone')
        return timezone

    def _set_timezone(self, timezone):
        if timezone not in pytz.all_timezones:
            raise RuntimeError(f'The timezone {timezone} is not a known timezone')
        worksheet_store = self._get_store('sqWorksheetStore')
        worksheet_store['timezone'] = timezone

    def _get_display_range(self):
        duration_store = self._get_store('sqDurationStore')
        display_range = _common.get(duration_store, 'displayRange', default=dict())
        if not display_range:
            return None
        start = pd.datetime.fromtimestamp(display_range['start'] / 1000)
        end = pd.datetime.fromtimestamp(display_range['end'] / 1000)
        return {'Start': start.isoformat(), 'End': end.isoformat()}

    def _set_display_range(self, display_start_end, check_investigate=True):
        if isinstance(display_start_end, pd.DataFrame):
            if len(display_start_end) > 1:
                raise RuntimeError('Display Range DataFrames are limited to one row')
            display_start_end = display_start_end.squeeze()
        start_ts = display_start_end['Start']
        end_ts = display_start_end['End']

        if not isinstance(start_ts, (str, pd.datetime)) or not isinstance(end_ts, (str, pd.datetime)):
            raise RuntimeError('Display range times must be ISO8601 strings or pandas datetime objects')
        try:
            if isinstance(start_ts, str):
                start_ts = pd.datetime.fromisoformat(start_ts)
            if isinstance(end_ts, str):
                end_ts = pd.datetime.fromisoformat(end_ts)
        except ValueError as e:
            raise RuntimeError(f'Display range times must be valid ISO8601 strings. Error parsing dates: {e}')

        if check_investigate:
            investigate_range = self.investigate_range
            if investigate_range is None:
                self._set_investigate_range(display_start_end, check_display=False)
            else:
                i_start = pd.datetime.fromisoformat(investigate_range['Start'])
                i_end = pd.datetime.fromisoformat(investigate_range['End'])
                i_duration = i_end - i_start
                if i_duration < end_ts - start_ts:
                    self._set_investigate_range(display_start_end, check_display=False)
                elif start_ts > i_end:
                    self._set_investigate_range({'Start': end_ts - i_duration, 'End': end_ts}, check_display=False)
                elif end_ts < i_start:
                    self._set_investigate_range({'Start': start_ts, 'End': start_ts + i_duration}, check_display=False)

        start_ts = start_ts.timestamp() * 1000
        end_ts = end_ts.timestamp() * 1000
        duration_store = self._get_store('sqDurationStore')
        auto_update = _common.get(duration_store, 'autoUpdate', default=dict(), assign_default=True)
        auto_update['offset'] = end_ts - pd.datetime.now().timestamp() * 1000
        display_range = _common.get(duration_store, 'displayRange', default=dict(), assign_default=True)
        display_range['start'] = start_ts
        display_range['end'] = end_ts

    def _get_investigate_range(self):
        duration_store = self._get_store('sqDurationStore')
        investigate_range = _common.get(duration_store, 'investigateRange', default=None)
        if investigate_range is None:
            return None
        start = pd.datetime.fromtimestamp(investigate_range['start'] / 1000).isoformat()
        end = pd.datetime.fromtimestamp(investigate_range['end'] / 1000).isoformat()
        return {'Start': start, 'End': end}

    def _set_investigate_range(self, investigate_start_end, check_display=True):
        if isinstance(investigate_start_end, pd.DataFrame):
            if len(investigate_start_end) > 1:
                raise RuntimeError('Investigate Range DataFrames are limited to one row ')
            investigate_start_end = investigate_start_end.squeeze()
        start_ts = investigate_start_end['Start']
        end_ts = investigate_start_end['End']

        if not isinstance(start_ts, (str, pd.datetime)) or not isinstance(end_ts, (str, pd.datetime)):
            raise RuntimeError('Investigate range times must be ISO8601 strings or pandas datetime objects')
        try:
            if isinstance(start_ts, str):
                start_ts = pd.datetime.fromisoformat(start_ts)
            if isinstance(end_ts, str):
                end_ts = pd.datetime.fromisoformat(end_ts)
        except ValueError as e:
            raise RuntimeError(f'Investigate range times must be valid ISO8601 strings. Error parsing dates: {e}')

        if check_display:
            display_range = self.display_range
            if display_range is None:
                self._set_display_range(investigate_start_end, check_investigate=False)
            else:
                d_start = pd.datetime.fromisoformat(display_range['Start'])
                d_end = pd.datetime.fromisoformat(display_range['End'])
                d_duration = d_end - d_start
                if d_duration > end_ts - start_ts:
                    self._set_display_range(investigate_start_end, check_investigate=False)
                elif d_start > end_ts:
                    self._set_display_range({'Start': end_ts - d_duration, 'End': end_ts}, check_investigate=False)
                elif d_end < start_ts:
                    self._set_display_range({'Start': start_ts, 'End': start_ts + d_duration}, check_investigate=False)

        start_ts = start_ts.timestamp() * 1000
        end_ts = end_ts.timestamp() * 1000
        duration_store = self._get_store('sqDurationStore')
        duration_store['investigateRange'] = {'start': start_ts, 'end': end_ts}

    @staticmethod
    def _validate_input(df):
        for col in ['ID', 'Type', 'Name']:
            if col not in df.columns:
                raise RuntimeError('%s column required in display_items DataFrame' % col)

        if any(df.duplicated(['ID'])):
            raise RuntimeError('Duplicate IDs detected in display_items DataFrame')

    def _set_display_items(self, items_df):
        AnalysisWorkstep._validate_input(items_df)

        workstep_stores = self.get_workstep_stores()

        # get the axes identifiers and convert them to the canonical "A", "B", "C"...
        axis_map = dict()
        if _common.present(items_df, 'Axis Group'):
            axis_map = AnalysisWorkstep._generate_axis_map(items_df['Axis Group'])

        # clear all items from the workstep
        for store_name in self._store_map_from_type('all'):
            store = _common.get(workstep_stores, store_name, default=dict(), assign_default=True)
            store['items'] = []

        lanes = set()
        axes = set()
        for _, item in items_df.iterrows():
            store_name = self._store_map_from_type(item['Type'])
            if not store_name:
                continue
            store_items = _common.get(workstep_stores, store_name)['items']
            store_items.append(dict())
            store_items[-1]['name'] = item['Name']
            store_items[-1]['id'] = item['ID']
            for column in item.keys():
                if column in self._workstep_display_user_to_workstep:
                    value = _common.get(item, column)
                    if pd.notna(value):
                        if column == 'Line':
                            value = self._workstep_dashStyle_user_to_workstep[value]
                        elif column == 'Samples':
                            value = self._workstep_sampleDisplay_user_to_workstep[value]
                        elif column == 'Axis Group':
                            value = axis_map[value]
                            axes.add(value)
                        elif column == 'Lane':
                            value = int(value) if int(value) > 0 else 1
                            lanes.add(value)
                        elif column == 'Line Width':
                            value = value if value > 0 else 1
                        elif column == 'Align':
                            value = self._workstep_rightAxis_user_to_workstep[value]
                        store_items[-1][self._workstep_display_user_to_workstep[column]] = value
            if 'lane' not in store_items[-1]:
                if lanes:
                    store_items[-1]['lane'] = max(lanes) + 1
                else:
                    store_items[-1]['lane'] = 1
                lanes.add(store_items[-1]['lane'])
            if 'axisAlign' not in store_items[-1]:
                if axes:
                    max_axis_number = max(list(map(
                        lambda x: AnalysisWorkstep.axes_number_from_identifier(x), list(axes))))
                    store_items[-1]['axisAlign'] = AnalysisWorkstep.axes_identifier_from_number(max_axis_number + 1)
                else:
                    store_items[-1]['axisAlign'] = 'A'
                axes.add(store_items[-1]['axisAlign'])

    def _get_display_items(self, item_type='all'):
        """
        Get the items of a given type displayed in the workstep, regardless of the worksheet view.

        Parameters
        ----------
        item_type : {'all', 'signals', 'conditions', 'scalars', 'metrics', 'tables'}, default 'all'
            The type of items to return.

        Returns
        -------
        {pandas.DataFrame, None}
            A list of the items present in the workstep or None if there is not workstep.data
        """
        if not self.data:
            return

        stores = list()
        if item_type in ['all', 'signals']:
            stores.append('sqTrendSeriesStore')
        if item_type in ['all', 'conditions']:
            stores.append('sqTrendCapsuleSetStore')
        if item_type in ['all', 'scalars']:
            stores.append('sqTrendScalarStore')
        if item_type in ['all', 'metrics']:
            stores.append('sqTrendMetricStore')
        if item_type in ['all', 'tables']:
            stores.append('sqTrendTableStore')

        items = list()
        for store in stores:
            workstep_store = self._get_store(store)
            for item in _common.get(workstep_store, 'items', default=list(), assign_default=True):
                output_item = dict()
                output_item['Name'] = item['name'] if 'name' in item else np.nan
                output_item['ID'] = item['id']
                output_item['Type'] = AnalysisWorkstep._type_from_store_name(store)
                for k in self._workstep_display_workstep_to_user.keys():
                    if k in item:
                        value = item[k]
                        if k == 'dashStyle':
                            output_item[self._workstep_display_workstep_to_user[k]] = \
                                self._workstep_dashStyle_workstep_to_user[value]
                        elif k == 'sampleDisplayOption':
                            output_item[self._workstep_display_workstep_to_user[k]] = \
                                self._workstep_sampleDisplay_workstep_to_user[value]
                        elif k == 'rightAxis':
                            output_item[self._workstep_display_workstep_to_user[k]] = \
                                self._workstep_rightAxis_workstep_to_user[value]
                        else:
                            output_item[self._workstep_display_workstep_to_user[k]] = value
                items.append(output_item)
        return pd.DataFrame(items)

    @staticmethod
    def _store_map_from_type(item_type):
        """
        Return a list with the name of the workstep store corresponding to the item type give.
        :param item_type: The string type of the item. If 'all' all stores will be returned
        :return: str store name, for all item_types except 'all'. If item_type == 'all', a tuple of all the store
        names. If item_type is not recognized, returns None.
        """
        if not item_type or not isinstance(item_type, str):
            return None

        if 'Signal' in item_type:
            return 'sqTrendSeriesStore'
        if 'Condition' in item_type:
            return 'sqTrendCapsuleSetStore'
        if 'Scalar' in item_type:
            return 'sqTrendScalarStore'
        if 'Metric' in item_type:
            return 'sqTrendMetricStore'
        if 'Table' in item_type:
            return 'sqTrendTableStore'
        if item_type == 'all':
            return ('sqTrendSeriesStore', 'sqTrendCapsuleSetStore', 'sqTrendScalarStore', 'sqTrendMetricStore',
                    'sqTrendTableStore')
        else:
            return None

    @staticmethod
    def _type_from_store_name(store_name):
        """
        Return the type of an item that is stored in a given data store
        Parameters
        ----------
        store_name : str
            The name of the data store

        Returns
        -------
        str
            The item type
        """
        if not store_name or not isinstance(store_name, str):
            return None

        store_map = {
            'sqTrendSeriesStore': 'Signal',
            'sqTrendCapsuleSetStore': 'Condition',
            'sqTrendScalarStore': 'Scalar',
            'sqTrendMetricStore': 'Metric',
            'sqTrendTableStore': 'Table'
        }

        if store_name not in store_map:
            return None

        return store_map[store_name]

    _workstep_display_user_to_workstep = {
        'Color': 'color',
        'Line': 'dashStyle',
        'Line Width': 'lineWidth',
        'Lane': 'lane',
        'Axis': 'axisAlign',
        'Samples': 'sampleDisplayOption',
        'Axis Auto Scale': 'axisAutoScale',
        'Axis Limits': 'yAxisConfig',
        'Align': 'rightAxis',
        'Axis Group': 'axisAlign',
        'Stack': 'stack'
    }

    _workstep_display_workstep_to_user = dict((v, k) for k, v in _workstep_display_user_to_workstep.items())

    _workstep_sampleDisplay_user_to_workstep = {
        'Line': 'line',
        'Line and Sample': 'lineAndSample',
        'Samples': 'sample',
        'Bars': 'bar'
    }

    _workstep_sampleDisplay_workstep_to_user = dict((v, k) for k, v in _workstep_sampleDisplay_user_to_workstep.items())

    _workstep_dashStyle_user_to_workstep = {
        'Solid': 'Solid',
        'Short Dash': 'ShortDash',
        'Short Dash-Dot': 'ShortDashDot',
        'Short Dash-Dot-Dot': 'ShortDashDotDot',
        'Dot': 'Dot',
        'Dash': 'Dash',
        'Long Dash': 'LongDash',
        'Dash-Dot': 'DashDot',
        'Long Dash-Dot': 'LongDashDot',
        'Long Dash-Dot-Dot': 'LongDashDotDot'
    }

    _workstep_dashStyle_workstep_to_user = dict((v, k) for k, v in _workstep_dashStyle_user_to_workstep.items())

    _workstep_rightAxis_user_to_workstep = {
        'Right': True,
        'Left': False
    }

    _workstep_rightAxis_workstep_to_user = dict((v, k) for k, v in _workstep_rightAxis_user_to_workstep.items())

    @staticmethod
    def _generate_axis_map(axis_group):
        specified_axes = axis_group.dropna().drop_duplicates().to_list()
        canonical_axes = list(AnalysisWorkstep.axes_identifier_list_from_number(len(specified_axes)))
        axis_map = dict()
        for ax in specified_axes:
            if ax in canonical_axes:
                axis_map[ax] = ax
                canonical_axes.remove(ax)
                continue
            else:
                axis_map[ax] = canonical_axes[0]
                del canonical_axes[0]
        return axis_map

    @staticmethod
    def axes_identifier_list_from_number(n):
        """
        A Generator that produces a canonical list of axes identifiers of the
        form "A", "B", "C",..., "AA", "AB", "AC",...
        Parameters
        ----------
        n : integer
            The number of identifiers required.

        Returns
        -------
        str
            The string for the current axis identifier.
        """
        generated = 0

        while generated < n:
            yield AnalysisWorkstep.axes_identifier_from_number(generated)
            generated += 1

    @staticmethod
    def axes_identifier_from_number(number):
        decimal_a, number_letters = 65, 26

        if number >= number_letters:
            return AnalysisWorkstep.axes_identifier_from_number(number // number_letters - 1) + \
                   chr(number % number_letters + decimal_a)
        else:
            return chr(number % number_letters + decimal_a)

    @staticmethod
    def axes_number_from_identifier(axis_id):
        """
        Converts from an alpha axis identifier, eg "A", "B",...,"AA", "AB",...
        to a decimal, essentially doing a conversion from base 26 to base 10.

        Parameters
        ----------
        axis_id: str
            The alpha identifier

        Returns
        -------
        int
            Integer base 10 equivalent
        """
        decimal_a, number_letters = 65, 26
        base_26_multipliers = [ord(i) + 1 - decimal_a for i in axis_id]
        base_10_components = \
            [b26 * number_letters ** (len(base_26_multipliers) - 1 - i) for i, b26 in enumerate(base_26_multipliers)]
        return sum(base_10_components)

    @staticmethod
    def add_display_columns(df, inplace):
        """
        See documentation for Worksheet.add_display_attribute_columns
        """
        working_df = df.copy(deep=True) if not inplace else df

        for attribute in AnalysisWorkstep._workstep_display_user_to_workstep.keys():
            if attribute not in working_df:
                working_df[attribute] = pd.np.nan

        return None if inplace else working_df

    def _get_view_key(self):
        """
        Get the view of the current workstep. If no view key is found the default value is returned
        :return: str view key
        """
        workstep_stores = self.get_workstep_stores()
        worksheet_store = _common.get(workstep_stores, 'sqWorksheetStore', default=dict(), assign_default=True)
        if 'viewKey' in workstep_stores:
            return self._view_key_workstep_to_user[worksheet_store['viewKey']]
        else:
            return None

    def _set_view_key(self, view='Trend'):
        if view not in self._view_key_user_to_workstep.keys():
            raise RuntimeError(f'The view key "{view}" is not recognized. Valid values are '
                               f'{self._view_key_user_to_workstep.keys()}')

        workstep_stores = self.get_workstep_stores()
        worksheet_store = _common.get(workstep_stores, 'sqWorksheetStore', default=dict(), assign_default=True)
        worksheet_store['viewKey'] = self._view_key_user_to_workstep[view]

    _view_key_user_to_workstep = {
        'Scorecard': 'SCORECARD',
        'Treemap': 'TREEMAP',
        'Scatter Plot': 'SCATTER',
        'Trend': 'TREND'
    }
    _view_key_workstep_to_user = dict((v, k) for k, v in _view_key_user_to_workstep.items())


class TopicWorkstep(Workstep):
    @property
    def date_ranges(self):
        return self._get_date_ranges()

    @date_ranges.setter
    def date_ranges(self, value):
        self._set_date_ranges(value)

    def _get_date_ranges(self):
        report_store = self._get_store('sqReportStore')
        date_variables = _common.get(report_store, 'dateVariables', default=None)
        if date_variables is None:
            return None
        output_dates = [AnalysisWorkstep._date_range_workstep_to_user(d) for d in date_variables]
        return pd.DataFrame(output_dates)

    @staticmethod
    def _date_range_workstep_to_user(date_range):
        dr_columns = ['ID', 'Name', 'Start', 'End', 'Auto Enabled', 'Auto Duration', 'Auto Offset',
                      'Auto Offset Direction', 'Auto Refresh Rate', 'Condition ID', 'Condition Name',
                      'Condition Strategy', 'Condition Reference', 'Condition Offset']
        dr = {c: pd.np.nan for c in dr_columns}

        dr['ID'] = date_range['id']
        dr['Name'] = date_range['name']
        if 'range' in date_range:
            _common.test_and_set(dr, 'Start', date_range['range'], 'start')
            _common.test_and_set(dr, 'End', date_range['range'], 'end')
        if 'auto' in date_range:
            _common.test_and_set(dr, 'Auto Enabled', date_range['auto'], 'enabled')
            _common.test_and_set(dr, 'Auto Duration', date_range['auto'], 'duration', lambda x: str(x / 1000) + 's')
            if 'offset' in date_range['auto']:
                _offset = date_range['auto']['offset']
                if 'value' in _offset and 'units' in _offset:
                    dr['Auto Offset'] = str(_offset['value']) + _offset['units']
            _common.test_and_set(dr, 'Auto Offset Direction', date_range['auto'], 'offsetDirection',
                                 lambda x: str.capitalize(x))
            if 'rate' in date_range['auto']:
                _rate = date_range['auto']['rate']
                if 'value' in _rate and 'units' in _rate:
                    dr['Auto Refresh Rate'] = str(_rate['value']) + _rate['units']
        if 'condition' in date_range:
            _common.test_and_set(dr, 'Condition ID', date_range['condition'], 'id')
            _common.test_and_set(dr, 'Condition Name', date_range['condition'], 'name')
            if 'strategy' in date_range['condition']:
                if date_range['condition']['strategy'] == 'closestTo':
                    dr['Condition Strategy'] = 'Closest To'
                elif date_range['condition']['strategy'] == 'offsetBy':
                    dr['Condition Strategy'] = 'Offset By'
            _common.test_and_set(dr, 'Condition Reference', date_range['condition'], 'reference',
                                 lambda x: str.capitalize(x))
            _common.test_and_set(dr, 'Condition Offset', date_range['condition'], 'offset')
        return dr

    def _set_date_ranges(self, date_ranges):
        date_range_list = list()
        if isinstance(date_ranges, pd.DataFrame):
            date_ranges = date_ranges.to_dict('records')
        for d in date_ranges:
            AnalysisWorkstep._validate_user_date_range(d)
            date_range_list.append(AnalysisWorkstep._date_range_user_to_workstep(d))
        report_store = self._get_store('sqReportStore')
        report_store['dateVariables'] = date_range_list

    @staticmethod
    def _date_range_user_to_workstep(date_range):
        """
        Converts a user specified date range to a dict for inclusion in the workstep. See _set_date_ranges
        for parameter explanation
        :param date_range: dict, single row pd.DataFrame, pd.Series
        :return: dict workstep daterange
        """

        # convert DataFrames and Series to a dict
        if isinstance(date_range, pd.DataFrame):
            if len(date_range) > 1:
                raise RuntimeError('This method can only accept one row of a DataFrame at a time')
            date_range = date_range.squeeze()
        if isinstance(date_range, pd.Series):
            date_range = date_range.to_dict()

        # defaults for the different aspects of the date range
        def _defaults(c_dr):
            _common.test_and_set(c_dr, 'id', date_range, 'ID', default_value=_common.new_placeholder_guid(),
                                 retain_target=False)
            c_dr['name'] = date_range['Name']

        def _range_defaults(c_dr):
            _range = _common.get(c_dr, 'range', default=dict(), assign_default=True)
            _range['start'] = (pd.datetime.now() - pd.Timedelta(days=1)).timestamp() * 1000
            _range['end'] = pd.datetime.now().timestamp() * 1000

        def _auto_defaults(c_dr):
            _auto = _common.get(c_dr, 'auto', default=dict(), assign_default=True)
            _auto['enabled'] = False
            _auto['duration'] = pd.Timedelta(days=1).total_seconds() * 1000
            _auto['offset'] = dict()
            _auto['offset']['value'] = 0
            _auto['offset']['units'] = 'min'
            _auto['offsetDirection'] = 'past'
            _auto['rate'] = dict()
            _auto['rate']['value'] = 5
            _auto['rate']['units'] = 'min'

        def _condition_defaults(c_dr):
            _condition = _common.get(c_dr, 'condition', default=dict(), assign_default=True)
            _condition['strategy'] = 'closestTo'
            _condition['reference'] = 'end'
            _condition['offset'] = 1

        dr = dict()
        _defaults(dr)
        _range_defaults(dr)
        _auto_defaults(dr)
        _condition_defaults(dr)
        _common.test_and_set(dr['range'], 'start', date_range, 'Start')
        _common.test_and_set(dr['range'], 'end', date_range, 'End')
        _common.test_and_set(dr['auto'], 'enabled', date_range, 'Auto Enabled', )
        _common.test_and_set(dr['auto'], 'duration', date_range, 'Auto Duration',
                             lambda x: _common.parse_str_time_to_ms(x)[2])
        _common.test_and_set(dr['auto']['offset'], 'value', date_range, 'Auto Offset',
                             lambda x: _common.parse_str_time_to_ms(x)[0])
        _common.test_and_set(dr['auto']['offset'], 'units', date_range, 'Auto Offset',
                             lambda x: _common.parse_str_time_to_ms(x)[1])
        _common.test_and_set(dr['auto'], 'offsetDirection', date_range, 'Auto Offset Direction', lambda x: str.lower(x))
        _common.test_and_set(dr['auto']['rate'], 'value', date_range, 'Auto Refresh Rate',
                             lambda x: _common.parse_str_time_to_ms(x)[0])
        _common.test_and_set(dr['auto']['rate'], 'units', date_range, 'Auto Refresh Rate',
                             lambda x: _common.parse_str_time_to_ms(x)[1])
        _common.test_and_set(dr['condition'], 'offset', date_range, 'Condition Offset', lambda x: str.lower(x))
        _common.test_and_set(dr['condition'], 'strategy', date_range, 'Condition Strategy', lambda x: str.lower(x))
        _common.test_and_set(dr['condition'], 'reference', date_range, 'Condition Reference', lambda x: str.lower(x))
        _common.test_and_set(dr['condition'], 'id', date_range, 'Condition ID')
        _common.test_and_set(dr['condition'], 'name', date_range, 'Condition Name')
        return dr

    @staticmethod
    def _validate_user_date_range(date_range):
        errors = []
        if 'Name' not in date_range:
            raise RuntimeError('All date ranges require a "Name"')
        # if auto enabled is defined, all the other auto fields must be defined.
        if 'Auto Enabled' in date_range and date_range['Auto Enabled']:
            if 'Auto Offset' not in date_range:
                errors.append('"Auto Offset" is required if "Auto Enabled" is True')
            if 'Auto Duration' not in date_range:
                errors.append('"Auto Duration" is required if "Auto Enabled" is True')
            if 'Auto Offset Direction' not in date_range:
                errors.append('"Auto Offset Direction" is required if "Auto Enabled" is True')
        if 'Condition ID' in date_range or 'Condition Name' in date_range:
            if 'Condition ID' not in date_range:
                errors.append('"Condition ID" must be supplied with "Condition Name"')
            if 'Condition Name' not in date_range:
                errors.append('"Condition Name" must be supplied with "Condition ID"')
            if 'Condition Strategy' not in date_range:
                errors.append('"Condition Strategy" must be supplied with "Condition Name" and "Condition ID"')
            if 'Condition Offset' not in date_range:
                errors.append('"Condition Offset" must be supplied with "Condition Name" and "Condition ID"')
            if 'Condition Reference' not in date_range:
                errors.append('"Condition Reference" must be supplied with "Condition Name" and "Condition ID"')
        if errors:
            msg = f'There was 1 error ' if len(errors) == 1 else f'There were {len(errors)} errors '
            msg += f'detected in date range "{date_range["Name"]}": {errors}'
            raise RuntimeError(msg)
