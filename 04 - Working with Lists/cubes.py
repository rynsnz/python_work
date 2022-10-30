# n ** 3; from n = 1 to 10
# make a list cubes and print using a for loop
cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

# using a list comprehension is "more pythonic!"
# expression for member in iterable
cubes = [value**3 for value in range(1,11)]
print(cubes)