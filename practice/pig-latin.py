""" Translates english into pig-latin.
Note: I still have not figured out to solve for punctuation that begins a word as of yet.
Future Goal #1: Solve for punctuation that begins a word, [e.g. (Sam) "Bob" or 'Tiffany' 'Tis]
Future Goal #2: Solve for multiple punctuation [e.g. "Is that butter?" or (Don't turn off the lights.)]
Note: With these goals, I'd like to avoid ruining punctuation around short words such as I and My.
EDIT 12-July-2016: Altering code to be a series of functions, solved for some apostrophes and capitals.
EDIT 12-July-2016: Added list of words in English that start with Y-vowel for higher accuracy.
"""

import string

# 1. Setup Define/Functions


FIRST_VOWELS = 'a e i o u A E I O U'.split()
LATER_VOWELS = 'a e i o u y A E I O U Y'.split()
SPECIAL_CASES = 'Ybe ybe Ycleped ycleped Yclept yclept Ysgard Ydo ydo Ydrad ydrad Yfere yfere Ygdrasyl ygdrasyl Yghe'\
               'ygh Ygo ygo Yground yground Ypres ypres Ypsiliform ypsiliform Ypsiloid ypsiloid Yren yren Ysame ysame '\
               'Ytterbic ytterbic Ytterbium ytterbium Yttria yttria Yttric yttric Yttriferous yttriferous Yttrious ' \
               'yttrious Yttrium yttrium Yttro-cerite yttro-cerite Yttro-columbite yttro-columbite Yttro-tantalite ' \
               'yttro-tantalite Yvel yvel Ywar ywar Ywis ywis'.split()
PUNCTUATIONS = list(string.punctuation)
CAPITALS = list(string.ascii_uppercase)


# 2. Define Functions


def get_input():
    """Aquires english phrase from user input and casts it as a list of strings.  """
    typed_phrase = input("What would you like to Anslatetray? ").split()
    return typed_phrase


def pull_english_word_from_list (phrase, i):
    """Pulls a single word from the list of english words to be translated."""
    pull_word = phrase[i]
    return pull_word

def flip_capital_boolean(word):
    """Checks for capitals at the start of a word, flips a boolean switch to run capitalizing function"""
    return word[0] in CAPITALS

def check_for_and_cut_capitals(english_word):
    """Checks for capitals at the start of a word, and casts it to lowercase
    This is a more complex function to accommodate bicapitalization.
    """
    uppercase_first_letter = english_word[0]
    lowercase_first_lettter = uppercase_first_letter.lower()
    strip_capital_english_word = english_word.replace(uppercase_first_letter,lowercase_first_lettter,1)
    return strip_capital_english_word

def flip_punctuation_boolean(word):
    """Checks for punctuation at end of word and flips a boolean switch if it is present """
    return word[-1] in PUNCTUATIONS

def save_punctuation(english_word):
    """saves the punctuation of the english word"""
    punctuation = english_word[-1]
    return punctuation

def strip_punctuation(english_word):
    """cuts punctuation of english word"""
    return english_word[0:-1]

def convert_english_word_to_pig_latin_word(english_word):
    """Translates english_word into pig_latin_word considering for up to 4 consonants in a row."""
    if english_word[0] in FIRST_VOWELS:
        pig_latin_word = english_word + 'yay'
    elif english_word in SPECIAL_CASES:
        pig_latin_word = english_word + 'yay'
    elif english_word[1] in LATER_VOWELS:
        pig_latin_word = english_word[1:] + english_word[:1] + 'ay'
    elif english_word[2] in LATER_VOWELS:
        pig_latin_word = english_word[2:] + english_word[:2] + 'ay'
    else:
        pig_latin_word = english_word[3:] + english_word[:3] + 'ay'
    return pig_latin_word

def capitalize_pig_latin_word(temp_pig_latin_word):
    """If the english word was capitalized, this function appropriately capitalized the Pig Latin Word"""
    lowercase_first_letter = temp_pig_latin_word[0]
    uppercase_first_letter = lowercase_first_letter.capitalize()
    pig_latin_word = temp_pig_latin_word.replace(lowercase_first_letter, uppercase_first_letter, 1)
    return pig_latin_word

def paste_punctution_back_on_pig_latin_word(temp_pig_latin_word, punctuation):
    """Adds punctuation to pig_latin_word as well as adding a space for a nice final phrase."""
    return temp_pig_latin_word + punctuation

def print_full_pig_latin_phrase (phrase):
    print(phrase)


# 3. Main


def main():
    """Main Function"""
    pig_latin_phrase = ''
    english_phrase = get_phrase_casted_into_list()




    for english_word in english_phrase:
        capitalize_boolean = flip_capital_boolean(english_word)
        if capitalize_boolean == True:
            english_word = check_for_and_cut_capitals(english_word)
        punctuation_boolean = flip_punctuation_boolean(english_word)
        if punctuation_boolean == True:
            saved_punctuation = save_punctuation(english_word)
            english_word = strip_punctuation(english_word)
        temp_pig_latin_word = convert_english_word_to_pig_latin_word(english_word)
        if capitalize_boolean == True:
            temp_pig_latin_word = capitalize_pig_latin_word(temp_pig_latin_word)
        if punctuation_boolean == True:
            temp_pig_latin_word = paste_punctution_back_on_pig_latin_word (temp_pig_latin_word,saved_punctuation)
        pig_latin_phrase += temp_pig_latin_word + ' '
    print_full_pig_latin_phrase(pig_latin_phrase)
main()




def main ():
english_words = get_input()
capital_indices_in_english_words = check capital index(english_words)
lowercase_words = lowercase_first_letters(english_words)
pig_latin_words = translate_to_pig_latin(lowercase_words)
    cut_and_save_punctuation
    alter_words
    paste_ay
re_cased_pig_latin_words = re_case_words(pig_latin_words)
re_punctuated_pig_latin_words = re_punctuate_words (re_cased_pig_latin_words)
output(re_cased_pig_latin_words)



