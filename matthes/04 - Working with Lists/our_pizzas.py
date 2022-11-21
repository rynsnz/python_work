# establish list
pizzas = ['cheese', 'pepperoni', 'margherita']

# copy original list to another
friend_pizzas = pizzas[:]

# update each list with a new type
pizzas.append('veggie')
friend_pizzas.append('bbq chicken')

# demonstate two seperate lists
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)