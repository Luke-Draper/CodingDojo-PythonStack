# Create beCheerful(). Within it, print string "good morning!" 98 times.
def beCheerful():
	print("good morning!"*98)
# beCheerful()

import random
import math
def randInt(min=0, max=100): # Min and Max are inclusive
	return int(math.floor(random.random()*((max+1)-min)+min))

print(randInt()) # returns a random integer between 0 to 100
print(randInt(max=50)) # returns a random integer between 0 to 50
print(randInt(min=50)) # returns a random integer between 50 to 100
print(randInt(min=50, max=500)) # returns a random integer between 50 and 500
