"""jokes Views."""
from django.http import HttpResponse
from django.shortcuts import render
from . import models


def render_jokes(request):
    """Renders a list of all the jokes."""
    template_arguments = {
        'jokes': models.jokes,
    }
    return render(request, 'jokes/Index.html', template_arguments)

