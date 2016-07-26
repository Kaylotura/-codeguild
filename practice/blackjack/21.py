"""
Gives basic Blackjack advice based on user input.
July.11.2016: Cleaned up code, added elif/else statements casting strings to ints, and added splitting advice for fun.
"""

# 1. Setup

card_1 = input('Please enter the first card ')
card_2 = input('Please enter the second card ')

# 2. transform

if card_1 == 'A':
    card_1_value = 11
elif card_1 == 'J' or card_1 == 'Q' or card_1 == 'K':
    card_1_value = 10
else:
    card_1_value = int(card_1)

if card_2 == 'A':
    card_2_value = 11
elif card_2 == 'J' or card_2 == 'Q' or card_2 == 'K':
    card_2_value = 10
else:
    card_2_value = int(card_2)

score = (card_1_value + card_2_value)


if card_1 == card_2:
    splitting_advice = 'You may also split since your cards are the same.'
else:
    splitting_advice = ' '

if score == 21:
    print('Your total is 21, Blackjack! ' + splitting_advice)
elif score == 22:
    print('Two Aces, Your total is 2 or 12, I reccomend you hit. ' + splitting_advice)
elif score >= 17:
    print('Your total is ' + str(score) + ', I reccomend you stay. ' + splitting_advice)
elif score <= 16:
    print('Your total is ' + str(score) + ', I reccomend you hit. ' + splitting_advice)