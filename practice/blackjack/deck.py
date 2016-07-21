"""Module containing the Deck class"""
from card import Card

class Deck:
    """A class for representing a Deck of cards"""

    def __init__(self, cards):
        self.cards = cards

    def __eq__(self, other):
        return (
            self.cards == other.cards
            )

    def __repr__(self):
        return 'Deck({!r})'.format(
            self.cards
        )