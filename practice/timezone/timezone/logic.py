"""Runs the logic for the timezone Django app."""

import arrow
import re
import tzwhere
from tzwhere import tzwhere
tz = tzwhere.tzwhere()


def get_time_now():
    """Returns the ISO 8601 string format version of the current time for UTC time.
    """
    time = arrow.now()
    return time.isoformat()


def get_time_now_for_timezone(timezone):
    """Takes in the timezone as an agurment and returns the ISO 8601 string
    format version of the current time for the given timezone.

    >>> a = get_time_now('US/Pacific')
    >>> re.search('-07:00', a)
    <_sre.SRE_Match object; span=(26, 32), match='-07:00'>
    """
    time = arrow.now(timezone)
    return time.isoformat()



def get_timezone(lat, lng):
    """Takes in the arguments of latitude and longitude, and returns the
    timezone as a simple string.


    >>> get_timezone(12, 12)
    'Africa/Lagos'
    """
    timezone = tz.tzNameAt(lat, lng)
    if timezone == None:
        raise ValueError('Timezone not found')
    else:
        return timezone


def get_timezone_conversion(timestamp, to_timezone):
    """Takes in a timestamp and a timezone as arguments, and returns a new timestamp that represents the same time as
    the given timestamp but for the given timezone.
    """
    return timestamp.to(to_timezone)
