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


ACES = ([Card('A', 'C'), Card('A', 'D')], ([Card('A', 'H'), Card('A', 'C')]))
EXAMPLE_CARD = Card('2', 'H')
EXAMPLE_HAND = Hand([Card('Q', 'S'), Card('J', 'C')])


def add_card_to_hand(hand, card):
    """Adds a card to an existing hand.

    >>> add_card_to_hand(EXAMPLE_HAND, EXAMPLE_CARD)
    Hand([Card('Q', 'S'), Card('J', 'C'), Card('2', 'H')])
    """
    cards_for_hand = hand.cards + [card]
    new_hand = Hand(cards_for_hand)
    return new_hand


def score_card(card):
    """Calculates score for a single card.

    >>> score_card(EXAMPLE_CARD)
    2
    >>> score_card(Card('K', 'S'))
    10
    >>> score_card(Card('A', 'C'))
    11
    """
    if card.rank == 'A':
        card_score = 11
    elif card.rank == 'J' or card.rank == 'Q' or card.rank == 'K':
        card_score = 10
    else:
        card_score = int(card.rank)
    return card_score


def score_hand(hand):
    """Calculates the score for a given hand.

    >>> score_hand(EXAMPLE_HAND)
    20
    >>> score_hand(Hand([Card('Q', 'S'), Card('J', 'C'), Card('5', 'C')]))
    25
    >>> score_hand(Hand([Card('Q', 'S'), Card('A', 'C'), Card('5', 'C')]))
    16
    >>> score_hand(Hand([Card('A', 'S'), Card('A', 'C'), Card('5', 'C')]))
    17
    >>> score_hand(Hand([Card('A', 'S'), Card('A', 'C'), Card('A', 'H')]))
    13
    >>> score_hand(Hand([Card('Q', 'S'), Card('A', 'S'), Card('A', 'C'), Card('A', 'H')]))
    13
    >>> score_hand(Hand([Card('Q', 'S'), Card('A', 'S'), Card('A', 'C'), Card('A', 'H'), Card('A', 'D')]))
    14

    """
    scores = [score_card(card) for card in hand.cards]
    temp_score = sum(scores)
    if temp_score > 21 and (
        Card('A', 'C') in hand.cards or
        Card('A', 'D') in hand.cards or
        Card('A', 'H') in hand.cards or
        Card('A', 'S') in hand.cards
    ):
        adjust_score = temp_score - 10
        if adjust_score > 21 and (
            Card('A', 'C') in hand.cards and Card('A', 'D') in hand.cards or
            Card('A', 'C') in hand.cards and Card('A', 'H') in hand.cards or
            Card('A', 'C') in hand.cards and Card('A', 'S') in hand.cards or
            Card('A', 'D') in hand.cards and Card('A', 'H') in hand.cards

        ):
            rejust_score = adjust_score -10
            if rejust_score > 21 and (
                Card('A', 'C') in hand.cards and Card('A', 'D') in hand.cards and Card('A', 'H') in hand.cards or
                Card('A', 'C') in hand.cards and Card('A', 'D') in hand.cards and Card('A', 'S') in hand.cards or
                Card('A', 'C') in hand.cards and Card('A', 'H') in hand.cards and Card('A', 'S') in hand.cards or
                Card('A', 'D') in hand.cards and Card('A', 'H') in hand.cards and Card('A', 'S') in hand.cards
            ):
                trijust_score = rejust_score - 10
                if trijust_score > 21 and (
                    Card('A', 'C') in hand.cards and
                    Card('A', 'D') in hand.cards and
                    Card('A', 'H') in hand.cards and
                    Card('A', 'S') in hand.cards
                ):
                    score = trijust_score - 10
                else:
                    score = trijust_score
            else:
                score = rejust_score
        else:
            score = adjust_score
    else:
        score = temp_score
    return score


def check_for_bust(hand):
    """Returns if hand's score is over 21.

    >>> check_for_bust(EXAMPLE_HAND)
    False
    >>> check_for_bust(Hand([Card('Q', 'S'), Card('J', 'C'), Card('2', 'H')]))
    True
    """
    return score_hand(hand) > 21


def convert_string_to_card(string):
    """Takes in a string representing a card and returns a Card Object

    >>> convert_string_to_card('KD')
    Card('K', 'D')
    """
    return Card(string[0], string[1])


def get_hand_imput():
    """Prints prompt and takes input to be changed into a hand"""
#   Not sure how to doctest for input
    print('Clubs: C, Diamonds: D, Hearts: H, Spades: S, Jack: J, King: K, Queen: Q')
    hand_string = input('Please enter the cards in your hand separated by a space: ')
    return hand_string


def string_to_hand(hand_string):
    """Takes in a string to create a hand of cards from.

    >>> string_to_hand('KD 2H')
    Hand([Card('K', 'D'), Card('2', 'H')])
    """
    cards_as_strings = hand_string.split(' ')
    cards = [convert_string_to_card(string) for string in cards_as_strings]
    new_hand = Hand(cards)
    return new_hand
