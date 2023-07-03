#---------------------------------------------#
#-- PYTHON CRASH COURSE CHAPTER 5 EXERCISES --#
#---------------------------------------------#
#   
# -- Author: Tony Gutierrez
# -- Date: 05/21/2023 
# -- Tools used: Python, VS Code

# These are the answers to the Chapter 5 exercises on Python Crash Course, 2nd Edition by Eric Matthes

# Problem 5.1: This code creates ten conditional tests, five evaluating for each outcome
print("Problem 5.1")
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car.lower() == 'audi')

num = 22
print("\nIs num >= 5 and num <= 100? I predict True.")
print((num >= 5) and (num <= 100))

print("Is num >= 9999 or num = 22? I predict False.")
print((num >= 9999) and (num == 22))

banned_customers = ['alan', 'christian', 'rebeccah']
user = 'quincy'
print("\nIs user in the banned_customers? I predict False.")
print(user.lower() in banned_customers)

print("Are 'alan' and 'quincy' in banned_customers? I predict False.")
print('alan' in banned_customers and ('quincy' in banned_customers))

answer_1 = -100
answer_2 = 100
print("\nIs answer_1 <= 5 and answer_2 <= 100? I predict True.")
print((answer_1 <= 5) and (answer_2 <= 100))

print("Is answer_1 <= 5 or answer_2 >= 5000? I predict True.")
print((answer_1 <= 5) or (answer_2 >= 5000))

cars = ['audi', 'bmw', 'subaru', 'toyota']
print("\nIs Audi in titlecase in the cars list? I predict False.")
print('Audi' in cars)

print("Is Audi in lowercase in the cars list? I predict True.")
print('audi' in cars)



############################################################################################################################
# Problem 5.2: This code creates additional conditional statements for practice
print("Problem 5.2")
car = 'mustang'
print("\nIs car == 'Mustang'? I predict False.")
print(car == 'Mustang')

print("\nIs car == 'mustang'? I predict True.")
print(car.lower() == 'mustang')
print('\n')

age = 60
if age == 60:
    print("You can rent a room in this retirement community.")
else:
    print("You can't rent a room in this retirement community.")

age = 35
if age >= 35:
    print("\nYou can be president of the United States.")
else:
    print("You can't be president of the United States.")

age = 23
if age >= 22 and age <=60:
    print("\nYou can ride this roller coaster")
else:
    print("You can't ride this roller coaster")

age = 16
if age <= 22 or age >=27:
    print("\nYou can enter this casino.")
else:
    print("You can't enter this casino.")

cats = ['siamese', 'burmese', 'persian']
print('\nburmese' in cats)
print('persian' in cats)
print('bobtail' in cats)

cats = ['khao manee', 'turkish', 'korat']
cat_name = 'snowshoe'
if cat_name not in cats:
    print("\mThis cat is not on the list.")
else:
    print("This cat is on the list.")



############################################################################################################################
# Problem 5.3: This code creates two if statement tests to see if an alien's color is green. 
# If the color is green, the player gets five points
# If the color is not green, there is no output
print("Problem 5.3")
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")



############################################################################################################################
# Problem 5.4: This code adds to the previous problem. The second code block has an
# additional if-else chain that gives the player ten points if the alien
# is not green
print("Problem 5.4")
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")



############################################################################################################################
# Problem 5.5: This code adds to the previous problem. The third code block has an
# if-else chain that gives the player ten points if the alien is yellow,
# and fifteen points if the alien is red
print("Problem 5.5")
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You hust earned 15 points!")



############################################################################################################################
# Problem 5.6: This code creates an if-elif-else chain that determines a person's stage of
# life based on their age
print("Problem 5.6")
age = 23
if age < 2:
    stage = 'baby'
elif (age >= 2) and (age < 4):
    stage = 'toddler'
elif (age >= 4) and (age < 13):
    stage = 'kid'
elif (age >= 13) and (age < 20):
    stage = 'teenager'
elif (age >= 20) and (age < 65):
    stage = 'adult'
else:
    stage = 'elder'
print(f"This person is in the {stage} stage.")



############################################################################################################################
# Problem 5.7: This code creates a list of my favorite fruits, as well as five different if
# statements that test whether certain fruits are in my list of favorites.
# Finally, it prints a message if those fruits are in my list of favorites
print("Problem 5.7")
fav_fruits = ['blueberries', 'raspberries', 'mangos']
if 'bananas' in fav_fruits:
    print("You must realy like bananas!")
if 'mangos' in fav_fruits:
    print("You must realy like mangos!")
if 'raspberries' in fav_fruits:
    print("You must realy like raspberries!")
if 'orange' in fav_fruits:
    print("You must realy like oranges!")
if 'blueberries' in fav_fruits:
    print("You must realy like blueberries!")



############################################################################################################################
# Problem 5.8: This code creates an list of usernames. Then it goes through that list in a 
# for loop to print a greeting.  We also have an if statement that changes the
# change the greeting depending on the user type 
print("Problem 5.8")
usernames = ['admin', 'power_user', 'it_support', 'executive', 'legal']
for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")



############################################################################################################################
# Problem 5.9: This code checks adds to the problem above and checks whether the usernames list
# is empty.  If it contains objects, it runs the for loop.  If it is empty, it will
# print a message that asks for users
print("Problem 5.9")
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")



############################################################################################################################
# Problem 5.10: This code creates a list of five usernames in lowercase, copies that list in
# uppercase, creates another list of five new usernames, and a for loop and if
# statement to check whether a new username is similar to a current username,
# case insenstive
print("Problem 5.10")
current_users = ['tony1', 'tony2', 'tony3', 'tony4', 'tony5']
current_users_upper = [user.upper() for user in current_users]
new_users = ['ToNy5', 'tony6', 'tony7', 'tony8', 'tony9']

for new_user in new_users:
    if new_user.upper() in current_users_upper:
        print(f"The username {new_user} is already taken.  Please choose another username")
    else:
        print(f"The username {new_user} is available.")



############################################################################################################################
# Problem 5.11: This code creates a list of the numbers from one through nine, and uses a
# for loop and an if-elif-else chain to print out the proper ordial number
# endings for each number
print("Problem 5.11")
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')