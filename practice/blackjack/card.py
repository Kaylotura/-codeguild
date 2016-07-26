"""Module containing the Card class"""


class Card:
    """A class for representing an individual card"""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        return (
            self.rank == other.rank and
            self.suit == other.suit
        )

    def __repr__(self):
        return 'Card({!r}, {!r})'.format(
            self.rank,
            self.suit,
        )