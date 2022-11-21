"""
Conditional Tests
"""

"""
Test for equality and inequality with strings
"""
model = 'GLI'
print('Is model == "GLI"? I predict True.')
print(model == 'GLI')

print('\nIs model == "Jetta"? I predict False.')
print(model == 'Jetta')

"""
Test using the string lower() method
"""
username = 'Guest'
print('\nIs username == "Guest" while ignoring case? I predict True.')
print(username.lower() == 'guest')


"""
Numerical tests...
"""

# equality
guest_age = 21
print('\nIs the guest 21?')
print(guest_age == 21)

# inequality
guest_age = 65
print('\nIs the guest not 21?')
print(guest_age != 21)

# greater than
guest_age = 65
print('\nIs the guest greater than 21?')
print(guest_age > 21)

# less than
guest_age = 65
print('\nIs the guest less than 21?')
print(guest_age < 21)

# less than or equal to
guest_age = 65
print('\nIs the guest less than or equal to 64?')
print(guest_age <= 64)

# greater than or equal to
guest_age = 65
print('\nIs the guest less than or equal to 65?')
print(guest_age >= 65)

# conditional test using the and keyword and the or keyword
"""
If you are age 15-17, you must be enrolled in, 
or 30 days prior to active participation in, 
an approved driver education course.
"""

driver_age = 17

"""
You also may practice driving with an adult who is at least age 21
Has a license for the type of vehicle you are driving
Has at least one year of driving experience.
"""
passenger_age = 21

print('\nIs this driver following the instruction permit requirements?')
print((15 <= driver_age >= 17) and (passenger_age >= 21))

"""
Test whether items are in a list or not
"""
proteins = ['chicken', 'steak', 'carnitas', 'barbacoa', 'sofritas']

requested_protein = 'garlic guajillo steak'
if requested_protein not in proteins:
    print(f'\nSorry! {requested_protein.title()} is not available.')

requested_protein = 'chicken'
if requested_protein in proteins:
    print(f'\n{requested_protein.title()} is available!')

