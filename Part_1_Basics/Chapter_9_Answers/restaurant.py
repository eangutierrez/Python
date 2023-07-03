"""A set of classes used to represent restaurants and ice cream stands. """

class Restaurant:
    """A simple attempt to model a restaurant."""
    
    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the type of restaurant"""
        msg= f"{self.name} is a {self.cuisine_type} restaurant."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Simulate opening the restaurant"""
        msg = f"{self.name} is now open for business!"
        print(f"\n{msg}")

    def set_number_served(self, new_number_served):
        """Set the number of customers that have been served"""
        self.number_served = new_number_served
    
    def increment_number_served(self, new_number_served):
        """Add the given amount to the number of customers served"""
        self.number_served += new_number_served


class IceCreamStand(Restaurant):
    """Create a child class for ice cream stands."""

    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize attributes of the parent class."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Print a list of all the ice cream stand flavors."""
        print(f"{self.name} has the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
