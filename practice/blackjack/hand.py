"""Module containing the Hand class"""
from card import Card

class Hand:
    """A class for representing a Hand of cards"""

    def __init__(self, cards):
        self.cards = cards

    def __eq__(self, other):
        return (
            self.cards == other.cards
            )

    def __repr__(self):
        return 'Hand({!r})'.format(
            self.cards
        )