#---------------------------------------------#
#-- PYTHON CRASH COURSE CHAPTER 2 EXERCISES --#
#---------------------------------------------#
#   
# -- Author: Tony Gutierrez
# -- Date: 05/21/2023 
# -- Tools used: Python, VS Code

# These are the answers to the Chapter 2 exercises on Python Crash Course, 2nd Edition by Eric Matthes

# Problem 2.1: This code assigns a message to a variable
# and prints that message
print("Problem 2.1")
message = "Hello wonderful people!" 
print(message)



############################################################################################################################
# Problem 2.2: This code assigns a message to a variable, 
# prints that message, assigns a new message to the same
# variable, and prints that message
print("Problem 2.2")
message = "Hello wonderful people!" 
print(message)

message = "Let's learn some Python today :)"
print(message)



############################################################################################################################
# Problem 2.3: This code assigns a name to a variable
# and prints it using an f-string
print("Problem 2.3")
name = "tony"
print(f"Hello, {name.title()}! Would you like to learn some Python today?")



############################################################################################################################
# Problem 2.4: This code assigns a name to a variable,
# and prints it three times, one in lower case, one in
# upper case, and one in title case.4
print("Problem 2.4")
name = "tony"
print(name.lower())
print(name.upper())
print(name.title())



############################################################################################################################
# Problem 2.5: This code assigns a name to a variable 
# and prints a famous quote by that person using an 
# f-string
print("Problem 2.5")
name = "albert einstein"
print(f"{name.title()} once said: 'A person who never made a mistake never tried anything new.'")



############################################################################################################################
# Problem 2.6: This code assigns a name to a variable, 
# a quote from that person to another variable, and 
# prints that name and quote
print("Problem 2.6")
famous_person = "albert einstein"
message = "once said: 'A person who never made a mistake never tried anything new.'"
print(famous_person.title(), message)



############################################################################################################################
# Problem 2.7: This code assigns a name to a variable 
# with extra space and prints it three times, with a 
# left trim, a right trim, and double trim
print("Problem 2.7")
name = "\tTony Gutierrez \n"
print("Raw Output:")
print(name)

print("\nUsing the lstrip() method:")
print(name.lstrip())

print("\nUsing the rstrip() method:")
print(name.rstrip())

print("\nUsing the strip() method:")
print(name.strip())



############################################################################################################################
# Problem 2.8: This code prints a sum, difference, product, 
# and a quotient which gives the number eight as a result
print("Problem 2.8")
print(7 + 1)
print(14 - 6)
print(4 * 2)
print(80 / 10)



############################################################################################################################
# Problem 2.9: This code assigns my favorite number to a 
# variable, and prints a message with that variable using
# an f-string
print("Problem 2.9")
favorite_number = "12"
message = f"My favorite number is {favorite_number}"
print(message)



############################################################################################################################
# Problem 2.10: This problem asked to show proper comment 
# practices on this exercise
print("Problem 2.10")



############################################################################################################################
# Problem 2.11: This code imports The Zen of Python by Tim Peters
print("Problem 2.11")
import this