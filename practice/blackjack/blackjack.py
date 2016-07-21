"""Runs a game of blackjack in the terminal."""

from card import Card
from hand import Hand

EXAMPLE_CARD = Card('2', '♡')
EXAMPLE_HAND = Hand([Card('Q', '♠'), Card('J', '♣')])


def add_card_to_hand(hand, card):
    """Adds a card to an existing hand.

    >>> add_card_to_hand(EXAMPLE_HAND, EXAMPLE_CARD)
    Hand([Card('Q', '♠'), Card('J', '♣'), Card('2', '♡')])
    """
    cards_for_hand = hand.cards + [card]
    new_hand = Hand(cards_for_hand)
    return new_hand

def score_hand(hand):
    """Calculates the score for a given hand

    """


def main():
    """Main function."""
    new_hand = add_card_to_hand(EXAMPLE_HAND, EXAMPLE_CARD)


if __name__ == '__main__':
    main()
