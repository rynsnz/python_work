# define a tuple of proteins that do not change
proteins = ('chicken', 'steak', 'carnitas', 'barbacoa', 'sofritas')

print("At Chipotle, you can choose from the following proteins:")
for protein in proteins:
    print(protein.title())

"""
this will throw a TypeError...
>>> proteins[0] = 'pollo asado'
>>> proteins[1] = 'garlic guajillo steak'
"""

# modify tuple for new proteins on the menu
proteins = ('pollo asado', 'garlic guajillo steak', 'carnitas', 'barbacoa', 
            'sofritas')
print("\nModified proteins:")
for protein in proteins:
    print(protein.title())