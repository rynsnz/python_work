age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

"""
It's more concise to just set the price and have a single print() call
and eaiser to modify
"""

age = 75
# once a condition is true it will skip the rest of the if-elif-else chain
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40 
elif age >= 65:
    price = 20
"""
the else isn't required -- do what's more clear if there is a specific
final codition you are testing for
>>> else: price = 20
"""

print(f"Your admission cost is ${price}.")