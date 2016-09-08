"""flutter Models."""

from django.db import models


class Flutt(models.Model):
    """A flutt class model that stores text and a timestamp."""
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Flutt(text={!r}, timestamp={!r})'.format(self.text, self.timestamp)