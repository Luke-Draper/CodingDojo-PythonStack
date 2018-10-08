
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
		if self.head == None:
			return self
		elif self.head.value == value:
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
	
	def insertNode(self, value, index):
		new_node = Node(value)
		if index == 0:
			new_node.next = self.head
			self.head = new_node
		else:
			current_node_index = 0
			current_node = self.head
			while (current_node.next != None):
				if current_node_index+1 == index:
					break
				current_node_index += 1
				current_node = current_node.next
			new_node.next = current_node.next
			current_node.next = new_node
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
list2.removeNode(9)
list2.removeNode(5)
list2.removeNode(1)
list2.printAllValues()

list3 = SList(5)
list3.addNode(7)
list3.addNode(9)
list3.addNode(1)
list3.insertNode(2, 0)
list3.insertNode(4, 2)
list3.insertNode(6, 6)
list3.insertNode(8, 24)
list3.printAllValues()