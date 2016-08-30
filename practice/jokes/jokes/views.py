"""jokes Views."""
from django.http import HttpResponse
from django.shortcuts import render
from . import models


def render_jokes(request):
    """Renders a list of all the jokes."""
    template_arguments = {
        'jokes': models.jokes,
    }
    return render(request, 'jokes/index.html', template_arguments)


def render_joke_form(request):
    """Renders the joke form page."""
    return render (request, 'jokes/joke_form.html')

def acknowledge_joke_form_submit(request):
    """Acknowledges that the joke form has been accepted or informs the user of an error after submit button is pressed.
    """
    if x:
        template_arguments = {
            'message': 'Lmao, we gatta add that one to the collection'
        }
    else:
        template_arguments = {
            'message': 'Oops. I guess we missed that one, try again?'
        }
    return render (request, 'jokes/joke_form_submit.html', template_arguments)