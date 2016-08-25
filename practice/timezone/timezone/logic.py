"""Runs the logic for the timezone Django app."""

import arrow
import re
import tzwhere
from tzwhere import tzwhere
tz = tzwhere.tzwhere()


def get_time_now(timezone):
    """Takes in the timezone as an agurment and returns the ISO 8601 string
    format version of the current time for the given timezone.

    If '' is passed
    in as the timezone, the time is returned for UTC time.

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


    >>> get_timezone_conversion('2016-08-25T10:40:15-07:00', 'America/Chicago')
    <Arrow [2016-08-25T12:40:15-05:00]>
    """
    working_time = arrow.get(timestamp)
    return working_time.to(to_timezone)
