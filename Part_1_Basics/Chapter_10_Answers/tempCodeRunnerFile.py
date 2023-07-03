print("Problem 10.12")
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