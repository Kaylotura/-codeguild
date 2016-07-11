"""Gives basic Blackjack advice based on user input."""

# 1. Setup

card1 = str(input('Please enter the first card '))
card2 = str(input('Please enter the second card '))

# 2. transform

if card1 == ('A'):
    card1v = 11
if card1 == ('J'):
    card1v = 10
if card1 == ('Q'):
    card1v = 10
if card1 == ('K'):
    card1v = 10
if card1 == ('10'):
    card1v = 10
if card1 == ('9'):
    card1v = 9
if card1 == ('8'):
    card1v = 8
if card1 == ('7'):
    card1v = 7
if card1 == ('6'):
    card1v = 6
if card1 == ('5'):
    card1v = 5
if card1 == ('4'):
    card1v = 4
if card1 == ('3'):
    card1v = 3
if card1 == ('2'):
    card1v = 2
if card2 == ('A'):
    card2v = 11
if card2 == ('J'):
    card2v = 10
if card2 == ('Q'):
    card2v = 10
if card2 == ('K'):
    card2v = 10
if card2 == ('10'):
    card2v = 10
if card2 == ('9'):
    card2v = 9
if card2 == ('8'):
    card2v = 8
if card2 == ('7'):
    card2v = 7
if card2 == ('6'):
    card2v = 6
if card2 == ('5'):
    card2v = 5
if card2 == ('4'):
    card2v = 4
if card2 == ('3'):
    card2v = 3
if card2 == ('2'):
    card2v = 2

score = (card1v + card2v)

if score == 21:
    print ("21, Blackjack!")
elif score == 22:
    print ("Two Aces, 2 or 12, I reccomend you hit.")
elif score >= 17:
    print (str(score) + ", I reccomend you stay.")
elif score <= 16:
    print (str(score) + ", I reccomend you hit.")
