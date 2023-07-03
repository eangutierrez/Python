print("Problem 9.13")

from random import randint

class Die:
    """A simple attempt to represent a 6-sided dice."""
    
    def __init__(self, sides=6):
        self.sides =sides
    
    def roll_dice(self):
        """Return a value from one to six."""
        return randint(1, self.sides)

# Make an 6-sided dice, roll it 10 times

sixdice = Die() # make the dice

results = [] # store the results
for roll_num in range(10): # for each individual roll in 10 rolls
    result = sixdice.roll_dice() # call the roll_dice method
    results.append(result) # save the result on the results list

print("These are the results of rolling a 6-sided dice 10 times:")
print(results) # print the results list
print("\n")
# Make a 10-sided dice, roll it 10 times

tendice = Die(sides=10) #make the dice

results = [] # store the results
for roll_num in range(10):
    result = tendice.roll_dice()
    results.append(result)

print("These are the results of rolling a 10-sided dice 10 times:")
print(results)
print("\n")

# Make a 10-sided dice, roll it 10 times

twentydice = Die(sides=20)

results = []
for roll_num in range(10):
    result = twentydice.roll_dice()
    results.append(result)

print("These are the results of rolling a 20-sided dice 10 times:")
print(results)