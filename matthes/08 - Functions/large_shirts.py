def make_shirt(size='L', text='I love Python'):
    """ Generate an order summary
    Default values: 
    - size: Large (L)
    - text: I love Python
    """
    print("--- Custom T-Shirt Maker Order Summary ---")
    print(f"Size: {size}")
    print(f"Custom Message: {text}\n")

# function call using default values
make_shirt()

# function call with a different size
make_shirt("M")

# function call with a custom size and message
make_shirt("XL", "I love Coding!")

# function call with keyword arguments
make_shirt(text="PYTHON!", size="S")