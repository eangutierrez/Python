"""A class used to represent website users."""

class User: # Define the class
    """A simple attempt to model website users."""

    def __init__(self, first_name, last_name, age, username, city, country):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.username = username
        self.city = city.title()
        self.country = country.title()
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"{self.username}'s profile information:", "\n")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Username: {self.username}")
        print(f"City: {self.city}")
        print(f"Country: {self.country}")
        print(f"Login Attempts: {self.login_attempts}")

    def greet_user(self):
        """Prints a simple greeting to welcome the user."""
        print(f"\nWelcome, {self.username}!")
    
    def increment_login_attempts(self):
        """Increases the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the number of login attempts to zero."""
        self.login_attempts = 0