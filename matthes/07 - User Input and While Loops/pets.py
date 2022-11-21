# create a list of multiple instances of something
# cat is listed multiple times in the list pets
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# with a while loop conditional statement it will run through the list
# and use the remove method to remove cat until the value no longer exists
# in the list
while 'cat' in pets:
    pets.remove('cat')

# python existed the while loop and we print the pet list again
# cat is no longer an instance of this list
print(pets)