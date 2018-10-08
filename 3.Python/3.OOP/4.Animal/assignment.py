# Animal Class
# Attributes:
# • name
# • health
# Methods:
# • walk: decreases health by one
# • run: health decreases by five
# • display health: print to the terminal the animal's health.

# Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() to confirm that the health attribute has changed.

class Animal:

	def __init__(self, name, health):
		self.name = name
		self.health = health
	
	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def display_health(self):
		print(self.health)
		return self

a1 = Animal("Jeremy", 45)
a1.walk().walk().walk().run().run().display_health()

# Dog Class
# • inherits everything from Animal
# Attributes:
# • default health of 150
# Methods:
# • pet: increases health by 5

# Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().

class Dog(Animal):

	def __init__(self, name):
		super().__init__(name, 150)
	
	def pet(self):
		self.health += 5
		return self

a2 = Dog("Fido")
a2.walk().walk().walk().run().run().pet().display_health()

# a2.fly() This causes an error

# Dragon Class
# • inherits everything from Animal
# Attributes:
# • default health of 170
# Methods:
# • fly: decreases health by 10
# • display health: prints health by calling the parent method and prints "I am a Dragon"

class Dragon(Animal):

	def __init__(self, name):
		super().__init__(name, 170)
	
	def fly(self):
		self.health -= 10
		return self
	
	def display_health(self):
		super().display_health()
		print("I am a Dragon")
		return self

a3 = Dragon("Glaurung the Golden")
a3.walk().walk().walk().run().run().fly().display_health()

# Now try creating a new Animal and confirm that it can not call the pet() and fly() methods,
# and its displayHealth() is not saying 'this is a dragon!'.
# Also confirm that your Dog class can not fly().

class Tiger(Animal):

	def __init__(self, name):
		super().__init__(name, 3000)
	
	def be_awesome(self):
		self.health += 5000
		return self
	
	def display_health(self):
		super().display_health()
		print("I am a Tiger... Rawr")
		return self

a4 = Tiger("Tiger")
a4.walk().walk().walk().run().run().be_awesome().display_health()

# a4.pet() This causes an error
# a4.fly() This causes an error