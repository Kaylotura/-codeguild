"""flutter Logic."""

from . import models


def create_and_save_new_flutt(text):
    """Creates and saves a new flutt.

    >>> stark = create_and_save_new_flutt('winter is coming')
    >>> stark.text
    'winter is coming'
    """
    new_flutt = models.Flutt(text=text)
    new_flutt.save()
    return new_flutt
