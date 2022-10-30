dimensions = (200, 50)

print("Orignial dimensions:")
for dimension in dimensions:
    print(dimension)

"""
a tuple is immutable this will throw a TypeError
>>> dimensions[0] = 100
"""

dimensions = (400, 50)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)