"""Asks the user for a list of space separated words and sorts them with oxford comma"""

# 1. Setup
# N/A

# 2. Input
word_list = (input('Please enter words seperated by a space. ')).split()

# 3. Transform
count = len (word_list)
if count == 1:
    word_string = str(word_list)
elif count == 2:
    wordstring = ' and'.joing(word_list)
else:
    word_string = ', '.join(word_list[0:-1])
    word_string = word_string + ', and ' + word_list[-1]

#4  Output
print(word_string)
