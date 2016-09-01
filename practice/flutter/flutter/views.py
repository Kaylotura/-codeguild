"""flutter Views."""

from . import models
from django.shortcuts import render


def render_index(request):
    """ Collects the 10 latest Flutts and sends them to the the index page."""
    flutts_by_time = models.Flutt.objects.order_by('timestamp').reverse()

    most_recent_flutts = flutts_by_time[:10]
    template_arguments = {
            'flutts': most_recent_flutts
        }
    return render(request, 'flutter/index.html', template_arguments)


# def render_post_form(request):
#     return render(post_form.html)
#     pass

