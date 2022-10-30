def sandwich_maker(*toppings):
    """Summarize the items a customer wants on a sandwich."""
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

sandwich_maker('turkey', 'lettuce', 'tomatoes', 'cucumbers', 'green peppers', 'red onions')
sandwich_maker('turkey', 'ham', 'swiss cheese')