"""Jokes models."""


class Joke:
    """
    Value type that represents a submitted joke. It has a setup, and a punchline.
    """
    def __init__(self, setup, punchline):
        """ Initiates a Joke

        >>> a = Joke('words', 'wordswords')
        >>> a
        'Joke(words, wordswords)'
        """

        self.setup = setup
        self.punchline = punchline

    def __eq__(self, other):
        """ Determines if one joke is the same as another

        >>> a = Joke('words', 'wordswords')
        >>> b = Joke('Old Man McGucket', 'wordswords')
        >>> a == b
        'False'

        >>> a = Joke('words', 'wordswords')
        >>> b = Joke('words', 'wordswords')
        >>> a == b
        'True'
        """
        return (
            self.setup == other.setup and
            self.punchline == other.punchline
        )

    def __repr__(self):
        """ Represents a Joke

         >>> a = Joke('words', 'wordswords')
         >>> a
         'Joke(words, wordswords)'
         """
        return 'Joke({!r}, {!r})'.format(self.setup, self.punchline)

_jokes = []


def _create_joke(setup, punchline):
    """
    Takes in an argument of a setup and a punchline, and creates a new Joke class object with it.

    >>> _create_joke('setup','punchline')
    'Joke(setup,punchline)'

    """
    if setup == '' or punchline == '':
        raise KeyError
    else:
        return Joke(setup, punchline)

def _append_joke(existing_jokes, new_joke):
    """
    Takes in arguments of a list of jokes and a joke to add, it then adds that joke to the list.

    >>> fake_list_of_jokes = []
    >>> newer_joke = 'Jokeyjokerson(lol,cupcake)'
    >>> _append_joke(fake_list_of_jokes, newer_joke)
    ['Jokeyjokerson(lol,cupcake)']
    """
    return existing_jokes + [new_joke]


def add_joke(setup, punchline):
    """
    Takes in an argument of a setup and a punchline, and creates a new Joke class object, which is then added to the
    global array of jokes.
    """
    new_joke = _create_joke(setup, punchline)
    _jokes = _append_joke(_jokes, new_joke)
    return new_joke


add_joke(
    'What is the difference between a duck?',
    'One leg is both the same'
    )
add_joke(
    'What is big and red and eats rocks?',
    'A big red rock eater'
    )
add_joke(
    'What is big and blue and eats rocks?',
    'A big blue rock eater'
    )
add_joke(
    'What is big and green and eats rocks?',
    'There is no such thing as a big green rock eater, silly'
    )