#---------------------------------------------#
#-- PYTHON CRASH COURSE CHAPTER 8 EXERCISES --#
#---------------------------------------------#
#   
# -- Author: Tony Gutierrez
# -- Date: 05/21/2023 
# -- Tools used: Python, VS Code

# These are the answers to the Chapter 8 exercises on Python Crash Course, 2nd Edition by Eric Matthes

# Problem 8.1: This code creates a function called display_message() that prints one
# sentece describing the contents of this chapter
print("Problem 8.1")
#create a function called display_message() that prints one sentece telling everyone that you are liearning about
def display_message():
    """Display a message telling everyone what you are learning"""
    print("This chapter is about creating functions in Python.")
    
display_message()



############################################################################################################################
# Problem 8.2: This code creates a function called favorite_book() that accepts one 
# parameter, title, and prints a message that conveys your favorite book
print("Problem 8.2")
def favorite_book(title):
    """Displays a message that tells everyone one of your favorite book"""
    print(f"One of my favorite books is {title.title()}.")

favorite_book('lord of the rings')



############################################################################################################################
# Problem 8.3: This code creates a function called make_shirt, it takes two arguments:
# tshirt_size and tshirt_message, and prints a sentence summarizing the 
# t-shirt. The function was called twice, once with positional arguments
# and once with keyword arguments
print("Problem 8.3")
def make_shirt(tshirt_size, tshirt_message):
    """Display information about a t-shirt."""
    print(f"\nThe t-shirt's size is: {tshirt_size.upper()}.")
    print(f"The t-shirt's message is: {tshirt_message}.")

make_shirt('xl', 'strawberries')
make_shirt(tshirt_size='m', tshirt_message='Wear Sunscreen')



############################################################################################################################
# Problem 8.4: This code builds on the code from Problem 8.3. It adds default values and
# calls the function three times, first with default values, second with 
# a medium size and default message, and third with any size and a new message
print("Problem 8.4")
def describe_tshirt(tshirt_size='L', tshirt_message='I love Python'):
    """Display information about a t-shirt."""
    print(f"\nThe t-shirt's size is: {tshirt_size.upper()}.")
    print(f"The t-shirt's message is: {tshirt_message}.")

describe_tshirt()
describe_tshirt('m')
describe_tshirt(tshirt_size='s', tshirt_message='Can I have a Donut?')



############################################################################################################################
# Problem 8.5: This code creates a function called describe_city, it takes two
# arguments, city_name and country_name, has a default value in 
# country_name, and calls the function three times, with at least
# 1 not being the default value
print("Problem 8.5")
def describe_city(city_name, country_name='el salvador'):
    """Display information about a city."""
    print(f"\n{city_name.title()} is located in {country_name.title()}.")

describe_city('reykjavik', 'iceland')
describe_city('santa ana')
describe_city('san juan capistrano', 'the united states')



############################################################################################################################
# Problem 8.6: This code creates a function called city_country, that takes two
# arguments, a city name and a country name, and returns them 
# neatly formatted, adds a variable called place three times, 
# each with a different city-country pair, and runs the function
print("Problem 8.6")
def city_country(city_name, country_name):
    """Return the name of a city and country pair, neatly formatted."""
    full_pair = f"{city_name}, {country_name}"
    return full_pair.title()

place = city_country('santiago', 'chile')
print(place)
place = city_country('lima', 'peru')
print(place)
place = city_country('la paz', 'bolivia')
print(place)



############################################################################################################################
# Problem 8.7: This code creates a function called make_album() that takes two parameters, artist name and album title
# and creates a dictionary with those arguments.  Then it creates a
# variable called add_album, which calls the function and adds the
# information of three albums to print these dicitonaries.  Below 
# that, the same code is used but an optional parameter to add
# number of tracks is added, and an if-statement handles  whether
# users add the optional parameter or not.  Finally, the function
# is called three times again to print these dictionaries
print("Problem 8.7")
def make_album(artist_name, album_title):
    """Return a dictionary of information about an album"""
    album = {'Artist Name': artist_name.title(), 'Album Title': album_title.title()}
    return album

add_album = make_album('madvillain', 'madvillainy')
print(add_album)
add_album = make_album('nirvana', 'nevermind')
print(add_album)
add_album = make_album('weezer', 'the blue album')
print(add_album)



def make_album(artist_name, album_title, number_of_songs=0):
    """Return a dictionary of information about an album"""
    album = {'Artist Name': artist_name.title(), 'Album Title': album_title.title()}
    if number_of_songs:
           album['Total Songs'] = number_of_songs
    return album

add_album = make_album('madvillain', 'madvillainy', 22)
print(add_album)
add_album = make_album('nirvana', 'nevermind')
print(add_album)
add_album = make_album('weezer', 'the blue album', 10)
print(add_album)



