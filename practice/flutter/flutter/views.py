"""flutter Views."""

from . import logic
from . import models
from django.shortcuts import render


def render_index(request):
    """Collects the 10 latest Flutts and sends them to the the index page."""
    flutts_by_time = models.Flutt.objects.order_by('timestamp').reverse()

    most_recent_flutts = flutts_by_time[:10]
    template_arguments = {
            'flutts': most_recent_flutts
        }
    return render(request, 'flutter/index.html', template_arguments)


def render_post_form(request):
    """Renders the post form page."""
    return render(request, 'post_form.html')


def render__post_submit(request):
    """Grabs the text from the post_form form and passes it through a create and save function to add it to the Flutt
    model, then renders the post sumbit page.
    """
    flutt_text = request.POST['name']
    new_post = logic.create_and_save_new_flutt(flutt_text)
    template_arguements = {
        'new_post': new_post
    }
    return render(request, 'post_form.html', template_arguements)
