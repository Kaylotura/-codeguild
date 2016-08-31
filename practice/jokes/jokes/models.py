"""Jokes models."""


class Joke:
    """
    Value type that represents a submitted joke. It has a setup, and a punchline.
    """

    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline

    def __eq__(self, other):
        return (
            self.setup == other.setup and
            self.punchline == other.punchline
        )

    def __repr__(self):
        return 'Joke({!r}, {!r})'.format(self.setup, self.punchline)

jokes = []

def add_joke(setup, punchline):
    """
    Takes in an argument of a setup and a punchline, and creates a new Joke class object, which is then added to the
    global array of jokes.
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