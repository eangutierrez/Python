#---------------------------------------------#
#-- PYTHON CRASH COURSE CHAPTER 9 EXERCISES --#
#---------------------------------------------#
#   
# -- Author: Tony Gutierrez
# -- Date: 05/21/2023 
# -- Tools used: Python, VS Code

# These are the answers to the Chapter 9 exercises on Python Crash Course, 2nd Edition by Eric Matthes
# Note: Please note that all files must be in the same directory for the import statements to work

# Problem 9.1: This code creates a class called Restaurant, stores two attributes
# in the __init__(): restaurant_name and cuisine_type, make method
# called describe_restaurant() that prints these two pieces of info
# and a method called open_restaurant() that prints a message saying
# its open. Finally, it make an instance called restaurant from 
# this class, prints the two attributes individually, then calls 
# both methods
print("Problem 9.1")
class Restaurant:
    """A simple attempt to model a restaurant."""
    
    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the type of restaurant"""
        msg= f"{self.name} is a {self.cuisine_type} restaurant."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Simulate opening the restaurant"""
        msg = f"{self.name} is now open for business!"
        print(f"\n{msg}")


# Make an instance representing a specific restaurant
restaurant = Restaurant('Nuovo Vesuvio', 'pizza')

# Print both attributes individually, then call both methods
print(f"The restaurant's name is {restaurant.name}.")
print(f"{restaurant.name} serves {restaurant.cuisine_type}.")

restaurant.describe_restaurant()
restaurant.open_restaurant()



# Problem 9.2: This code uses the code from Problem 9.1 as base, creates three different
# instances from the Restaurant class, and calls the describe_restaurant()
# method for each instance
print("Problem 9.2")
class Restaurant:
    """A simple attempt to model a restaurant."""
    
    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the type of restaurant"""
        msg= f"{self.name} is a {self.cuisine_type} restaurant."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Simulate opening the restaurant"""
        msg = f"{self.name} is now open for business!"
        print(f"\n{msg}")


# Make three instances representing different restaurants
restaurant = Restaurant('nuovo vesuvio', 'pizza')
restaurant_1 = Restaurant('the krusty krab', 'seafood')
restaurant_2 = Restaurant('los pollos hermanos', 'fried chicken')

# Run the describe_restaurant() method three times
restaurant.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()



############################################################################################################################
# Problem 9.3: This code creates a class called user, with five attributes for
# each user profile. It then creates a method called describe_user()
# that prints a summary of the user's info. It then creates another 
# method called greet_user() that prints a personalized greeting to
# the user. Finally, it creates several instances reprenting different
# users, and calls both methods for each user
print("Problem 9.3")
class User: # Define the class
    """A simple attempt to model website users."""

    def __init__(self, first_name, last_name, age, username, city, country):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.username = username
        self.city = city.title()
        self.country = country.title()

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"{self.username}'s profile information:", "\n")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Username: {self.username}")
        print(f"City: {self.city}")
        print(f"Country: {self.country}")
    
    def greet_user(self):
        """Prints a simple greeting to welcome the user."""
        print(f"\nWelcome, {self.username}!")
        print("\n")


# Create several instances representing different users
user_01 = User('john', 'jameson', 25, 'john70', 'paris', 'france')
user_02 = User('jane', 'robinson', 26, 'jane48', 'lucerne', 'switzerland')
user_03 = User('sara', 'thompson', 27, 'sara51', 'kinshasa', 'congo')

# Call both methods for each user
user_01.describe_user()
user_01.greet_user()

user_02.describe_user()
user_02.greet_user()

user_03.describe_user()
user_03.greet_user()



############################################################################################################################
# Problem 9.4: This code builds on the code from problem 9.1.  It creates a number_served
# attribute with a default value of zero. Then it creates an instance called 
# restaurant from this class. Then it prints the number of customers the 
# restaurant has served. Then it changes the value and prints the new number.
# It also creates a method called set_number_served(), which lets you set the
# number of customers that have been served. Then it calls this method with a
# new number and prints the new number. It also adds method called 
# increment_number_served() that lets you increment the number of customers 
# who've been served. Finally, it calls this method with a new number
# and prints the total number of customers
print("Problem 9.4")
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


# Make an instance representing a specific restaurant with
# # of customers served
restaurant = Restaurant('Nuovo Vesuvio', 'pizza')

# Print the number of customers served, change the number
# of customer served and print the new number
print(f"{restaurant.name} has served {restaurant.number_served} customers.")
restaurant.number_served = 1200
print(f"{restaurant.name} has served {restaurant.number_served} customers.")

# Call the set_number_served() method with a new number
# and print the number of customers again
restaurant.set_number_served(1800)
print(f"{restaurant.name} has served {restaurant.number_served} customers.")

# Call the increment_number_served() method with a new
# number to add to the total and print again
restaurant.increment_number_served(127)
print(f"{restaurant.name} has served {restaurant.number_served} customers.")



