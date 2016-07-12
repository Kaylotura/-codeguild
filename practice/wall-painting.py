"""
Calculates how much it will cost to paint one or more walls, based on user
input and the assumption that a gallon of paint covers 400 square feet.
I imagine I can solve for the advanced solution with a while loop, but find my
weekend quickly running out of time.
Edit July.11.2016: cleaned up code considerably, added more variables, and excised excess no-op code.
"""

# 1. Setup
SQUARE_FT_IN_GALLONS= 400

# 2. Input

wall_width = float(input('Please enter the width of the wall in feet. '))
wall_height = float(input('Please enter the height of the wall in feet. '))
number_of_coats = float(input('How many coats would you like to apply? '))
paint_cost = float(input('How much does the paint cost? '))


# 3. Transform

wall_square_feet = (wall_width * wall_height)
gallons_per_coat = (wall_square_feet / SQUARE_FT_IN_GALLONS)
gallons_total_wall = gallons_per_coat * number_of_coats
round_up_gallons = int(gallons_total_wall) + 1
total_cost = (round_up_gallons * paint_cost)

# 4. Output
print(str(round_up_gallons) + ' gallons of paint will be required for ' + str(number_of_coats
) + 'coats of pain on your ' + str(wall_square_feet) + ' square foot wall, and will cost $' + str(total_cost))
