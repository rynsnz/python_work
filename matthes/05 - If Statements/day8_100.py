# conditional test examples using the and/or keyword

driver_age = 17
passenger_age = 21

print('Is this driver following the instruction permit requirements?')
print((15 <= driver_age >= 17) and (passenger_age >= 21))

highschool_ed = True
commercial_ed = False

print('\nIs your driving education valid?')
print(highschool_ed or commercial_ed)

# test if items are in a list or not

proteins = ['chicken', 'steak', 'carnitas', 'barbacoa', 'sofritas']

requested_protein = 'garlic guajillo steak'
if requested_protein not in proteins:
    print(f'\nSorry! {requested_protein.title()} is not available.')

requested_protein = 'chicken'
if requested_protein in proteins:
    print(f'\n{requested_protein.title()} is available!')