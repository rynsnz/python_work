# simple dictionary with famous dog names and their associated breed
pets = {
    'lassie': 'rough collie',
    'poe': 'labradoodle',
    'toto': 'cairn terrier',
    'tinkerbelle': 'chihuahua',
    'sophie': 'cocker spaniel',
    'bo': 'labradoodle'
}

# loop through a sorted dictionary
for name, breed in sorted(pets.items()):
    print(f"{name.title()}: {breed}")

# keys method
for name in pets.keys():
    print(name.title())

# values method within the set function 
for breed in set(pets.values()):
    print(breed.title())