"""Asks for user's name and age, and greets them and tells them how old they'll be next year"""

# 1. Setup
# N/A

# 2. Input
name = input ("Hello, my name is Greetbot, what's your name? ")
age = input(name + ' is a lovely name! How old are you, ' + name + '? ')

# 3. Transform
olderage = str(int(age) + 1)

# 4. Output
print ("You're " + age + "-years old? Wow, I guess that means you're going to be " + olderage + " next year!")
