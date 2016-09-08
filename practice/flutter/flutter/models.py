"""flutter Models."""

from django.db import models


class Flutt(models.Model):
    """A flutt class model that stores text and a timestamp.
    """
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a string that represnts a shorthand description of the flutt.
        >>> carol = Flutt(text='the moumwraiths outgrabe')
        >>> carol.__str__()
        'the moumwraiths outgrabe'
        """
        return self.text

    def __repr__(self):
        """Returns a string that represnts a shorthand description of the flutt.
        >>> billy = Flutt(text='dancing with myself, oh-oh', timestamp=3)
        >>> billy.__repr__()
        'Flutt(text=dancing with myself, timestamp=3)
        """
        return 'Flutt(text={!r}, timestamp={!r})'.format(self.text, self.timestamp)