"""
GoodWan client library: helpers
"""
import datetime


DATETIME_FORMAT_OLD = "%Y-%m-%dT%H:%M:%S%z"
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"
old_format = False


def tz_add_colon(s):
    return s[:-2] + ":" + s[-2:]


def tz_rm_colon(s):
    if s[-3] == ":":
        s = s[:-3] + s[-2:]
    return s


def str_to_datetime_old_format(date_string, timezone):
    """
    Convert string to datetime
    :param date_string: date string
    :type date_string: str
    :param timezone: pytz timezone
    :type timezone: pytz.timezone
    :return: datetime
    :rtype: datetime.datetime
    """
    date_string = tz_rm_colon(date_string)
    result = datetime.datetime.strptime(date_string, DATETIME_FORMAT_OLD)
    if result.tzinfo is None:
        result = timezone.localize(result, is_dst=None)
    else:
        result = result.astimezone(timezone)

    return result


def datetime_to_str_old_format(datetime_value, timezone):
    """
    Convert datetime to string
    :param datetime_value: datetime value
    :type datetime_value: datetime.datetime
    :param timezone: pytz timezone
    :type timezone: pytz.timezone
    :return: datetime string
    :rtype: str
    """
    if datetime_value.tzinfo is None:
        datetime_value = timezone.localize(datetime_value)
    return tz_add_colon(datetime_value.strftime(DATETIME_FORMAT_OLD))


def tz_truncate_microseconds(s: str) -> str:
    """
    Make microseconds in time format a 3-chars string from 5 chars
    :param s: date string
    :type s: str
    :return: new string
    :rtype: str
    """
    if s[-12] == ".":
        s = s[:-8] + s[-6:]
    return s


def tz_grow_microseconds(s: str) -> str:
    """
    Make microseconds in time format a 3-chars string
    :param s: date string
    :type s: str
    :return: new string
    :rtype: str
    """
    if s[-10] == ".":
        s = s[:-6] + "00" + s[-6:]
    elif s[-9] == ":":
        s = s[:-6] + ".00000" + s[-6:]
    return s


def str_to_datetime(date_string, timezone):
    """
    Convert string to datetime
    :param date_string: date string
    :type date_string: str
    :param timezone: pytz timezone
    :type timezone: pytz.timezone
    :return: datetime
    :rtype: datetime.datetime
    """
    if old_format:
        return str_to_datetime_old_format(date_string, timezone)
    date_string = tz_grow_microseconds(date_string)
    result = datetime.datetime.strptime(date_string, DATETIME_FORMAT)
    if result.tzinfo is None:
        result = timezone.localize(result, is_dst=None)
    else:
        result = result.astimezone(timezone)

    return result


def datetime_to_str(datetime_value, timezone):
    """
    Convert datetime to string
    :param datetime_value: datetime value
    :type datetime_value: datetime.datetime
    :param timezone: pytz timezone
    :type timezone: pytz.timezone
    :return: datetime string
    :rtype: str
    """
    if old_format:
        return datetime_to_str_old_format(datetime_value, timezone)
    if datetime_value.tzinfo is None:
        datetime_value = timezone.localize(datetime_value)
    return tz_truncate_microseconds(datetime_value.strftime(DATETIME_FORMAT))
