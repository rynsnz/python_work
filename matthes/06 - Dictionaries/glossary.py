methods = {
    'append': 'The simplest way to add a new element to a list',
    'insert': 'A means to add a new element by specifying index and value',
    'pop': 'Remove an element by specifying index or by default the last item',
    'sort': 'Change the order of the list and store alphabetically (perm)',
    'reverse': 'Simply reverses the order of the list as is (perm)',
    'items': 'Return a sequence of key-value pairs when working with a dictionary',
    'keys': 'Simply returns just the keys of a dictionary',
    'values': 'Simply returns just the values of a dictionary',
    'set': 'Return values of a dictionary without any duplication of unique values'

}

print("Methods learned that can be used when working with Python lists.\n")
for method, explanation in methods.items():
    print(f"{method.title()}: {explanation}.")