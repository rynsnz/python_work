"""
✅ A dictionary in #python is a collection of key-value pairs created with 
braces {}.
🔑 Each key is connected to a value to form a key-value pair.
"""

alien_0 = {}

# adding baseline key-value pairs
alien_0['color'] = 'green'
alien_0['points'] = 5

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# adding new key-value pairs for position
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# mofidying values in a dictionary
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# remove key-value pairs
del alien_0['points']

# track position of an alien at differnt speeds with if-elif-else chain

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Orignial position: {alien_0['x_position']}")

# most alien to the right
# determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")
