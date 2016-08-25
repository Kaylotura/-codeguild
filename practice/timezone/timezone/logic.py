"""Runs the logic for the timezone Django app."""

from . import models
import arrow


def get_time_right_now():
    """ Returns the ISO 8601 string format version of the time this function was called."""
    time = arrow.now()
    return time.isoformat()
