import datetime
import json
import pytz
import re
import six
import sys
import traceback
import uuid

from seeq.sdk import *
from seeq.sdk.rest import ApiException

from IPython.core.display import display, HTML, clear_output

import pandas as pd
import numpy as np

DEFAULT_DATASOURCE_NAME = 'Seeq Data Lab'
DEFAULT_DATASOURCE_CLASS = 'Seeq Data Lab'
DEFAULT_DATASOURCE_ID = 'Seeq Data Lab'
DEFAULT_WORKBOOK_PATH = 'Data Lab >> Data Lab Analysis'
DEFAULT_WORKBOOK_TYPE = 'Analysis'
DEFAULT_WORKBOOK_NAME = DEFAULT_WORKBOOK_PATH.split('>>')[-1].strip()
DEFAULT_SEARCH_PAGE_SIZE = 100
DEFAULT_PULL_PAGE_SIZE = 1000000
DEFAULT_PUT_SAMPLES_AND_CAPSULES_BATCH_SIZE = 100000
DEFAULT_WORKBOOK_STATE = '{"version":1, "state":{"stores":{}}}'
DEFAULT_THREAD_POOL_SIZE = 8


class DependencyNotFound(Exception):

    def __init__(self, identifier, message=None):
        self.identifier = identifier
        self.message = message

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        rep = ''
        if self.identifier:
            rep = rep + self.identifier
        if self.message:
            rep = rep + '\n' if len(rep) > 0 else ''
            rep = rep + self.message

        return rep


def present(row, column):
    return (column in row) and \
           (row[column] is not None) and \
           (not isinstance(row[column], float) or not pd.isna(row[column]))


def get(row, column, default=None, assign_default=False):
    """
    Get the value in the column of a row. Can also accept dictionaries.
    Optionally define a default value/type to return and indicate if the
    default should be assigned to the row[column]. For example,

    >>> get(row, column, default=dict(), assign=False)
    if there is no value in row[column] a new dictionary will be returned

    >>> get(row, column, default=dict(), assign=True)
    if there is no value in row[column] a new dictionary will be assigned
    to row column and that dictionary will be returned

    :param row: The row object. Can be pd.Series, a single row pd.DataFrame, or dict
    :param column: The name of the column to query
    :param default: If the no value is present, the return value/type
    :param assign_default: Flag if the default should be assigned to the row[column]
    :return:
    """
    if present(row, column):
        return row[column]
    d = default
    if assign_default:
        row[column] = d
    return d


def get_timings(http_headers):
    output = dict()
    for header, cast in [('Server-Meters', int), ('Server-Timing', float)]:
        server_meters_string = http_headers[header]
        server_meters = server_meters_string.split(',')
        for server_meter_string in server_meters:
            server_meter = server_meter_string.split(';')
            if len(server_meter) < 3:
                continue

            dur_string = cast(server_meter[1].split('=')[1])
            desc_string = server_meter[2].split('=')[1].replace('"', '')

            output[desc_string] = dur_string

    return output


def format_exception(e=None):
    exception_type = None
    tb = None
    if e is None:
        exception_type, e, tb = sys.exc_info()

    if isinstance(e, ApiException):
        content = ''
        if e.reason and len(e.reason.strip()) > 0:
            if len(content) > 0:
                content += ' - '
            content += e.reason

        if e.body:
            # noinspection PyBroadException
            try:
                body = json.loads(e.body)
                if len(content) > 0:
                    content += ' - '
                content += body['statusMessage']
            except BaseException:
                pass

        return '(%d) %s' % (e.status, content)

    else:
        if tb is not None:
            return traceback.format_exception(exception_type, e, tb)
        else:
            return str(e)


GUID_REGEX = r'[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}'
HTML_EQUALS_REGEX = r'(?:=|&#61;)'


def get_workbook_id_from_url(url):
    results = workbook_worksheet_url_regex(url)
    if results:
        return results.groupdict()['workbook']


def get_worksheet_id_from_url(url):
    results = workbook_worksheet_url_regex(url)
    if results:
        return results.groupdict()['worksheet']


