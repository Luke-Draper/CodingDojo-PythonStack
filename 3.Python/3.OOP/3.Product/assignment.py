# Attributes:
# Price
# Item Name
# Weight
# Brand
# Status: default "for sale"

# Methods:
# Sell: changes status to "sold"
# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item
#	including sales tax
# Return Item: takes reason_for_return as a parameter and changes status accordingly.
#	If the item is being returned because it is defective, change status to "defective"
#	and change price to 0. If it is being returned in the box, like new, mark it "for sale".
#	If the box has been opened, set the status to "used" and apply a 20% discount.
#	(use "defective", "like_new", or "opened" as three possible value for reason_for_return).
# Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.

class Product:

	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"
		print(self.display_info())

	def display_info(self):
		output = "Price: "
		output += str(self.price)
		output += "\nName: "
		output += str(self.item_name)
		output += "\nWeight: "
		output += str(self.weight)
		output += "\nBrand: "
		output += str(self.brand)
		output += "\nStatus: "
		output += str(self.status)
		return output
	
	def sell(self):
		self.status = "sold"
		return self
	
	def add_tax(self, tax):
		return self.price * (1+tax)
	
	def return_item(self, reason_for_return):
		if reason_for_return == "defective":
			self.status = "defective"
			self.price = 0
		elif reason_for_return == "like_new":
			self.status = "for sale"
		elif reason_for_return == "opened":
			self.status = "used"
			self.price = self.price * 0.8
		return self

prod1 = Product(10.99, "Nice Shiny", "1lbs", "McShiners")
print(prod1.return_item("like_new").display_info())
prod2 = Product(7.99, "Ok Shiny", "0.6lbs", "McShiners")
print(prod2.return_item("defective").display_info())
prod3 = Product(4.99, "Starter Shiny", "0.3lbs", "McShiners")
print(prod3.return_item("opened").display_info())
prod4 = Product(4.99, "Ripoff Shiny", "1lbs", "MicShooopers")
print(prod4.sell().display_info())
prod5 = Product(100.99, "LEGENDARY Shiny", "55lbs", "McShiners")
print(prod5.add_tax(0.23))

