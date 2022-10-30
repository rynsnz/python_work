# dictionaries of famous dog names and their associated breed
pet_0 = {'name': 'lassie', 'breed': 'rough collie'}
pet_1 = {'name': 'poe', 'breed': 'labradoodle'}
pet_2 = {'name': 'toto', 'breed': 'cairn terrier'}
pet_3 = {'name': 'tinkerbelle', 'breed': 'chihuahua'}
pet_4 = {'name': 'sophie', 'breed': 'cocker spaniel'}
pet_5 = {'name': 'bo', 'breed': 'labradoodle'}

# list of all the famous dogs
pets = [pet_0, pet_1, pet_2, pet_3, pet_4, pet_5]

# loop through a list of dictionaries
for pet in pets:
    print(f"{pet['name'].title()} is a {pet['breed'].title()}.")