prompt = "\nWhat five toppings would you like on your pizza?:"
prompt += "\n(Enter 'done' when you are finished.) "

toppings = []

# use an active variable to control how long the loop runs
while len(toppings) < 5:
    topping = input(prompt)

    # conditional w/ break statement to exit the loop
    if topping == 'done':
        break
    else:
        print(f"Adding {topping.title()} to your pizza!")
        toppings.append(topping)

if len(toppings) == 0:
    print(f"Are you sure you don't want any toppings?")
else: print(f"Your pizza with {toppings} will be ready soon!")