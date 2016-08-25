"""Generates views for the timezone Django app."""

from . import logic
from . import models
from django.http import HttpResponse


def show_time_now(response):
    """Renders the HTML for get time right now."""
    now = logic.get_time_now('')
    return HttpResponse(now)


def show_timezone(response, lat, lng):
    """Renders the HTML for get timezeon"""
    try:
        timezone = logic.get_timezone(float(lat), float(lng))
    except ValueError:
        return HttpResponse('Timezone not found', status=404)
    return HttpResponse(timezone)


def show_time_for_timezone(response, lat, lng):
    """Finds the timezone, then renders the HTML for the current time of the
    given timezone.
    """
    try:
        timezone = logic.get_timezone(float(lat), float(lng))
    except ValueError:
        return HttpResponse('Bad request, timezone not found', status=400)
    now = logic.get_time_now(timezone)
    return HttpResponse(now)


def show_timezone_conversion(response, time, lat, lng):
    """Takes in a complete timestamp, a lattitude, and a longitude as arguments,
    and returns the time in the timezone at at a given latitude and longitude
    when it is the same moment as the given time at the timezone of the
    timestamp'
    """
    try:
        timezone = logic.get_timezone(float(lat), float(lng))
    except ValueError:
        return HttpResponse('Bad request, timezone not found', status=400)
    converted_time = logic.get_timezone_conversion(time, timezone)
    return HttpResponse(converted_time)
