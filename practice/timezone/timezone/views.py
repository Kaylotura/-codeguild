"""Generates views for the timezone Django app."""

from . import logic
from . import models

from django.http import HttpResponse

def get_now(response):
    """Renders the HTML for get time right now."""
    now =  logic.get_time_right_now()
    return HttpResponse(now)

def get_timezone(lattitude, longitude, response):
    """Renders the HTML for get timezeon"""
    timezone = logic.find_time_zone(lattitude, longitude)
    return HttpResonse(timezone)