def workbook_worksheet_url_regex(url):
    workbook_regex = re.search(f'/workbook[s]?/(?P<workbook>{GUID_REGEX})/worksheet[s]?/(?P<worksheet>{GUID_REGEX})',
                               url, re.I)
    if workbook_regex:
        return workbook_regex
    workbook_regex = re.search(f'/worksheet[s]?/(?P<workbook>{GUID_REGEX})/(?P<worksheet>{GUID_REGEX})', url, re.I)
    if workbook_regex:
        return workbook_regex
    workbook_regex = re.search(f'/view/(?P<worksheet>{GUID_REGEX})', url, re.I)
    if workbook_regex:
        return workbook_regex
    return None


def get_workstep_id_from_url(url):
    workbook_regex = re.search(f'workstep[s]?/(?P<workstep>{GUID_REGEX})', url, re.I)
    if workbook_regex:
        return workbook_regex.groupdict()['workstep']
    workbook_regex = re.search(f'workstepId=(?P<workstep>{GUID_REGEX})', url, re.I)
    if workbook_regex:
        return workbook_regex.groupdict()['workstep']
    return None


def is_guid(s):
    return isinstance(s, str) and re.match(GUID_REGEX, sanitize_guid(s))


def sanitize_guid(g):
    return g.upper()


def new_placeholder_guid():
    return str(uuid.uuid4()).upper()


def validate_timezone_arg(tz):
    if tz is not None:
        try:
            pd.to_datetime('2019-01-01T00:00:00.000Z').tz_convert(tz)

        except pytz.exceptions.UnknownTimeZoneError:
            raise RuntimeError('Unknown timezone "%s". Acceptable timezones:\n%s' % (tz, '\n'.join(pytz.all_timezones)))


def validate_errors_arg(errors):
    if errors not in ['raise', 'catalog']:
        raise RuntimeError("errors argument must be either 'raise' or 'catalog'")


def time_abbreviation_to_ms_multiplier(abbreviation):
    """
    Given a time abbreviation, returns a multiplier that converts the time
    value to ms and the canonical version of that time abbreviation.
    For example, "6 sec", pass the "sec" to this function and it will
    return (1000, 's'). Multiplying 6 by 1000 gives the duration in ms.

    Parameters
    ----------
    abbreviation : str
        The time abbreviation.  Acceptable values are:
        s, sec, second, seconds
        min, minute, minutes
        h, hr, hour, hours
        d, day, days
        w, wk, wks, week, weeks
        m, mo, month, months
        y, yr, yrs, year, years

    Returns
    -------
    (int, str)
        The multiplier to convert from the time basis to ms and the canonical
        version of the unit
    """
    abv = abbreviation.lower()
    if abv in ['s', 'sec', 'second', 'seconds']:
        return 1000, 's'
    if abv in ['min', 'minute', 'minutes']:
        return 60000, 'min'
    if abv in ['h', 'hr', 'hour', 'hours']:
        return 3.6e6, 'h'
    if abv in ['d', 'day', 'days']:
        return 8.64e7, 'day'
    if abv in ['w', 'wk', 'wks', 'week', 'weeks']:
        return 6.048e8, 'week'
    if abv in ['m', 'mo', 'month', 'months']:
        return 2.628e9, 'month'
    if abv in ['y', 'yr', 'yrs', 'year', 'years']:
        return 3.154e10, 'year'


def parse_str_time_to_ms(str_time):
    """
    Given a string time like 5min, 3hr, 2d, 7mo, etc, get the numeric and unit
    portions and calculate the number of milliseconds. Time units will be
    converted to the Seeq canonical versions, eg, 'sec' will yield 's'
    :param str_time: A string representing a time. Eg, 3min
    :return: tuple (numeric portion, string unit, milliseconds)
    For example '5min' returns (5, 'min', 300000)
    """
    i = -1
    while not str_time[:i].isdigit():
        i -= 1
    value = float(str_time[:i].strip())
    unit = str_time[i:].strip().lower()
    conversion = time_abbreviation_to_ms_multiplier(unit)
    return value, conversion[1], value * conversion[0]


