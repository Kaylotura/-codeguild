"""Module containing the Deck class"""


from card import Card
from random import shuffle


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


STANDARD_DECK = Deck([
    Card('A', 'C'),
    Card('2', 'C'),
    Card('3', 'C'),
    Card('4', 'C'),
    Card('5', 'C'),
    Card('6', 'C'),
    Card('7', 'C'),
    Card('8', 'C'),
    Card('9', 'C'),
    Card('10', 'C'),
    Card('J', 'C'),
    Card('Q', 'C'),
    Card('K', 'C'),
    Card('A', 'D'),
    Card('2', 'D'),
    Card('3', 'D'),
    Card('4', 'D'),
    Card('5', 'D'),
    Card('6', 'D'),
    Card('7', 'D'),
    Card('8', 'D'),
    Card('9', 'D'),
    Card('10', 'D'),
    Card('J', 'D'),
    Card('Q', 'D'),
    Card('K', 'D'),
    Card('A', 'H'),
    Card('2', 'H'),
    Card('3', 'H'),
    Card('4', 'H'),
    Card('5', 'H'),
    Card('6', 'H'),
    Card('7', 'H'),
    Card('8', 'H'),
    Card('9', 'H'),
    Card('10', 'H'),
    Card('J', 'H'),
    Card('Q', 'H'),
    Card('K', 'H'),
    Card('A', 'S'),
    Card('2', 'S'),
    Card('3', 'S'),
    Card('4', 'S'),
    Card('5', 'S'),
    Card('6', 'S'),
    Card('7', 'S'),
    Card('8', 'S'),
    Card('9', 'S'),
    Card('10', 'S'),
    Card('J', 'S'),
    Card('Q', 'S'),
    Card('K', 'S')
    ])
EXAMPLE_DECK = Deck([Card('A', 'C'), Card('2', 'C'), Card('3', 'C')])


def get_shuffled_deck(deck):
    """Shuffles a deck of cards

    """
    shuffled_cards = shuffle(deck.cards)
    shuffled_deck = Deck(shuffled_cards)
    return shuffled_deck


def draw_card_show_card(deck):
    """Shows the card on the top of a deck

    >>> draw_card_show_card(EXAMPLE_DECK)
    Card('A', 'C')
    >>> draw_card_show_card(Deck([Card('A', 'C')]))
    You are drawing the last card in this deck.
    Card('A', 'C')
   """
    if len(deck.cards) > 1:
        return deck.cards[0]
    elif len(deck.cards) == 1:
        print('You are drawing the last card in this deck.')
        return deck.cards[0]


def draw_card_remove_card(deck):
    """Returns a new deck with the top card removed.

    >>> draw_card_remove_card(EXAMPLE_DECK)
    Deck([Card('2', 'C'), Card('3', 'C')])
    """

    cards_less_top_card = deck.cards[1:]
    return Deck(cards_less_top_card)


def check_deck_for_empty(deck):
    """Returns true if deck is empty.

    >>> check_deck_for_empty(EXAMPLE_DECK)
    False
    >>> check_deck_for_empty(Deck([]))
    True
    """
    return len(deck.cards) == 0