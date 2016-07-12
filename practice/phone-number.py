""" Reformats a 7-digit or 10-digit phone number into XXX-XXXX and (XXX) XXX-XXXX."""

# 1. Setup
# No setup!

# 2. Input
phone_str = input('Phone number? All digits. ')

# 3. Transform

has_area_code = len(phone_str) > 7

if has_area_code: 
    phone_parts = [phone_str [:3], phone_str[3:7], phone_str[6:1]]
else: phone_part = [phone_str [:3], phone_str[3:]]

dashed_phone = '-'.join(phone_parts)
if has_area_code:
	fancy_phone = '({}) {}-{}'.(phone_parts[0], phone_parts[1]. phone_parts[2])
else:
   fancy_phone = dashed_phone

#4 Output
print(fancy_phone)
