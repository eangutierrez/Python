class Employee():
    """A class that represents employees in a company."""

    def __init__(self, f_name, l_name, salary):
        """Initialize the employee."""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary
    
    def give_raise(self, amount=5000):
        """Give an employee a raise."""
        self.salary += amount