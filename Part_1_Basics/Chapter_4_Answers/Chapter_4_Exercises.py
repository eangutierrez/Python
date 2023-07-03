#---------------------------------------------#
#-- PYTHON CRASH COURSE CHAPTER 4 EXERCISES --#
#---------------------------------------------#
#   
# -- Author: Tony Gutierrez
# -- Date: 05/21/2023 
# -- Tools used: Python, VS Code

# These are the answers to the Chapter 4 exercises on Python Crash Course, 2nd Edition by Eric Matthes

# Problem 4.1: This code creates a list of three of my favorite 
# pizzas, runs a for loop to print out each of my 
# favorite pizzas, and gives a statement outside of my for loop
print("Problem 4.1")
fav_pizzas = ['extra pepperoni', 'cheese and thin crust', 'supreme']
for pizza in fav_pizzas:
    print(f"I like {pizza} pizza.")
print("\nMy favorite food is pizza!")



############################################################################################################################
# Problem 4.2: This code creates a list of my favorite animals, 
# runs a for loop to print out each of these animals, and
# gives a statement outside of my for loop
print("Problem 4.2")
fav_animals = ['dogs', 'cats', 'rabbits', 'hamsters']
for animal in fav_animals:
    print(f"A {animal} would make a great pet.")
print("\nAny of these animals would make a great pet!")



############################################################################################################################
# Problem 4.3: This code creates a forloop to print the numbers from 1 to 20 inclusive
print("Problem 4.3")
for value in range (1, 21):
    print(value)



############################################################################################################################
# Problem 4.4: This code creates a list from one to one million, and then counts the
# numbers from one to a million.  The answer is commented out to avoid
# performance errors
print("Problem 4.4")
# numbers = list(range(1, 1_000_001))
# for value in range (1, 1_000_001):
#    print(value)



############################################################################################################################
# Problem 4.5: This code creates a list from one to one million, and then uses 
# the functions min(), max(), and sum() on the list
print("Problem 4.5")
numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))



############################################################################################################################
# Problem 4.6: This code creates a list of all odd numbers from 1 to 20 and uses a 
# for loop to prints the objects in that list
print("Problem 4.6")
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)



############################################################################################################################
# Problem 4.7: This code creates a list of the multiples of three from 3 to 30, and uses a for loop 
# to print those numbers 
print("Problem 4.7")
mult_3 = list(range(3, 31, 3))
for number in mult_3:
    print(number)



############################################################################################################################
# Problem 4.8: This code creates an empty list, uses a for loop to dynamically add the cubed values
# from the range 1 to 11 to the list, and uses another for loop to print out each 
# individual value of the list 
print("Problem 4.8")
cubes = []
for value in range(1,11):
    cubes.append(value**3)
for cube in cubes:
    print(cube)



############################################################################################################################
# Problem 4.9: This code uses list comprehension to generate a list of the first 10 cubes
print("Problem 4.9")
cubes = [number**3 for number in range(1,11)]
print(cubes)



############################################################################################################################
# Problem 4.10: This code uses list comprehension to generate a list of the first 10 cubes
# Then it prints the first three, middle three, and last three items in the 
# list
print("Problem 4.10")
cubes = [number**3 for number in range(1,11)]
print(cubes)

print("\nThe first three items in the list are:")
print(cubes[:3])
print("\nThe middle three items in the list are:")
print(cubes[3:6])
print("\nThe last three items in the list are:")
print(cubes[-3:])



############################################################################################################################
# Problem 4.11: This code creates a list of my favorite pizzas, copies that list to a list
# called friends_pizzas, adds a different new pizza to each list, and prints
# both lists to confirm 
print("Problem 4.11")
fav_pizzas = ['extra pepperoni', 'cheese and thin crust', 'supreme']
friend_pizzas = fav_pizzas[:]

fav_pizzas.append('veggie')
friend_pizzas.append('bbq chicken')

print("\nMy favorite pizzas are:")
for pizza in fav_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)



############################################################################################################################
# Problem 4.12: This code creates a for loop to print all the objects of the code found in the foods.py document
print("Problem 4.12")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("\nMy favorite foods are")
for food in my_foods:
    print(food)
print("\nMy friend's foods are:")
for food in friend_foods:
    print(food)



############################################################################################################################
# Problem 4.13: This code creates a list of Japanese mountains and performs the functions used in this chapter once
print("Problem 4.13")
print("This is the old menu:")
buffet = ('cupcakes', 'cookies', 'brownies', 'muffins', 'puddings')
for food in buffet:
    print(food)

# buffet[1] = 'ice cream' # This line is commented out because it creates an error

buffet = ('cupcakes', 'cookies', 'brownies', 'pies', 'sweet breads')
print("\nThis is the new menu:")
for food in buffet:
    print(food)