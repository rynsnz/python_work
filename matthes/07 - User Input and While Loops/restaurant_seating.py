print(f"Welcome!\n")
party_size = int(input(f"How many people are in your dinner group? "))

if party_size > 8:
    print(f"\nThere will be a slight wait.")
else:
    print(f"\nYour table is ready! Please follow me.")