"""
Calculates how much it will cost to paint one or more walls, based on user
input and the assumption that a gallon of paint covers 400 square feet.
I imagine I can solve for the advanced solution with a while loop, but find my
weekend quickly running out of time.
"""

# 1. Setup
sqaure_ft_in_gallon = 400

# 2. Input

wall_width = float(input("Please enter the width of the wall in feet. "))
wall_height = float(input("Please enter the height of the wall in feet. "))
coats = float(input("How many coats would you like to apply? "))
paint_cost = float(input("How much does the paint cost? "))


# 3. Transform

wall_square_feet = (wall_width * wall_height)
gallons = (wall_square_feet / sqaure_ft_in_gallon)
gallons = (wall_square_feet / sqaure_ft_in_gallon) * coats
int(gallons) + 1
total_cost = (gallons * paint_cost)


# 4. Output
print(str(gallons) + ' gallons of paint will be required for \
' + str(coats) + 'coats of pain on your ' + str(wall_square_feet) + ' \
square foot wall, and will cost $' + str(total_cost))
