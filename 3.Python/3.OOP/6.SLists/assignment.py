
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
			while (current_node.next != None):
				if current_node.next.value == value:
					current_node.next = current_node.next.next # This equals the next in line if the matched value is in the middle but it equals none if the matched value is the tail
					break
				current_node = current_node.next
		return self
	
	def printAllValues(self):
		output = ""
		current_node = self.head
		while (current_node.next != None):
			output += (str(current_node.value) + ", ")
			current_node = current_node.next
		output += str(current_node.value)
		print(output)
		return self

list1 = SList(5)
list1.addNode(7)
list1.addNode(9)
list1.addNode(1)
list1.printAllValues()


list2 = SList(5)
list2.addNode(7)
list2.addNode(9)
list2.addNode(1)
list2.removeNode(9) # removes 9, which is one of the middle nodes in the list
list2.removeNode(5) # removes 5, which is the first value in the list
list2.removeNode(1) # removes 1, which is the last node in the list
list2.printAllValues()