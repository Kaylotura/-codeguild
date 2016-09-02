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
    return render(request, 'flutter/post_form.html')


def render__post_submit(request):
    """Grabs the text from the post_form form and passes it through a create and save function to add it to the Flutt
    model, then renders the post sumbit page.
    """
    flutt_text = request.POST['text']
    new_post = logic.create_and_save_new_flutt(flutt_text)
    template_arguements = {
        'new_post': new_post
    }
    return render(request, 'flutter/post_submit.html', template_arguements)

def render_query(request):
    """Searches the Flutt model for flutts with matching text, and returns up to 10 of the most recent fluts with that
    text."""
    query_text = request.GET.get('query', '')
    query_flutts = models.Flutt.objects.filter(text__icontains=query_text)
    if len(query_flutts) > 10:
        query_flutts_by_time = query_flutts.order_by('timestamp').reverse()
        most_recent_flutts = query_flutts_by_time[:10]
        message = 'Here are the ten most recent songs by that tune.'
    elif len(query_flutts) == 0:
        message = 'Sorry I haven\'nt heard any songs like that.'
        most_recent_flutts = ''
    else:
        most_recent_flutts = query_flutts.order_by('timestamp').reverse()
        message = 'These are all the songs I\'ve heard like that.'
    template_arguments = {
            'flutts': most_recent_flutts,
            'message': message
        }
    return render(request, 'flutter/query.html', template_arguments)
