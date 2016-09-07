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

jokes = []


def add_joke(setup, punchline):
    """
    Takes in an argument of a setup and a punchline, and creates a new Joke class object, which is then added to the
    global array of jokes.

    >>> add_joke('words', 'wordswords')
    'Joke(words, wordswords)'
    """
    new_joke = Joke(setup, punchline)
    jokes.append(new_joke)


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