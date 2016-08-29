"""jokes Models."""

class Joke():
    """
    Value type that represents a submitted joke.
    It has a setup, and a punchline.
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

duck_joke = Joke('What is the difference between a duck?', 'One leg is both the same.')
rock_eater_joke_1 = Joke('What is big and red and eats rocks?', 'A big red rock eater.')
rock_eater_joke_2 = Joke('What is big and blue and eats rocks?', 'A big blue rock eater.')
rock_eater_joke_3 = Joke('What is big and green and eats rocks?', 'There is no such thing as a big green rock eater, silly.')


jokes = [duck_joke, rock_eater_joke_1, rock_eater_joke_2, rock_eater_joke_3]