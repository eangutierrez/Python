#---------------------------------------------#
#-- PYTHON CRASH COURSE CHAPTER 7 EXERCISES --#
#---------------------------------------------#
#   
# -- Author: Tony Gutierrez
# -- Date: 05/21/2023 
# -- Tools used: Python, VS Code

# These are the answers to the Chapter 7 exercises on Python Crash Course, 2nd Edition by Eric Matthes

# Problem 7.1 This code acts like a rental car clerk asks the user to input the 
# type of car that they need, and it will respond with an fstring 
# of their response
print("Problem 7.1")
car = input("What type of car do you need? ")
print(f"\nLet's see if I can find you a {car.title()}.")



############################################################################################################################
# Problem 7.2 This code acts like a restaurant greeter and asks for the number of 
# members in the party, and it will use an if statement to respond 
print("Problem 7.2")
number_of_guests = input("How many people are in your party? ")
number_of_guests = int(number_of_guests)

if number_of_guests > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready!")



############################################################################################################################
# Problem 7.3: This code asks the user to provide a number, and it will use modular
# division to find out if the number is a multiple of 10 
print("Problem 7.3")
number = input("Enter a number and I will tell you if it's a multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
    print("\nThe number is a multiple of 10!")
else:
    print("\nThe number is not a multiple of 10.")



############################################################################################################################
# Problem 7.4: This code creates a prompt that acts as a pizza restaurant clerk. 
# It asks people to input toppings for their pizza, and to input
# the word 'quit' when finished.  Finally, it uses a while loop
# and if statement to either print the topping they want on their
# pizza or break the loop
print("Problem 7.4")
prompt = "\nPlease enter one pizza topping to add to your pizza:"
prompt += "\n(Enter the word 'quit' when you are finished.)"

while True:
    topping = input(prompt)
    
    if topping != 'quit':
        print(f"Adding {topping} to your pizza.")
    else:
        break



############################################################################################################################
# Problem 7.5: This code asks the user for their age and charges them a
# different entrance fee depending on their age
print("Problem 7.5")
prompt = "\nWelcome to Python Movie Theather. What is your age?"
prompt += "\n(Enter the word 'quit' when you are finished.)"
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        price = 0
    elif (age >= 3) and (age < 13):
        price = 10
    else:
        price = 15
    
    print(f"\nYour price of admission is ${price}.")



############################################################################################################################
# Problem 7.6: This problem asks to rewrite Problem 7.4 or 7.5 to use, a conditional
# test in the while statement for the loop to stop, an active variable
# to control how long the loop runs, and a break statement to exit the
# loop when the user enters a quit value. For practice purposes, I have 
# rewritten both of my answers above to meet these specifications
print("Problem 7.6")



############################################################################################################################
# Problem 7.7: This code creates an infinite loop.  I have commented it out to avoid 
# any performance issues
# print("Problem 7.7")
# x = 1
# while x <= 20:
#     print(x)
#     x += 1 # The absence of this line creates an infinite loop because
#     # the value of x does not increase, thus never breaking the loop



############################################################################################################################
# Problem 7.8: This code creates a list called sandwich orders with five sandwiches,
# an empty list called finished sandwiches, a while loop that confirms 
# each sandwich has been made, moves each object from one list to the other,
# and prints that list as a completed order
print("Problem 7.8")
sandwich_orders = ['tuna', 'blt', 'chicken', 'grilled cheese', 'nutella']
finished_sandwiches = []

# Verify that each sandwich has been made to order and move each verified
# sandwich to the finished sandwiches list
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made a {current_sandwich.title()} Sandwich!")
    finished_sandwiches.append(current_sandwich)

# Print out the list of all the sandwiches in the order
print("\nThe following order is complete:\n")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()} Sandwich")



############################################################################################################################
# Problem 7.9: This code builds on the previous problem.  It adds pastrami several times
# on the list, adds a message stating that the deli has run out of pastrami,
# runs a while loop to remove all the pastrami orders, and runs the rest of 
# Problem 7.8's code
print("Problem 7.9")
sandwich_orders = ['tuna', 'pastrami', 'chicken', 'grilled cheese', 'pastrami', 'blt', 'pastrami', 'pastrami', 'nutella']
finished_sandwiches = []

# Verify that there are no pastrami orders, remove all pastrami orders with
# a while loop, and move all sandwich orders to the finished sandwiches 
# list
print(f"We have run out of {sandwich_orders[1]} for the day!")
print("\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made a {current_sandwich.title()} Sandwich!")
    finished_sandwiches.append(current_sandwich)

# Display all confirmed users
print("The following order is complete:")
print("\n")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()} Sandwich")



############################################################################################################################
# Problem 7.10: This code creates three prompts to carry out a poll, an empty dictionary to store responses, 
# a while loop that stores customer names and responses, and prints out the results
print("Problem 7.10")
# Prompt for the person's name and response
name_prompt = "\nWhat is your name? "
question_prompt = "If you could visit one place in the world, where would you go "
continue_prompt = "\nWould you like to let someone else respond? (yes/ no) "
                     
# Store the responses in the dictionary
responses = {}

#Ask users:
while True:
    name = input(name_prompt)
    response = input(question_prompt)

    # Save response
    responses[name] = response

    # Ask to continue
    to_continue = input(continue_prompt)
    if to_continue == 'no':
        break

# Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()}'s dream vacation is visiting {response.title()}.")