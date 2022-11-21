prompt = "\nWhat toppings would you like on your pizza?:"
prompt += "\nFive toppings maximum!"
prompt += "\n(Enter 'done' when you are finished.) "

toppings = []

# use an active variable to control how long the loop runs
while len(toppings) < 5:
    topping = input(prompt)

    # conditional w/ break statement to exit the loop
    if topping == 'done':
        print(f"Your pizza with {toppings} will be ready soon!")
        break
    else:
        print(f"Adding {topping.title()} to your pizza!")
        toppings.append(topping)

print(f"Your pizza with {toppings} will be ready soon!")