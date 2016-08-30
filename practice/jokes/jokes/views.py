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
    return render(request, 'jokes/joke_form.html')


def acknowledge_joke_form_submit(request):
    """ Attempts to take in post data from the joke form to create a new joke. It informs the user if this process is
    successful or not, and displays the joke form acknowledgement page.
    """
    try:
        setup = request.POST['setup']
        punchline = request.POST['punchline']
    except KeyError:
        return HttpResponse('Lol, you forgot your own joke!', status=400)
    if setup == '' or punchline == '':
        return render(request, 'jokes/joke_form_fail.html')
    else:
        models.add_joke(setup, punchline)
        template_arguments = {
            'setup': setup,
            'punchline': punchline
        }
        return render(request, 'jokes/joke_form_submit.html', template_arguments)
