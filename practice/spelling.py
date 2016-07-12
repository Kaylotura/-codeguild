"""
Examines words based on user input to see if the word follows the 'I before E except after C" rule, and informs the user
if it does or does not follow the rule.
Goals for the future
Goal #1: Fix cieie bug, where if cie and ie exist in same word it states that the rule is followed.
"""

# 1. Setup
yes_rule_basic = 'ie'
yes_rule_c = 'cei'
no_rule_basic = 'ei'
no_rule_c = 'cie'

# 2. Input

words_list = input('I before E, except after C, what word would you like to check? ')

# 3. Transform/Output

if (no_rule_c in words_list) or ((no_rule_basic in words_list) and (yes_rule_c not in words_list)):
    print("I'm afraid {} breaks the rule.".format(words_list))
elif (yes_rule_basic in words_list and no_rule_c not in words_list) or yes_rule_c in words_list:
    print("Yes, {} follows the rule.".format(words_list))
else:
    print("I'm afraid {} doesn't apply to the rule.".format(words_list))

# ie = true
# ei = false
# cie = false
# cei = true
# cieie = false
# ieei = false
# eiie - false
# ceiei should = false but is returning true, I want to fix that.
