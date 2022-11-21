class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbered_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, a model example of authentic {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, total):
        """Set the customer count to given value."""
        self.numbered_served = total

    def increment_number_served(self, total):
        """Add the given amount to the customer count."""
        self.numbered_served += total

    def read_number_served(self):
        """Print a statement of customers the restaurant has served."""
        print(f"{self.restaurant_name} has served {self.numbered_served} customers.")

# make an instance of the Restaurant class
restaurant = Restaurant('Dos Amigos', 'Mexican')

# print attributes
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.read_number_served)

# update attributes
restaurant.set_number_served(15)

# call methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.read_number_served()

hanakawa = Restaurant('Hanakawa', 'Japanese')
fodrak = Restaurant('Fodrak', 'Fast Food')
thai_noodles_cafe = Restaurant('Thai Noodles Cafe', 'Thai')

hanakawa.describe_restaurant()
fodrak.describe_restaurant()
thai_noodles_cafe.describe_restaurant()