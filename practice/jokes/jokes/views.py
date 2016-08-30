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
    """ Attempts to take in post data from the joke form to create a new joke. It informs the user if this process is
    successful or not, and displays the joke form acknowledgement page.
    """
    try:
        setup = request.POST['setup']
        punchline = request.POST['author']
    except KeyError:
        return HttpResponse('All setup and no punchline? A travesty does not a joke make.', status=400)
    template_arguments = {
        'message': 'Lmao, we gatta add that one to the collection',
        'retry': 'Got any more?'
    }
    try:
        comment = models.add_joke(setup, punchline)
    except ValueError:
        template_arguments = {
            'message': 'Oops. I guess we missed that one.',
            'retry': 'Wanna run that by me again?'
        }
    return render (request, 'jokes/joke_form_submit.html', template_arguments)