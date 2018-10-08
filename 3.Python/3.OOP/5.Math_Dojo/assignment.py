# Create a Python class called MathDojo that has the methods add and subtract.
# Have these 2 functions take at least 1 parameter.

# Then create a new instance called md. It should be able to do the following task:

# x = md.add(2).add(2,5,1).subtract(3,2).result
# print(x) # should print 5
# which should perform 0+2+(2+5+1)-(3+2) and print 5.

class MathDojo:

	def __init__(self, result = 0):
		self.result = result

	def add(self, *args):
		for arg in args:
			self.result += arg
		return self

	def subtract(self, *args):
		for arg in args:
			self.result -= arg
		return self

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x) # should print 5