def test_and_set(target, target_key, source, source_key, apply_func=None, default_value=None, retain_target=True):
    """
    If the source has source_key and it's not NaN, set it as the value for target[target_key]

    Optionally, apply a function to the value in source[source_key]. Must be a function that
    takes a single input, such as lambda x: str.lower( x) or lambda x: str.upper(x) or

    Optionally, set a default input for target[target_key] if source[source_key] is NaN. Note that
    the default is only applied if source_key is in source, but the source value is NaN

    Parameters
    ----------
    target : dict
        The dictionary that the value is to be inserted into
    target_key : str
        The key in target for the value
    source : dict
        The source dictionary
    source_key : str
        The key in the source dict to look for the value
    apply_func : function
        A function to apply to the source[source_key] value, if it's not NaN
    default_value : obj
        If source[source_key] is NaN, the value for target[target_key]. See "retain_default" for
        additional functionality
    retain_target : bool
        If true and source_key not in source, do not assign the default - retain the current target value
        If false and source_key not in source, overwrite the current target value with the default
    """
    if source_key in source:
        if pd.notna(source[source_key]):
            if apply_func is not None:
                target[target_key] = next(map(apply_func, [source[source_key]]))
            else:
                target[target_key] = source[source_key]
            return
        elif default_value is not None:
            target[target_key] = default_value
        return
    elif not retain_target:
        target[target_key] = default_value


def validate_argument_types(expected_types):
    for _value, _name, _types in expected_types:
        if _value is None:
            continue

        if not isinstance(_value, _types):
            raise TypeError("Argument '%s' should be type %s, but is type %s" %
                            (_name, _types, type(_value)))


def none_to_nan(v):
    return np.nan if v is None else v


def ensure_unicode(o):
    if isinstance(o, six.binary_type):
        return six.text_type(o, 'utf-8', errors='replace')
    else:
        return o


def timer_start():
    return datetime.datetime.now()


def timer_elapsed(timer):
    return datetime.datetime.now() - timer


def convert_to_timestamp(unix_timestamp_in_ns, tz):
    return convert_timestamp_timezone(none_to_nan(pd.Timestamp(unix_timestamp_in_ns)), tz)


def convert_timestamp_timezone(timestamp, tz):
    if pd.isna(timestamp):
        return timestamp

    timestamp = timestamp.tz_localize('UTC')
    return timestamp.tz_convert(tz) if tz else timestamp


def display_supports_html():
    # noinspection PyBroadException
    try:
        # noinspection PyUnresolvedReferences
        ipy_str = str(type(get_ipython()))
        if 'zmqshell' in ipy_str:
            return True
        if 'terminal' in ipy_str:
            return False

    except:
        return False


def ipython_clear_output(wait=False):
    clear_output(wait)


def ipython_display(*objs, include=None, exclude=None, metadata=None, transient=None, display_id=None, **kwargs):
    display(*objs, include=include, exclude=exclude, metadata=metadata, transient=transient,
            display_id=display_id, **kwargs)


def get_data_lab_datasource_input():
    datasource_input = DatasourceInputV1()
    datasource_input.name = DEFAULT_DATASOURCE_CLASS
    datasource_input.description = 'Signals, conditions and scalars from Seeq Data Lab.'
    datasource_input.datasource_class = DEFAULT_DATASOURCE_CLASS
    datasource_input.datasource_id = DEFAULT_DATASOURCE_ID
    datasource_input.stored_in_seeq = True
    datasource_input.additional_properties = [ScalarPropertyV1(name='Expect Duplicates During Indexing', value=True)]
    return datasource_input


def regex_from_query_fragment(query_fragment, contains=True):
    if query_fragment.startswith('/') and query_fragment.endswith('/'):
        regex = query_fragment[1:-1]
    else:
        regex = re.escape(query_fragment).replace(r'\?', '.').replace(r'\*', '.*')

        if contains and not regex.startswith('.*') and not regex.endswith('.*'):
            regex = '.*' + regex + '.*'

    return regex