############################################################################################################################
# Problem 8.8: This code builds on the code of Problem 8.7. It creates a program that
# runs on user input.  It lets users know to enter the word quit to stop
# the program, asks for an artist name, an album name, runs the make_album
# function to build a dictionary with the user's inputs, and prints the
# dictionary
print("Problem 8.8")
def make_album(artist_name, album_title, number_of_songs=0):
    """Return a dictionary of information about an album"""
    album = {'Artist Name': artist_name.title(), 'Album Title': album_title.title()}
    if number_of_songs:
           album['Total Songs'] = number_of_songs
    return album

print("Enter 'quit' at any time to stop.")
artist_prompt= "Who is the artist?"
album_prompt = "What is the album's name?"

while True:
    ar_name = input(artist_prompt)
    if ar_name == 'quit':
        break
    al_name = input("Album Name: ")
    if al_name == 'quit':
        break
    
    ar_al_pair = make_album(ar_name, al_name)
    print(ar_al_pair)
print("\nThank you for participating!")



############################################################################################################################
# Problem 8.9: This code creates a message list and a function called 
# show_messages() that receives a list as an argumetn and prints
# all the messages in that list 
print("Problem 8.9")
message_list = ['Hello', 'How are you?', 'Are you feeling well?', 'Did you watch the football game?']

def show_messages(messages):
    """Show all the messages in a list."""
    for message in messages:
        print(message)

show_messages(message_list)



############################################################################################################################
# Problem 8.10: This code builds on the code from Problem 8.9. It adds a function 
# called send_messages() that prints each text message and moves 
# each message to a new list called sent_messages. Finally, it 
# prints both lists to prove that the messages were moved correctly
print("Problem 8.10")
message_list = ['Hello', 'How are you?', 'Are you feeling well?', 'Did you watch the football game?']
sent_messages = []
def show_messages(messages):
    """Show all the messages in a list."""
    for message in message_list:
        print(message)

def send_messages(message, sent_message):
    """Print all text messages and move them to a list  called sent_messages."""
    while message_list:
        current_message = message_list.pop()
        print(current_message)
        sent_messages.append(current_message)

print("This is the original list:")
show_messages(message_list)

print("\nThis is the the new list:")
send_messages(message_list, sent_messages)

print("\nThese are the original list and the final list prove messages have been moved:")
print(message_list)
print(sent_messages)



############################################################################################################################
# Problem 8.11: This code builds on the code from Problem 8.10. It calls the 
# function send_messages() with a copy of the list of messages
# by using [:]. It prints the original list, the new list, 
# and both lists to  show that the original list has retained
# its content
print("Problem 8.11")
message_list = ['Hello', 'How are you?', 'Are you feeling well?', 'Did you watch the football game?']
sent_messages = []
def show_messages(messages):
    """Show all the messages in a list."""
    for message in message_list:
        print(message)

def send_messages(message_list, sent_messages):
    """Print all text messages and move them to a list  called sent_messages."""
    while message_list:
        current_message = message_list.pop()
        print(current_message)
        sent_messages.append(current_message)

print("This is the original list:")
show_messages(message_list)

print("\nThis is the the new list:")
send_messages(message_list[:], sent_messages)

print("\nThese are the original list and the final list prove that the original list has retained its messages:")
print(message_list)
print(sent_messages)



############################################################################################################################
# Problem 8.12: This code creates a function called make_sandwich, which accepts
# a list of any number of fillings on a sandwich and prints a summary
# of the ingredients in each sandwich.  Finally, it calls the 
# function three times, using a different number of arguments each time
print("Problem 8.12")
def make_sandwich(*fillings):
    """Build a sandwich containing everything inside the sandwich."""
    print("\nMaking a sandwich with the following ingredients:")
    for filling in fillings:
        print(f"- {filling}")
    print("Your sandwich is ready to go!")

make_sandwich('bacon', 'lettuce', 'tomato')
make_sandwich('ham', 'cheese')
make_sandwich('tuna salad')



############################################################################################################################
# Problem 8.13: This code creates a function called build_profile, which takes a series
# of arguments to build a dictionary, and prints that profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about the user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('tony', 'gutierrez',
                             location='austin',
                             field='data science',
                             hobby='watching basketball')
print(user_profile)



############################################################################################################################
# Problem 8.14: This code creates a function that stores info about a car
# in a dictionary. It always receive a manufacturer and a
# model name, and accepts an arbitrary number of keyword arguments
print("Problem 8.14")
def make_car(manufacturer, model, **other_facts):
    """Build a dictionary containing everything we know about a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for other_fact, value in other_facts.items():
        car_dict[other_fact] = value

    return car_dict

old_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(old_car)

new_car = make_car('honda', 'accord', year=1991, color='white', 
                   headlights='popup')
print(new_car)



############################################################################################################################
# Problem 8.15: This asks us to take an example of code that simulates printing
# 3d models and split it into two files: printing_functions.py 
# and printing_models.py and use the import statement to print
# the models. Please refer to the files on this folder for 
# the answer
print("Problem 8.15")