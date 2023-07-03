"""A set of classes used to represent Admin users and their privileges."""

from user import User

class Admin(User):
    """Represents aspects of users, specific to the Admins.""" 

    def __init__(self, first_name, last_name, age, username, city, country):
        """Initialize attributes of the parent class"""
        super().__init__(first_name, last_name, age, username, city, country)

        """Initialize attributes for the list of privileges."""
        self.privileges = Privileges()


class Privileges():
    """Create the Privileges class to store all the methods about privileges."""

    def __init__(self, privileges=[]):
        """Initialize attributes for the class."""
        self.privileges = privileges

    def show_privileges(self):
        """List the administrator's set of privileges."""
        print("\nThis user has the following privileges:")
        if self.privileges:
                for privilege in self.privileges:
                    print(f"- {privilege}")
        else:
            print("- N\A")