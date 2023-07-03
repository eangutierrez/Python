#----------------------------------------------#
#-- PYTHON CRASH COURSE CHAPTER 17 EXERCISES --#
#----------------------------------------------#
#   
# -- Author: Tony Gutierrez
# -- Date: 05/21/2023 
# -- Tools used: Python, VS Code

# These are the answers to the Chapter 17 exercises on Python Crash Course, 2nd Edition by Eric Matthes

# Problem 17.1: This problem asks to create a file called
# learning_python.txt, which contains three sentences about Python.
# It also asks to create a program (called learning_python.py) that
# reads the file and prints what you wrote 3 times, once by reading
# the entire file, once by looping over the lines in the file, and 
# once by storing the lines in a list and then working with them 
# outside the with block
print("Problem 17.1")




############################################################################################################################
# Problem 17.2: This code builds on the code from Problem 17.1
# It reads the contents of the file learning_python.txt, 
# uses the replace() method to replaces the word 'Python' with 
# the word 'C,' and prints each modified line of text
print("Problem 17.2")

filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Python', 'C'))


############################################################################################################################
# Problem 17.3: This code asks the user for their name and 
# writes the user's response to a file called guest.txt
print("Problem 17.3")
name = input("What's your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(f"{name.title()}")



############################################################################################################################
# Problem 17.4: This code builds on the code form Problem 17.3.
# It asks the user to input their name, adds a line record to
# a file called guest_book.txt, and continues to take names
# until the user enters the word 'quit'
print("Problem 17.4")
filename = 'guest_book.txt'

print("Enter the word 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name?" )
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"Hi {name.title()}, you've been added to the guest book!")


############################################################################################################################
# Problem 17.5: This code creates a while loop that asks people
# why they like programming. Each time someone enters a reason,
# their response is added to the programming_poll.txt file
print("Problem 17.5")
filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else answer the question? (yes/no) ")
    if continue_poll == 'no':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")    


############################################################################################################################
# Problem 17.6: This code creates a program that receives users'
# input. It takes in two numbers and adds them together.  If the
# user inputs non-numeric characters in one of the two numbers, 
# the program lets the user know that it needs two numbers

print("Problem 17.6")
try:
    a = input("Give me a number to add: ")
    a = int(a)

    b = input("Give me a nother number to add: ")
    b = int(b)
except ValueError:
    print("You provided something that is not a number. Please provide a number")
else:
    answer = a + b
    print(f"\nThe sum of {a} and {b} is {answer}!")



############################################################################################################################
# Problem 17.7: This code takes the code from Problem 17.6 as base.
# It adds a while loop to keep the program running, even if the
# user provides non-numeric characters
print("Problem 17.7")
print("Give me two numbers, and I'll add them.")
print("Enter the letter 'q' to quit.")

while True:
    first_number = input("\n First number:")
    if first_number == 'q':
        break
    second_number = input("\n Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You provided something that is not a number. Please provide a number")
    else:
        print(f"\nThe sum of {first_number} and {second_number} is {answer}!")



############################################################################################################################
# Problem 17.8: This code creates a program that reads
# the contents of two files, cats.txt and dogs.txt, 
# and prints the contents of those files. It also 
# uses a try-except block to let users know whenever a
# file is missing
print("Problem 17.8")
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading the contents of {filename}...")
    print(f"Printing the contents of {filename}:")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")



############################################################################################################################
# Problem 17.9: This code uses the code from Problem 17.8 as base.
# It uses a pass statement to let the program silently fail
print("Problem 17.9")
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
            print(f"\nReading the contents of {filename}...")
            print(f"Printing the contents of {filename}:")
            print(contents)



############################################################################################################################
# Problem 17.10: This code creates program that counts how
# many times a particular word appears in a file.
print("Problem 17.10")
def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)

        msg = f"In {filename}, the word '{word}' appears about {word_count} times."
        print(msg)

filename = 'alice.txt'
count_common_words(filename, 'the')
count_common_words(filename, 'the ')


############################################################################################################################
# Problem 17.11: This problem asks to create two programs,
# one that asks users for a favorite number and stores it,
# and one that reads the value and prints the favorite number
# Please look at record_favorite_number.py and 
# read_favorite_number.py to see the results
print("Problem 17.11")



############################################################################################################################
# Problem 17.12: This code combines the two programs from Problem
# 17.11, and adds extra functionality. If the user's number is
# already stored, then it reports the number. Otherwise, it
# asks the new user for their favorite number
print("Problem 17.12")
import json

try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)
    print("Thank you! I will make sure to remember it.")
else:
    print(f"I know your favorite number! It's {number}.")



############################################################################################################################
# Problem 17.13: This code creates a list of Japanese mountains and performs the functions used in this chapter once
print("Problem 17.13")