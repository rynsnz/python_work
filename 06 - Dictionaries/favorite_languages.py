# A Dictionary of Simiar Objects

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print()
"""
looping through all the keys in a dictionary in a particular order
"""

friends = ['phil', 'sarah']

# method: keys() | sorted()
# function: print()
for name in sorted(favorite_languages.keys()):
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print()
"""
keys() method helpful to validate 'in' | 'not in'
"""

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print()
"""
looping through all the values in a dictionary in a particular order
"""
print("The following languages have been mentioned:")

# function: print()
# method: values() | set()
for language in set(favorite_languages.values()):
    print(language.title())