# define an empty dictionary
responces = {}

# Set a flag to indicate the polling is active
polling_active = True

# as long as polling_active is true this loop will continue to run
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("If you could go anywhere in the world, where would you go? ")

    # Store the response in a dictionary
    responces[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes | no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responces.items():
    print(f"{name} would like to visit {response}.")