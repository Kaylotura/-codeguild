import string
import re
""" Takes input in CamelCase, CONSTANT_CASE, kebab-case, or snake_case and converts to any of the others."""

LOWERCASE_STRING = string.ascii_lowercase
UPPERCASE_LIST = list(string.ascii_uppercase)


def input_phrase_to_translate():
    """ Gets phrase to be translated from user input"""
    entered_phrase = input('Please enter a phrase in CamelCase, CONSTANT_CASE, kebab-case, or snake_case. ')
    if entered_phrase == '':
        entered_phrase = 'snake_case_test'
    return entered_phrase


def input_new_case():
    """ Gets new case to be translated to from user input
    >>> input_new_case(2)
    'CONSTANT_CASE'
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


# def check_old_case(cased_old_phrase):
#     """Checks the original case of the phrase to comment on it
#
#     >>> check_old_case(['i_eat_kebabs']):
#     'snake_case'
#     """
#     if '-' in str(cased_old_phrase):
#         old_case = 'kebab-case'
#     elif '_' in str(cased_old_phrase) and any(LOWERCASE_STRING) in str(cased_old_phrase):
#         old_case = 'snake_case'
#     elif '_' in str(cased_old_phrase) and any(LOWERCASE_STRING) not in str(cased_old_phrase):
#         old_case = 'CONSTANT_CASE'
#     if [for letter in (LOWERCASE_STRING)] in str(cased_old_phrase):
#         old_case = 'CamelCase'
#     return old_case


def slice_words_apart(unsliced_phrase):
    """Takes phrase to be translated and splits it up with spaces
    >>> slice_words_apart(i-liek-mudkips)
    'i liek mudkips'
    >>> slice_words_apart(ITouchaDaFishie)
    ' I Toucha Da Fishie'
    >>> slice_words_apart(here_come_dat_boi)
    'here come dat boi'
    >>> slice_words_apart(DO_NOT_HUG_ME_I_AM_SCARED)
    ' DO NOT HUG ME I AM SCARED'
    """
    if '-' in unsliced_phrase:
        sliced_list = unsliced_phrase.split('-')
    elif '_' in unsliced_phrase:
        sliced_list = unsliced_phrase.split('_')
    else:
        sliced_list = re.findall('[A-Z][^A-Z]*', unsliced_phrase)
    spaced_phrase = ' '.join(sliced_list)
    return spaced_phrase


def standardize_phrase_lower(phrase):
    """Sets the phrase into lowercase letters for easy manipulation
    >>> standardize_phrase_lower('You are the weakest link. Goodbye.')
    'You are the weakest link. Goodbye.'
    """
    return phrase.lower


def alter_capitalization_to_new_case(phrase, case):
    """Checks for the desired case, then capitalizes appropriately.
    >>> alter_capitalization_to_new_case(['apple', 'core'], 'CONSTANT_CASE')
    'APPLE CORE'
    >>> alter_capitalization_to_new_case(['want', 'some', 'more'], 'CamelCase')
    'Apple Core'
    """
    if case == 'CamelCase':
        capitalized_phrase = phrase.capitalize()
    elif case == 'CONSTANT_CASE':
        capitalized_phrase = phrase.upper()
    else:
        capitalized_phrase = phrase
    return capitalized_phrase


def paste_phrase(phrase):
    """Removes spaces from phrase
    >>> paste_phrase('what is your favorite meme?')
    'whatisyourfavoritememe?'
    """
    return str(phrase).replace(' ','')


def output(old_phrase, new_phrase, new_case):
    """Outputs the translation.
    output(pancakes_taste_good, snake_cake, PancakesTasteGood, CamelCase)
    PancakesTasteGood
    """
    print(old_phrase + " translated to " + new_case + " is " + new_phrase + "!")

def main ():
    """Main Function"""
    phrase_to_translate = input_phrase_to_translate()
    new_case = input_new_case()
#    old_case = check_old_case(phrase_to_translate)
    phrase_with_spaces = slice_words_apart(phrase_to_translate)
    standardized_phrase_lower = standardize_phrase_lower(phrase_with_spaces)
    appropriately_capitalized_phrase = alter_capitalization_to_new_case(standardized_phrase_lower, new_case)
    final_phrase = paste_phrase(appropriately_capitalized_phrase)
    output(phrase_to_translate, final_phrase, new_case)


if __name__ == '__main__':
    main()