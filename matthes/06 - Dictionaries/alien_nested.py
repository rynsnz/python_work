"""
Nesting: storing multiple dictionaires in a list example
...common to store a number of dictionaries in a list when each dictionary
contains many kinds of information about one object.
"""
# empty list for storing aliens
aliens = []

# create 30 green aliens
# function: range to tell Python how many times we want the loop to repeat
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
    
# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
# function: to ask python how many separte alien objects exist
print(f"Total number of aliens: {len(aliens)}")