"""flutter Logic."""

from . import models


def create_and_save_new_flutt(text):
    """creates and saves a new flutt."""
    new_flutt = models.Flutt(text=text)
    new_flutt.save()
    return new_flutt
