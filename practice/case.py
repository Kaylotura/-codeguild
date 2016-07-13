import string

""" Takes input in CamelCase, CONSTANT_CASE, kebab-case, or snake_case and converts to any of the others."""

LOWERCASE_LIST = list(string.ascii_lowercase)

def input_phrase_to_translate():
    """ Gets phrase to be translated from user input"""
    entered_phrase = list(input('Please enter a phrase in CamelCase, CONSTANT_CASE, kebab-case, or snake_case. '))
    if entered_phrase == '':
        entered_phrase = 'snake_case_test'
    return entered_phrase

def input_new_case():
    """ Gets new case to be translated to from user input"""
    print('CamelCase = 1, CONSTANT_CASE = 2, kebab-case = 3, or snake_case = 4')
    case_by_number = input('What case would you like this translated to? ')
    if  case_by_number == '1':
        entered_case = 'CamelCase'
    elif case_by_number == '2':
        entered_case = 'CONSTANT_CASE'
    elif case_by_number == '3':
        entered_case = 'kebab-case'
    elif case_by_number == '4':
        entered_case = 'snake_case'
    elif case_by_number == '':
        entered_case = 'CamelCase'
    return entered_phrase

def check_old_case(cased_old_phrase):
    """Checks the original case of the phrase to comment on it"""
    if '-' in cased_old_phrase:
        old_case = 'kebab-case'
    elif '_' in cased_old_phrase and any(LOWERCASE_LIST) in cased_old_phrase :
        old_case = 'snake_case'
    elif '_' in cased_old_phrase and any(LOWERCASE_LIST) not in cased_old_phrase:
        old_case = 'CONSTANT_CASE'
    elif any(LOWERCASE_LIST) in cased_old_phrase:
        old_case = 'CamelCase'
    return old_case

def slice_words_apart(unsliced_phrase):
    dash_sliced_phrase = [word.replace(-, ) for word in unsliced_phrase]
    underscore_sliced_phrase = [word.replace(_, ) for word in unsliced_phrase]
    totally_sliced_phrase = [word + ' ' for word in unsliced_phrase]
    return sliced_words


def main ()
    """Main Function"""
    phrase_to_translate = input_phrase_to_translate()
    new_case = input_new_case()
    old_case = check_old_case(phrase_to_translate)
    phrase_with_spaces = slice_words_apart(phrase_to_translate)
    standardized_phrase_lower = standardize_phrase_lower(phrase_to_translate)
    appropriately_capitalized_phrase = alter_capitalization_to_new_case (standardized_phrase_lower)
    final_phrase = paste_phrase(appropriately_capitalized_phrase)
    output(final_phrase)


# 1) Take Input (prash_to_translate)
# 2) Take Input (new_case)
# 3) Slice words apart
# 	if snake or if CONSTANT:
# 		replace _ with ' '
# 	elif kebab:
# 		replace - with ' '
# 	elif Camel:
# 		insert ' ' before CAPITALS
# 4) Standardize words
# 	lowercase all word
# 5) Check new case & alter cases as needed
# 	if Camel:
# 		uppercase 1st letter in each word
# 	if CONSTANT:
# 		uppercase all letters
# 6) Pastewords
# 		if snake or if CONSTANT:
# 		replace ' ' with '_'
# 	elif kebab:
# 		replace ' ' with '-'
# 	elif Camel:
# 		remove ' ' before
# 7) Print


main()