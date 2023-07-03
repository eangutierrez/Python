#---------------------------------------------#
#-- PYTHON CRASH COURSE CHAPTER 6 EXERCISES --#
#---------------------------------------------#
#   
# -- Author: Tony Gutierrez
# -- Date: 05/21/2023 
# -- Tools used: Python, VS Code

# These are the answers to the Chapter 6 exercises on Python Crash Course, 2nd Edition by Eric Matthes

# Problem 6.1: This code creates a dictionary with information about person_0, and prints out 
# all the contents of the dictionary
print("Problem 6.1")
person_0 = {
    'first_name': 'elvis',
    'last_name': 'presley',
    'age': 40,
    'city': 'memphis',
}

print(f"This is all the information about person_0:")
print(person_0['first_name'])
print(person_0['last_name'])
print(person_0['age'])
print(person_0['city'])



############################################################################################################################
# Problem 6.2: This code creates a dictionary with my friends and their favorite numbers
# and runs a for loop in a list of the dictionary's key-value tuple pairs
# created using the items() method to print out the key and the value
print("Problem 6.2")
favorite_numbers = {
    "Bernard": 22,
    "Cesar": 7,
    "Art": 6,
    "Sean": 23,
    "Fry": 11
}

print("This is a list of my friends' favorite numbers:")
for keys, values in favorite_numbers.items():
    print(f"{keys.title()}'s favorite number is: {values}")