############################################################################################################################
# Problem 9.5: This code builds on Problem 9.3's code. It adds an attribute called
# login_attempts to the user class. Then it writes a method called
# increment_login_attempts() that increments the value of login
# attempts by 1. Then it adds another method called 
# reset_login_attemts() that resets the value of login_attempts to 0.
# Then it makes an instance of user class and calls the 
# increment_login_attempts() method several times. After printing the
# number of login attempts to ensure the code works, it calls the 
# reset_login_attempts() method to erase all login attempts
print("Problem 9.5")
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


# Create one instance representing one user
user_01 = User('john', 'jameson', 25, 'john70', 'paris', 'france')

# Describe and greet the user
user_01.describe_user()
user_01.greet_user()

# Call the increment_login_attempts() method several times
print("\nMaking three login attempts...")
user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.increment_login_attempts()
print(f"User {user_01.username} has had {user_01.login_attempts} login attempts.")

# Call the reset_login_attempts() method to reset the number of
# login attempts
print(f"\nResetting {user_01.username}'s login attempts...")
user_01.reset_login_attempts()
print(f"{user_01.username}'s current login attempts: {user_01.login_attempts}")



############################################################################################################################
# Problem 9.6: This code builds on the code from problem 9.4. It creates a child
# class ccalled IceCreamStand that inherits the Restaurant class,
# adds an attribute called flavors that stores a list of ice cream
# flavors, writes a method that displays these flavors, creates
# an instance of IceCreamStand, and calls the show_flavors() method 
print("Problem 9.6")

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


ice_cream_stand_01 = IceCreamStand('best natural ice cream stand')
ice_cream_stand_01.flavors = ['vanilla', 'chocolate', 'strawberry', 'cherry', 'pecan']

ice_cream_stand_01.describe_restaurant()
ice_cream_stand_01.show_flavors()



############################################################################################################################
# Problem 9.7: This code uses the code from Problem 9.5 as base, makes a child
# class called Admin that inherits the User class, adds an 
# attribute called privileges, that stores a list of strings,
# such as "can add post, can delete post, can ban user, etc,
# writes a method called show_privileges to this class
# creates an instance of admin and calls the show_privileges()
# method
print("Problem 9.7")
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


class Admin(User):
    """Represents aspects of users, specific to the Admins.""" 

    def __init__(self, first_name, last_name, age, username, city, country):
        """Initialize attributes of the parent class"""
        super().__init__(first_name, last_name, age, username, city, country)
        self.privileges = []

    def show_privileges(self):
        """List the administrator's set of privileges"""
        print("\nThis user has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Create one instance representing one admin
user_04 = Admin('thomas', 'moss', 40, 'thomas60', 'valencia', 'spain')

user_04.privileges = [
    'can add post',
    'can delete post',
    'can ban user', 
    'can restrict user activity'
]

user_04.describe_user()
user_04.show_privileges()



############################################################################################################################
# Problem 9.8: This code uses the code of Problem 9.7 as base.
# It creates a separate class called Privileges, adds the
# attribute privileges, that stores a list of strings, and 
# moves the show_privileges() method to this class. It also
# makes two instances of two admin users, one with and one
# without privileges. Finally, it describes and lists 
# both profiles and their privileges.
print("Problem 9.8")
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


# Create two instances representing two users
user_04 = Admin('thomas', 'moss', 40, 'thomas60', 'valencia', 'spain')
user_05 = Admin('lara', 'smith', 28, 'lara14', 'woodlands', 'singapore')

user_05_privileges = [
    'can add post',
    'can delete post',
    'can ban user', 
    'can restrict user activity'
]

user_05.privileges.privileges = user_05_privileges

user_04.describe_user()
user_04.privileges.show_privileges()
print("\n")
user_05.describe_user()
user_05.privileges.show_privileges()



############################################################################################################################
# Problem 9.9: This code uses the code from electri_car.py as base.
# It adds a method to the battery class called upgrade_battery().
# This method should check the battery size and set the capacity to
# 100 if it isn't already 100. It makes an electric car with a 
# default battery size, calls the get_range() method once, and then
# calls the get_range() method a second time after upgrading the
# battery, showing an increase in the car's range
print("Problem 9.9")

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage>= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""        
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        msg = f"This vehicle can go  for about {range}"
        msg += " miles on one full charge."
        print(msg)

    def updgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 75:
            self.battery_size = 100
            print("The battery has been upgraded to 100 kWh.")
        else:
            print("the batter has already been upgraded.")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year): #this is the info required for the parent class
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()


# Create a new instance of an electric car and check its range
my_ev = ElectricCar('chevrolet', 'bolt', 2023)
print(my_ev.get_descriptive_name())
my_ev.battery.get_range()

# Upgrade the battery and see the new range
my_ev.battery.updgrade_battery()
my_ev.battery.get_range()



############################################################################################################################
# Problem 9.10: This code uses the code from Problem 9.6 as base.
# It stores the Restaurant class in a module called restaurant.py, 
# makes a separate file called new_restaurant.py that imports 
# restaurant.py. Finally, it makes a new restaurant instance
# and calls one of restaurant.py's methods to show that the 
# import statement is working properly. Please look at the 
# attached files on this folder
print("Problem 9.10")



