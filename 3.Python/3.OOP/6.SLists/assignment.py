
class Node:

	def __init__(self, value):
		self.value = value
		self.next = None

class SList:

	def __init__(self, value):
		node = Node(value)
		self.head = node
	
	def addNode(self, value):
		new_node = Node(value)
		current_node = self.head
		while (current_node.next != None):
			current_node = current_node.next
		current_node.next = new_node
		return self
	
	def removeNode(self, value):
		if self.head.value == value:
			self.head = self.head.next
		else:
			current_node = self.head
			while (current_node.next.next != None):
				if current_node.next.value == value:
					current_node.next = current_node.next.next
					break
				current_node = current_node.next
			
	
	def printAllValues(self):
		output = ""
		current_node = self.head
		while (current_node.next != None):
			output += (str(current_node.value) + ", ")
			current_node = current_node.next
		output += str(current_node.value)
		print(output)
		return self

list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.printAllValues()