############################################################################################################################
# Problem 6.3: This code creates a dictionary of five Python-related terms and their 
# definitions.  Then we create the variable entry, which equals a key in
# the dictionary.  Then we create an fstring that calls the string
# andthe glossary's definition by calling the variable as the key
print("Problem 6.3")
glossary = {
    'string': 'A series of alphanumeric characters.',
    'comment': 'A note in a program that explains the code.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }
print("This is a glossary of five different words I have learned thanks to this book:")

entry = 'string'
print(f"\n{entry.title()}: {glossary[entry]}")
entry = 'comment'
print(f"\n{entry.title()}: {glossary[entry]}")
entry = 'list'
print(f"\n{entry.title()}: {glossary[entry]}")
entry = 'loop'
print(f"\n{entry.title()}: {glossary[entry]}")
entry = 'dictionary'
print(f"\n{entry.title()}: {glossary[entry]}")



############################################################################################################################
# Problem 6.4: This code creates a guest list and writes a message to each person inviting them to dinner
print("Problem 6.4")
glossary = {
    'string': 'A series of alphanumeric characters.',
    'comment': 'A note in a program that explains the code.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The name that will pinpoint specific data.',
    'value': 'The specific data that is pinpointed by a key.',
    'conditional test': 'test to see if code meets specific conditions.',
    'float': 'A number with a decimal.',
    'boolean expression': 'An expression that evaluates to either True or False.',
    }
print("This is a glossary of five different words I have learned thanks to this book:")

for k, v in glossary.items():
    print(f"\n{k.title()}: {v}")



############################################################################################################################
# Problem 6.5: This code creates a dictionary of countries and rivers in those countries.
# Then it creates a for loop that runs through and prints the keys and values
# in the dictionary. Then it creates a for loop that runs through and prints
# only the keys in the dictionary. Finally, it creates a for loop that runs 
# through and prints all the values in the dictionary
print("Problem 6.5")
rivers = {
    'nile': 'egypt',
    'red river': 'united states',
    'yangtze': 'china',
}
print("These are the statements with the keys and values in my dictionary:")
for k, v in rivers.items():
    print(f"The {k.title()} runs through {v.title()}.")

print("\nThese are the keys in my dictionary:")
for k in rivers.keys():
    print(f"{k.title()}")

print("\nThese are the values in my dictionary:")
for v in rivers.values():
    print(f"{v.title()}")



############################################################################################################################
# Problem 6.6: This code creates a dictionary of people and their favorite languages.
# It also creates a list of five people, some whose names are inside
# the dictionary.  Finally, it runs a for loop with if statements to
# thank those who have taken the poll, or ask people to participate in
# the poll
print("Problem 6.6")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_candidates = ['phil', 'kim', 'johnny', 'sarah', 'amy']

for name in poll_candidates:
    if name in favorite_languages:
        print(f"Thank you for taking the poll, {name.title()}!")
    else:
        print(f"Please take our favorite languages poll, {name.title()}.")



############################################################################################################################
# Problem 6.7: This code uses the code in Problem 6.1, adds 2 new dictonaries representing 
# two different people, makes a list that stores the three dictionaries,
# and runs a for loop to print out the person and the information on the list
print("Problem 6.7")
# Create three different people in their respective dictionaries
person_0 = {
    'first_name': 'elvis',
    'last_name': 'presley',
    'age': 40,
    'city': 'memphis',
}

person_1 = {
    'first_name': 'james',
    'last_name': 'worthy',
    'age': 60,
    'city': 'los angeles',
}

person_2 = {
    'first_name': 'david',
    'last_name': 'robinson',
    'age': 50,
    'city': 'san antonio',
}

# Make a list with the three dictionaries inside
people = [person_0, person_1, person_2]

# Create a for loop.  Inside that for loop, create three new variables, name
# (which contains the first and last name properly capitalized), age, and city
# (properly capitalized)
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = f"{person['age']}"
    city = f"{person['city'].title()}"

# With the proper variables created, we have simplified the print statement
# and ask to print the name, the city, and the age of each person. Because
# the print statement is inside the for loop, all the people will be printed 
    print(f"{name}, of {city}, is {age} years old.")



############################################################################################################################
# Problem 6.8: This code creates an empty list called pets. Then it makes several 
# dictionaries representing a different pet and it's information. Then it 
# adds these dictionaries to the empty list.  Then it runs a for loop
# to display all the keys and values of each pet dictionary in the list
print("Problem 6.8")
# Make an empty list
pets = []

# Create 3 different dictionaries and add them to the list
pet_to_add = {
    'animal type': 'python',
    'name': 'snakey',
    'owner': 'john',
    'weight': 43,
    'food': 'bugs',
}
pets.append(pet_to_add)

pet_to_add = {
    'animal type': 'cat',
    'name': 'simba',
    'owner': 'jane',
    'weight': 20,
    'food': 'fish',
}
pets.append(pet_to_add)

pet_to_add = {
    'animal type': 'dog',
    'name': 'spike',
    'owner': 'julia',
    'weight': 23,
    'food': 'steak',
}
pets.append(pet_to_add)

# Run a for loop that display's each pet's information
for pet in pets:
    print(f"{pet['name'].title()}'s Information:")

# Run another for loop that points to the keys and variables 
# for each pet
    for k, v in pet.items():
# Print each dictionary's keys and values
        print(f"\t{k.title()}: {v}")



############################################################################################################################
# Problem 6.9: This code creates a dictionary that contains 3 people and their favorite
# places to visit.  It then runs several for loops to list each person
# and their favorite destinations 
print("Problem 6.9")
# Make a dictionary called facorite places, add names as keys and 
# destinations as lists
favorite_places = {
    'john': ['maldives', 'austin', 'oklahoma city'],
    'ema': ['hong kong', 'london', 'chiang mai'],
    'ellen': ['milano', 'seoul', 'santo domingo'],
}
# Create a for loop that uses the variable name for the key, places as the
# variable for the lists
for name ,places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
# Create another for loop that uses the variable place for each individual
# place in places and prints each place
    for place in places:
        print(f"\t- {place.title()}")



############################################################################################################################
# Problem 6.10: This code uses the code in Problem 6.2, changes the dictionary so that
# each person can have a list of multiple numbers, and prints each 
# person's name along with their favorite numbers
print("Problem 6.10")
favorite_numbers = {
    "Bernard": [22, 15, 7, 9, 1000],
    "Cesar": [388779, 350639, 577907, 400193, 793315],
    "Art": [82543, 348712, 996300, 470967, 682277],
    "Sean": [647511, 752884, 731294, 967900, 223346],
    "Fry": [82543, 348712, 996300, 470967, 68227722],
}

print("This is a list of my friends' favorite numbers:")
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t- {number}")



############################################################################################################################
# Problem 6.11: This code creates a dictionary called cities, with the names of three
# cities as keys, and three different dictionaries as values. Each 
# dictionary contains different facts about each city.  Finally, it 
# uses for loops to print each city and its facts
print("Problem 6.11")
# Create a dictionary called city, with city names as keys and 
# dictionaries as values
cities = {
    'san antonio': {
        'country': 'united states',
        'population': 1_434_625,
        'fact': 'Home of The Spurs',
    },
    'austin': {
        'country': 'united states',
        'population': 964_177,
        'fact': 'Home of The Longhorns', 
    },
    'houston': {
        'country': 'united states',
        'population': 2_301_572,
        'fact': 'Home of The Rockets',
    },
}

# For loop that creates the variables name and city_info
for name, city_info in cities.items():
    print(f"\nFacts about {name.title()}:")

# Create the variables country, population, and fact, that 
# extract their value from each individual dictionary    
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

# Print each city's individual facts
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")



############################################################################################################################
# Problem 6.12: This code creates a dictionary of all the enemies in stage 1, with
# the names of three types of enemies as keys, and several enemy
# facts as values. Finally, it uses for loops to print each 
# type of Stage 1 Enemy and its stats
print("Problem 6.12")
stage_1_enemies = {
    'normal alien': {
        'color': 'green',
        'attack': 10,
        'special attack': 5,
        'defense': 10,
        'special defense': 5,
        'speed': 20,
        'hit points': 50
    },
    'miniboss alien': {
        'color': 'yellow',
        'attack': 20,
        'special attack': 25,
        'defense': 30,
        'special defense': 40,
        'speed': 35,
        'hit points': 100
    },
    'boss alien': {
        'color': 'red',
        'attack': 40,
        'special attack': 50,
        'defense': 50,
        'special defense': 50,
        'speed': 40,
        'hit points': 300
    },
}

# For loop that creates the variables name and city_info
print("Facts about Stage 1 Enemies:")
for name, alien_stats in stage_1_enemies.items():
    print(f"\n{name.title()} Enemy Stats:")

# Create the variables country, population, and fact, that 
# extract their value from each individual dictionary    
    color = alien_stats['color']
    attack = alien_stats['attack']
    sattack = alien_stats['special attack']
    defense = alien_stats['defense']
    sdefense = alien_stats['special defense']
    speed = alien_stats['speed']
    hp = alien_stats['hit points']  

# Print each city's individual facts
    print(f"\tColor: {color.title()}")
    print(f"\tAttack: {attack}")
    print(f"\tSpecial Attack: {sattack}")
    print(f"\tDefense: {defense}")
    print(f"\tSpecial Defense: {sdefense}")
    print(f"\tSpeed: {speed}")
    print(f"\tHit Points: {hp}")