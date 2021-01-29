import datetime
import time


def from_datetime_to_unix(dt: datetime.datetime) -> int:
    unixtime = time.mktime(dt.timetuple())
    return int(unixtime)


def from_datetime_to_unix_ms(dt: datetime.datetime) -> int:
    unixtime = time.mktime(dt.timetuple()) * 1000
    return int(unixtime)


def utc_now():
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