def does_query_fragment_match(query_fragment, string, contains=True):
    regex = regex_from_query_fragment(query_fragment, contains=contains)
    return re.fullmatch(regex, string, re.IGNORECASE) is not None


def get_workbook_type(workbook_output_data):
    if not workbook_output_data:
        return 'Analysis'

    # noinspection PyBroadException
    try:
        data = json.loads(workbook_output_data)
    except BaseException:
        return 'Analysis'

    if 'isReportBinder' in data and data['isReportBinder']:
        return 'Topic'
    else:
        return 'Analysis'


class Status:
    RUNNING = 0
    SUCCESS = 1
    FAILURE = 2
    CANCELED = 3

    def __init__(self, quiet=False):
        self.quiet = quiet
        self.df = pd.DataFrame()
        self.timer = timer_start()
        self.message = None
        self.current_df_index = None

    def metrics(self, d):
        self.df = pd.DataFrame(d).transpose()

    def put(self, column, value):
        self.df.at[self.current_df_index, column] = value

    def get(self, column):
        return self.df.at[self.current_df_index, column]

    def update(self, new_message, status):
        if self.quiet:
            return

        if not display_supports_html():
            if new_message != self.message:
                text = re.sub(r'</?[^>]+>', '', new_message)
                display(text)
                self.message = new_message
            return

        ipython_clear_output(wait=True)

        display_df = self.df
        if status == Status.RUNNING and len(self.df) > 20 and 'Result' in self.df.columns:
            display_df = self.df[~self.df['Result'].isin(['Queued', 'Success'])]

        if status == Status.RUNNING:
            color = '#EEEEFF'
        elif status == Status.SUCCESS:
            color = '#EEFFEE'
        else:
            color = '#FFEEEE'

        style = 'background-color: %s;' % color
        html = '<div style="%s">%s</div>' % (
            style + 'text-align: left;', Status._massage_cell(new_message))

        if len(display_df) > 0:
            html += '<table>'
            html += '<tr><td style="%s"></td>' % style

            for col in display_df.columns:
                html += '<td style="%s">%s</td>' % (style, Status._massage_cell(col))

            html += '</tr>'

            for index, row in display_df.iterrows():
                html += '<tr style="%s">' % style
                html += '<td>%s</td>' % index
                for cell in row:
                    if isinstance(cell, datetime.timedelta):
                        hours, remainder = divmod(cell.seconds, 3600)
                        minutes, seconds = divmod(remainder, 60)
                        html += '<td>{:02}:{:02}:{:02}.{:02}</td>'.format(int(hours), int(minutes), int(seconds),
                                                                          int((cell.microseconds + 5000) / 10000))
                    else:
                        html += '<td>%s</td>' % Status._massage_cell(cell, links=True)
                html += '</tr>'

            html += '</table>'

        display(HTML(html))

    @staticmethod
    def _massage_cell(cell, links=False):
        cell = str(cell)
        cell = cell.replace('\n', '<br>')
        if links:
            cell = re.sub(r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)',
                          r'<a target="_blank" href="\1">link</a>',
                          cell)

        return cell

    def get_timer(self):
        return timer_elapsed(self.timer)

    def reset_timer(self):
        self.timer = timer_start()

    def exception(self, e):
        if isinstance(e, KeyboardInterrupt):
            self.df['Result'] = 'Canceled'
            status_message = 'Canceled'
            status_code = Status.CANCELED
        else:
            status_message = 'Error encountered, scroll down to view'
            status_code = Status.FAILURE

        self.update(status_message, status_code)

    @staticmethod
    def validate(status, quiet=False):
        """
        :param status: An already-instantiated Status object
        :type status: Status
        :param quiet: If True, suppresses output to Jupyter/console
        :type quiet: bool
        :rtype Status
        :return: The already-instantiated Status object passed in, or a newly-instantiated Status object
        """
        if status is None:
            status = Status(quiet=quiet)

        if not isinstance(status, Status):
            raise TypeError(f'Argument status must be of type Status, not {type(status)}')

        return status
