"""flutter Views."""

from . import logic
from . import models
from django.shortcuts import render


def flutts_by_time(flutts):
    """Takes in a series of flutt objects, and orders them by time with the most recent first."""
    return flutts.order_by('timestamp').reverse()


def render_index(request):
    """Collects the ten latest Flutts and render them with the the index page."""
    most_recent_flutts = flutts_by_time(models.Flutt.objects)[:10]
    template_arguments = {
            'flutts': most_recent_flutts
        }
    return render(request, 'flutter/index.html', template_arguments)


def render_post_form(request):
    """Renders the post form page."""
    return render(request, 'flutter/post_form.html')


def render__post_submit(request):
    """Grabs the text from the form on the post_form page and passes it through a create and save function to add it to
    the Flutt class-model, then renders the post submit page.
    """
    flutt_text = request.POST['text']
    new_post = logic.create_and_save_new_flutt(flutt_text)
    template_arguments = {
        'new_post': new_post
    }
    return render(request, 'flutter/post_submit.html', template_arguments)


def render_query(request):
    """Using url query parameters, this function grabs the queery text from the url, and uses that to search all the
    objects in the Flutt model-class for flutts with matching text, and returns up to 10 of the most recent flutts with
    that text.
    This function then renders the query page, with a message based the number of flutts that matched the query text.
    """
    query_text = request.GET.get('query', '')
    query_flutts = models.Flutt.objects.filter(text__icontains=query_text)
    if len(query_flutts) > 10:
        most_recent_flutts = flutts_by_time(query_flutts)[:10]
        message = 'Here are the ten most recent songs by that tune.'
    elif len(query_flutts) == 0:
        most_recent_flutts = ''
        message = 'Sorry, I have\'nt heard any songs like that.'
    else:
        most_recent_flutts = flutts_by_time(query_flutts)
        message = 'These are all the songs I\'ve heard like that.'
    template_arguments = {
            'flutts': most_recent_flutts,
            'message': message
        }
    return render(request, 'flutter/query.html', template_arguments)
