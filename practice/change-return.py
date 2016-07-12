"""Takes user input and  figures out how to divvy up an amount of change into \
the fewest bills and coins possible. Unfinished"""

# 1. Setup
# N/A

# 2. Input
change_total = input("What is the value of your change in cents? ")

# 3. Transform


hundred_thousand_bill = int(change_total) // 10000000

ten_thousand_bill = (int(change_total) - (hundred_thousand_bill * 10000000)) // 1000000

five_thousand_bill = (int(change_total) - (hundred_thousand_bill * 10000000) - (ten_thousand_bill * 1000000)) // 500000

one_thousand_bill = (int(change_total) - (hundred_thousand_bill * 10000000) - (ten_thousand_bill * 1000000) - \
                     (five_thousand_bill * 500000)) // 100000

five_hundred_bill = (int(change_total) - (hundred_thousand_bill * 10000000) - (ten_thousand_bill * 1000000) - \
                     (five_thousand_bill * 500000) - (one_thousand_bill * 100000)) // 50000

one_hundred_bill = (int(change_total) - (hundred_thousand_bill * 10000000) - (ten_thousand_bill * 1000000) - \
                    (five_thousand_bill * 500000) - (one_thousand_bill * 100000) - (five_hundred_bill * 50000)) // 10000

fifty_bill = (int(change_total) - (hundred_thousand_bill * 10000000) - (ten_thousand_bill * 1000000) - \
              (five_thousand_bill * 500000) - (one_thousand_bill * 100000) - (five_hundred_bill * 50000) - \
              (one_hundred_bill * 10000)) // 5000

twenty_bill = (int(change_total) - (hundred_thousand_bill * 10000000) - (ten_thousand_bill * 1000000) - \
               (five_thousand_bill * 500000) - (one_thousand_bill * 100000) - (five_hundred_bill * 50000) - \
               (one_hundred_bill * 10000) - (fifty_bill * 5000)) // 2000

ten_bill = (int(change_total) - (hundred_thousand_bill * 10000000) - (ten_thousand_bill * 1000000) - \
            (five_thousand_bill * 500000) - (one_thousand_bill * 100000) - (five_hundred_bill * 50000) - \
            (one_hundred_bill * 10000) - (fifty_bill * 5000) - (twenty_bill * 2000)) // 1000

five_bill = (int(change_total) - (hundred_thousand_bill * 10000000) - (ten_thousand_bill * 1000000) - \
             (five_thousand_bill * 500000) - (one_thousand_bill * 100000) - (five_hundred_bill * 50000) - \
             (one_hundred_bill * 10000) - (fifty_bill * 5000) - (twenty_bill * 2000) - (ten_bill * 1000)) // 500

two_bill = (int(change_total) - (hundred_thousand_bill * 10000000) - (ten_thousand_bill * 1000000) - \
            (five_thousand_bill * 500000) - (one_thousand_bill * 100000) - (five_hundred_bill * 50000) - \
            (one_hundred_bill * 10000) - (fifty_bill * 5000) - (twenty_bill * 2000) - (ten_bill * 1000) - \
            (five_bill * 500)) // 200

one_bill = (int(change_total) - (hundred_thousand_bill * 10000000) - (ten_thousand_bill * 1000000) - \
            (five_thousand_bill * 500000) - (one_thousand_bill * 100000) - (five_hundred_bill * 50000) - \
            (one_hundred_bill * 10000) - (fifty_bill * 5000) - (twenty_bill * 2000) - (ten_bill * 1000) - \
            (five_bill * 500) -(two_bill * 200)) // 100

fifty_cent = (int(change_total) - (hundred_thousand_bill * 10000000) - (ten_thousand_bill * 1000000) - \
            (five_thousand_bill * 500000) - (one_thousand_bill * 100000) - (five_hundred_bill * 50000) - \
            (one_hundred_bill * 10000) - (fifty_bill * 5000) - (twenty_bill * 2000) - (ten_bill * 1000) - \
            (five_bill * 500) - (two_bill * 200) - (one_bill * 100)) // 50

quarters = (int(change_total) - (hundred_thousand_bill * 10000000) - (ten_thousand_bill * 1000000) - \
              (five_thousand_bill * 500000) - (one_thousand_bill * 100000) - (five_hundred_bill * 50000) - \
              (one_hundred_bill * 10000) - (fifty_bill * 5000) - (twenty_bill * 2000) - (ten_bill * 1000) - \
              (five_bill * 500) - (two_bill * 200) - (one_bill * 100) - (fifty_cent * 50)) // 25

dimes = (int(change_total) - (hundred_thousand_bill * 10000000) - (ten_thousand_bill * 1000000) - \
            (five_thousand_bill * 500000) - (one_thousand_bill * 100000) - (five_hundred_bill * 50000) - \
            (one_hundred_bill * 10000) - (fifty_bill * 5000) - (twenty_bill * 2000) - (ten_bill * 1000) - \
            (five_bill * 500) - (two_bill * 200) - (one_bill * 100) - (fifty_cent * 50) - (quarters * 25)) // 10

#
# nickles
#
# nickles = (int(change_total) - (quarters * 25) - (dimes * 10)) // 5
# pennies = (int(change_total) - (quarters * 25) - (dimes * 10) - (nickles * 5))
#
# # 4. Output
# print('Your change is.')
#
# if quarters >= 1:
#     print(str(quarters) + " quarters")
# if dimes >= 1:
#     print(str(dimes) + " dimes")
# if nickles >= 1:
#     print(str(nickles) + " nickles")
# if pennies >= 1:
#     print(str(pennies) + " pennies")
