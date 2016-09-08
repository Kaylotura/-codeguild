"""flutter Logic."""

from . import models


def create_and_save_new_flutt(text, timestamp=''):
    """Takes in text as an argument and creates and saves a new flutt. Generally the timestamp entry will be left empty,
    as that the Flutt model automatically genertes its own timestamp, but it has been included as an optional argument
    for the purposes of testing.

    >>> stark = create_and_save_new_flutt('winter is coming', 3)
    >>> stark
    'Flutt(text=winter is coming, timestamp=3)'
    """
    if timestamp == '':
        new_flutt = models.Flutt(text=text)
    else:
        new_flutt = models.Flutt(text=text, timestamp=timestamp)
    new_flutt.save()
    return new_flutt


def get_flutts_by_time(flutts):
    """Takes in a series of flutt objects, and orders them by time with the most recent first.

    >>> a = models.Flutt(text='a', timestamp=1)
    >>> a.save()
    >>> b = models.Flutt(text='b', timestamp=2)
    >>> b.save()
    >>> c = models.Flutt(text='c', timestamp=3)
    >>> c.save()
    >>> get_flutts_by_time([a, b, c])
    [Flutt(text=c, timestamp=3), Flutt(text=b, timestamp=2), Flutt(text=a, timestamp=1)]
    """
    return flutts.order_by('timestamp').reverse()


def get_first_ten(any_list):
    """Takes in a list as an arguement and returns the first 10 items in a new list

    >>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
    >>> get_first_ten(a)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    new_list = any_list[:10]
    return new_list


def get_most_recent_flutts(flutts):
    """Takes in a list of flutts and returns a list of the most recent flutts with the newest first, and so on. If there
    are more than 10, the list only returns the 10 most recent flutts.

    >>> a = models.Flutt(text='a', timestamp=1)
    >>> a.save()
    >>> b = models.Flutt(text='b', timestamp=2)
    >>> b.save()
    >>> c = models.Flutt(text='c', timestamp=3)
    >>> c.save()
    >>> d = models.Flutt(text='d', timestamp=4)
    >>> d.save()
    >>> e = models.Flutt(text='e', timestamp=5)
    >>> e.save()
    >>> f = models.Flutt(text='f', timestamp=6)
    >>> f.save()
    >>> g = models.Flutt(text='g', timestamp=7)
    >>> g.save()
    >>> h = models.Flutt(text='h', timestamp=8)
    >>> h.save()
    >>> i = models.Flutt(text='i', timestamp=9)
    >>> i.save()
    >>> j = models.Flutt(text='j', timestamp=10)
    >>> j.save()
    >>> k = models.Flutt(text='k', timestamp=11)
    >>> k.save()
    >>> test_flutts = [a, b, c, d, e, f, g, h, i, j, k]
    >>> recent_test_flutts = get_most_recent_flutts(test_flutts)
    >>> [flutt.text for flutt in test_flutts]
    [k, j, i, h, g, f, e, d, c, b]

    """
    flutts_by_time = get_flutts_by_time(flutts)
    if len(flutts_by_time) > 10:
        return get_first_ten(flutts_by_time)
    elif len(flutts_by_time) == 0:
        return ['']
    else:
        return flutts_by_time


def search_flutts(query_text):
    """ Uses the django model method of filter to find flutts that contain the query text.

    >>> a = models.Flutt(text='You grab a line, I grab a pole, honey!')
    >>> a.save()
    >>> b = models.Flutt(text='We all go down to that crawdad hole, baby!')
    >>> b.save()
    >>> c = models.Flutt(text='There are no crawdad in that lake, honey!')
    >>> c.save()
    >>> crawdad_list = search_flutts('crawdad')
    >>> [flutt.text for flutt in crawdad_list]
    ['We all go down to that crawdad hole, baby!', 'There are no crawdad in that lake, honey!']
    """
    return models.Flutt.objects.filter(text__icontains=query_text)
