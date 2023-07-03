import json

number = input("What is your favorite number? ")

with open('favorite_number.json', 'w') as f:
    json.dump(number, f)
    print("Thank you! I will make sure to remember it.")