############################################################################################################################
# Problem 9.11: This code uses the code from Problem 9.8 as base.
# It creates a file called user_classes.py to store the classes
# User, Privilege, and Admin on one module. It also creates a 
# separate file called new_user.py that imports Admin, creates
# a new Admin instance, and calls the show_privileges() method
# to show that the import statement is working properly. Please
# look at the attached files on this folder
print("Problem 9.11")



############################################################################################################################
# Problem 9.12: This code uses the code from Problem 9.8 as base.
# It stores the User class on a module called user.py, stores the 
# Privilege and Admin classes on a separate module called
# adminprivileges.py, and creates a file called new_user_02.py. 
# Finally, it makes a new Admin instance and calls the 
# show_privileges() method to show that all import statements are
# working correctly. Please look at the attached files on this folder
print("Problem 9.12")



############################################################################################################################
# Problem 9.13: This code creates a class called Die with one
# attribute called sides that has a default value of 6. It also
# creates a method called roll_die() that prints a random 
# number between 1 and the number of sides the die has. Then it
# makes a 6-sided die, a 10-sided die, and a 20-sided die and
# roll them 10 times, printing their results
print("Problem 9.13")

from random import randint

class Die:
    """A simple attempt to represent a 6-sided dice."""
    
    def __init__(self, sides=6):
        self.sides =sides
    
    def roll_dice(self):
        """Return a value from one to six."""
        return randint(1, self.sides)

# Make an 6-sided dice, roll it 10 times

sixdice = Die() # make the dice

results = [] # store the results
for roll_num in range(10): # for each individual roll in 10 rolls
    result = sixdice.roll_dice() # call the roll_dice method
    results.append(result) # save the result on the results list

print("These are the results of rolling a 6-sided dice 10 times:")
print(results) # print the results list
print("\n")
# Make a 10-sided dice, roll it 10 times

tendice = Die(sides=10) #make the dice

results = [] # store the results
for roll_num in range(10):
    result = tendice.roll_dice()
    results.append(result)

print("These are the results of rolling a 10-sided dice 10 times:")
print(results)
print("\n")

# Make a 10-sided dice, roll it 10 times

twentydice = Die(sides=20)

results = []
for roll_num in range(10):
    result = twentydice.roll_dice()
    results.append(result)

print("These are the results of rolling a 20-sided dice 10 times:")
print(results)



############################################################################################################################
# Problem 9.14: This code makes a list containing a series of
# 10 numbers and five letters. Then it createsa while-loop to
# randomly select 4 numbers or letters from the list and
# prevents pulling the same number or letter twice. Finally, 
# it prints a message saying that any ticket matching these
# four numbers or letters wins a prize
print("Problem 9.14")
from random import choice

# make a list of the possible 10 numbers and 5 letters
possibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'e', 'i', 'o', 'u']

# make an empty list that will hold the winning alphanumeric combination
winning_combo = []
print("Today's lucky combination is: \n")

# make a while-loop that chooses
while len(winning_combo) < 4:
    pulled_object = choice(possibilities)
    if pulled_object not in winning_combo:
        print(f"{pulled_object}!")
        winning_combo.append(pulled_object)

print(f"\nIf you have a ticket with {winning_combo}, you win a prize!")



############################################################################################################################
# Problem 9.15: This code uses the code from Problem 9.14 as base.
# It makes a list called my_ticket, makes a loop that keeps
# pulling numbers until your combination wins. Finally, it prints
# a message reporting how many times the loop had to run to give
# a winning combination.
print("Problem 9.15")
from random import choice

def get_winning_combo(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_combo = []

    while len(winning_combo) < 4:
        pulled_object = choice(possibilities)
        if pulled_object not in winning_combo:
            winning_combo.append(pulled_object)
    
    return winning_combo


def check_combo(played_combo, winning_combo):
    """Check all elements in the played ticket"""
    for element in played_combo:
        if element not in winning_combo:
            return False
    
    return True


def make_random_combo(possibilities):
    """Return a random combo from a set of possibilities"""
    combo = []
    while len(combo) < 4:
        pulled_object = choice(possibilities)
        if pulled_object not in combo:
            combo.append(pulled_object)
    
    return combo


possibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'e', 'i', 'o', 'u']
winning_combo = get_winning_combo(possibilities)

times = 0
won = False
max_tries = 1_000_000 # Set a max to keep program from getting stuck

while not won:
    new_combo = make_random_combo(possibilities)
    won = check_combo(new_combo, winning_combo)
    times += 1
    if times >= max_tries:
        break

if won:
    print("We have a winner!")
    print(f"Your combination is: {new_combo}.")
    print(f"The winning combination is: {winning_combo}.")
    print(f"It took {times} different pulls to win.")
else:
    print("You didn't win!")
    print(f"Your combination is: {new_combo}.")
    print(f"The winning combination is: {winning_combo}.")
    print(f"You have pulled over {times} total times.")