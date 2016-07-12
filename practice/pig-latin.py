import string

"""
Translates english into pig-latin
Note: I still have not figured out to solve for punctuation that begins a word as of yet.
Future Goal #1: Solve for Capital and Punctuation on one word [e.g. No.]
Future Goal #2: Solve for apostraphes
Future Goal #3: Solve for punctuation that begins a word, [e.g. (Sam) "Bob" or 'Tiffany' 'Tis]
Future Goal #4: Solve for capitals in the middle of a word, [e.g. McDonalds]
Future Goal #5: Solve for multiple punctuation [e.g. "Is that butter?" or (Don't turn off the lights.)]
Note: With these goals, I'd like to avoid ruining punctuation around short words such as I and My.
"""

# 1. Setup
FIRST_VOWEL = 'a e i o u'.split()
LATER_VOWEL = 'a e i o u y'.split()
PUNCTUATION_LIST = list(string.punctuation)
CAPITALS_LIST = list(string.ascii_uppercase)
new_punctuation = ''
new_phrase = ''

# 2. Input

english_phrase = input("What would you like to Anslatetray? ").split()

# 3. Transform

i= 0
while i < len(english_phrase):
    english_word = english_phrase[i]
    if english_word[-1] in PUNCTUATION_LIST:
        new_punctuation = english_word[-1]
        modified_english_word = english_word.strip(new_punctuation)
        re_capitlaize_word = False
    elif english_word[0] in CAPITALS_LIST:
        modified_english_word = english_word.lower()
        re_capitlaize_word = True
    else:
        modified_english_word = english_word
        re_capitlaize_word = False

    if english_word[0] in FIRST_VOWEL:
        pig_latin_word = modified_english_word + 'yay'
    elif english_word[0] not in FIRST_VOWEL and english_word[1] in LATER_VOWEL:
        pig_latin_word = modified_english_word[1:] + modified_english_word[:1] + 'ay'
    elif english_word[0] not in FIRST_VOWEL and  english_word[1] not in LATER_VOWEL:
        pig_latin_word = modified_english_word[2:] + modified_english_word[:2] + 'ay'

    if re_capitlaize_word == True:
         new_phrase += '{} '.format(pig_latin_word.capitalize() + new_punctuation )
    else:
            new_phrase += '{} '.format(pig_latin_word + new_punctuation)
    new_punctuation = ''
    i +=1

# 4. Print

print(new_phrase)