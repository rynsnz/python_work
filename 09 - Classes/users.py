class Users:
    """A simple model of a user."""

    def __init__(self, first_name, last_name, age, hometown):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hometown = hometown

    def describe_user(self):
        """Talk about the user."""
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"{full_name} is {self.age} and is from {self.hometown.title()}.")
    
    def greet_user(self):
        """Greet the user."""
        print(f"Hello {self.first_name.title()}!")


poe = Users('poe', 'kappa', 3, 'everett')
erwin = Users('erwin', 'kappa', 26, 'hilo')
ryan = Users('ryan', 'kappa', 29, 'honolulu')

poe.describe_user()
erwin.describe_user()
ryan.describe_user()

erwin.greet_user()