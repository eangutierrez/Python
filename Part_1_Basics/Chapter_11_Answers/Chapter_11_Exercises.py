#----------------------------------------------#
#-- PYTHON CRASH COURSE CHAPTER 11 EXERCISES --#
#----------------------------------------------#
#   
# -- Author: Tony Gutierrez
# -- Date: 05/21/2023 
# -- Tools used: Python, VS Code

# These are the answers to the Chapter 11 exercises on Python Crash Course, 2nd Edition by Eric Matthes

# Problem 11.1: This code creates a a function called 
# city_functions.py that accepts two parameters: a city name and
# a country name. The function returns a single string of the
# form City, Country, such as Santiago, Chile. It also creates
# a file called test_cities.py that tests the city_functions.py 
# by importing the unittest module city_functions.py. Finally,  
# it writes a method called test_city_country() to verify that
# calling the function with values such as 'santiago' and 'chile'
# results in the correct string. Please look at the files mentioned
# above and run test_cities.py to make sure the test_city_country()
# passes.
print("Problem 11.1")



############################################################################################################################
# Problem 11.2: This code builds on the code from Problem 11.1.
# It modifies the function so it requires a third parameter, 
# population. It now returns a single string of the form 
# City, Country: population ####, such as 
# Santiago, Chile – population 5000000. Run test_cities.py
# again and make sure test_city_country() fails this time.
# Then it modifies the function so the population parameter
# is optional. Then it runs test_cities.py again to ensure
# that test_city_country() passes again. Then it writes a
# second test called test_city_country_population(), that
# verifies you can call your function with the values
# 'santiago', 'chile', and 'population=5000000'. Please find
# the files modified_city_functions.py, 
# modified_test_cities.py, and run the test to ensure
# the new test passes.
print("Problem 11.2")



############################################################################################################################
# Problem 11.3: This code creates a class called Employee.
# The __init__() method takes in a first name, a last name,
# and an annual salary, and store each of these as attributes. 
# It also creates a method called give_raise() that adds $5,000
# to the annual salary by default, but also accepts a different
# raise amount. Then it writes a test case for Employee, with 
# two test methods, test_give_default_raise() and 
# test_give_custom_raise(). The setUp() method is used so you
# don’t have to create a new employee instance in each test method. 
# Please look at the files employee.py and test_employee.py
# to run the test case, and make sure both tests pass.
print("Problem 11.3")