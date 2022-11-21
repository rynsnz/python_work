available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['pineapple', 'mushrooms', 'french fries', 'extra cheese']

"""
inequality operator (!=) "does not equal to..."
"""
if requested_toppings != 'anchovies':
    print('Hold the anchovies!')

"""
testing multiple conditions
if-elif-else block used then it would skip after the first True condition
adjusted if-elif-else chain to test when a topping is not availabile
created condition to ensure list is not emply
"""

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'pineapple':
            print("Sorry, we are out of pineapple right now.")
        elif requested_topping in available_toppings:
            print(f"Adding {requested_topping}")
        else:
            print(f"Sorry, we don't have {requested_topping}")
    print('\nFinished making your pizza!')

else:
    print("Are you sure you want a plain pizza?")


"""
All of this is duplicated effort...why keep typing "Adding..."

if 'mushrooms' in requested_topping:
    print('Adding mushrooms.')
if 'pepperoni' in requested_topping:
    print('Adding pepperoni.')
if 'extra cheese' in requested_topping:
    print('Adding extra cheese.')
"""