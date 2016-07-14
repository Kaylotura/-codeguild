""" Takes input in CamelCase, CONSTANT_CASE, kebab-case, or snake_case and converts to any of the others."""
import string
import re

LOWERCASE_LIST = list(string.ascii_lowercase)
UPPERCASE_LIST = list(string.ascii_uppercase)

def input_phrase_to_translate():
    """ Gets phrase to be translated from user input"""
    entered_phrase = input('Please enter a phrase in CamelCase, CONSTANT_CASE, kebab-case, or snake_case. ')
    if entered_phrase == '':
        entered_phrase = 'snake_case_test'
    return entered_phrase


def input_new_case():
    """ Gets new case to be translated to from user input
    """
    print('CamelCase = 1, CONSTANT_CASE = 2, kebab-case = 3, or snake_case = 4')
    case_by_number = input('What case would you like this translated to? ')
    if case_by_number == '1':
        entered_case = 'CamelCase'
    elif case_by_number == '2':
        entered_case = 'CONSTANT_CASE'
    elif case_by_number == '3':
        entered_case = 'kebab-case'
    elif case_by_number == '4':
        entered_case = 'snake_case'
    elif case_by_number == '':
        entered_case = 'CamelCase'
    return entered_case


def check_old_case(cased_old_phrase):
    """Checks the original case of the phrase to comment on it
    >>> check_old_case('i_eat_snakes')
    'snake_case'
    >>> check_old_case('i-eat-kebabs')
    'kebab-case'
    >>> check_old_case('I_CONSTANTLY_EAT')
    'CONSTANT_CASE'
    >>> check_old_case('IEatCamels')
    'CamelCase'
    """
    if '-' in cased_old_phrase:
        old_case = 'kebab-case'
    elif '_' in cased_old_phrase and any(letter for letter in cased_old_phrase if letter.islower()):
        old_case = 'snake_case'
    elif '_' in cased_old_phrase:
        old_case = 'CONSTANT_CASE'
    elif '-' not in cased_old_phrase and '_' not in cased_old_phrase:
        old_case = 'CamelCase'
    return old_case


def slice_words_apart(unsliced_phrase):
    """Takes phrase to be translated and splits it up with spaces
    >>> slice_words_apart('i-liek-mudkips')
    'i liek mudkips'
    >>> slice_words_apart('ITouchaDaFishie')
    'I Toucha Da Fishie'
    >>> slice_words_apart('here_come_dat_boi')
    'here come dat boi'
    >>> slice_words_apart('DO_NOT_HUG_ME_I_AM_SCARED')
    'DO NOT HUG ME I AM SCARED'
    """
    if '-' in unsliced_phrase:
        sliced_list = unsliced_phrase.split('-')
    elif '_' in unsliced_phrase:
        sliced_list = unsliced_phrase.split('_')
    else:
        sliced_list = re.findall('[A-Z][^A-Z]*', unsliced_phrase)
    spaced_phrase = " ".join(sliced_list)
    return spaced_phrase


def standardize_phrase_lower(phrase):
    """Sets the phrase into lowercase letters for easy manipulation
    >>> standardize_phrase_lower('You are the weakest link Goodbye')
    'you are the weakest link goodbye'
    """
    lower_phrase = phrase.lower()
    return lower_phrase

def alter_capitalization_to_new_case(phrase, case):
    """Checks for the desired case, then capitalizes appropriately.
    >>> alter_capitalization_to_new_case('apple core', 'CONSTANT_CASE')
    'APPLE CORE'
    >>> alter_capitalization_to_new_case('want some more', 'CamelCase')
    'Want Some More'
    """
    if case == 'CamelCase':
        capitalized_phrase = phrase.title()
    elif case == 'CONSTANT_CASE':
        capitalized_phrase = phrase.upper()
    else:
        capitalized_phrase = phrase
    return capitalized_phrase


def paste_phrase(phrase, new_case):
    """Removes spaces from phrase

    >>> paste_phrase('what is your favorite meme','snake_case')
    'what_is_your_favorite_meme'
    >>> paste_phrase('WHO DARES WINS','CONSTANT_CASE')
    'WHO_DARES_WINS'
    >>> paste_phrase('do not taser me bro','kebab-case')
    'do-not-taser-me-bro'
    >>> paste_phrase('What The Rock Is Cooking','CamelCase')
    'WhatTheRockIsCooking'
    """
    if new_case == 'CamelCase':
        pasted_phrase = str(phrase).replace(' ','')
    elif new_case =='CONSTANT_CASE' or new_case =='snake_case':
        pasted_phrase = str(phrase).replace(' ', '_')
    elif new_case =='kebab-case':
        pasted_phrase = str(phrase).replace(' ', '-')
    return pasted_phrase

def output(old_phrase, new_phrase, old_case, new_case):
    """Outputs the translation.
    """
    print(old_phrase + " translated from " + old_case + " to " + new_case + " is " + new_phrase + "!")

def main():
    """Main Function"""
    phrase_to_translate = input_phrase_to_translate()
    new_case = input_new_case()
    old_case = check_old_case(phrase_to_translate)
    phrase_with_spaces = slice_words_apart(phrase_to_translate)
    standardized_phrase_lower = standardize_phrase_lower(phrase_with_spaces)
    appropriately_capitalized_phrase = alter_capitalization_to_new_case(standardized_phrase_lower, new_case)
    final_phrase = paste_phrase(appropriately_capitalized_phrase, new_case)
    output(phrase_to_translate, final_phrase, old_case, new_case)

if __name__ == '__main__':
    main()