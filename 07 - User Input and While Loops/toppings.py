prompt = "\nWhat pizza toppings do you want:"
prompt += "\n(Enter 'quit' when you are finished.) "

toppings = []

while True:
    topping = input(prompt)

    if topping == 'quit':
        print(f"Your pizza with {toppings} will be ready soon!")
        break
    else:
        print(f"Adding {topping.title()} to your pizza!")
        toppings.append(topping)