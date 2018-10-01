print("Countdown")
# Create a function that accepts a number as an input.
# Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).
# For example countDown(5) should return [5,4,3,2,1,0].

def countdown(num):
	if num < 0:
		return "invalid input : num less than 0"
	output = [num]
	for i in range(num-1, 0-1, -1):
		output.append(i)
	return output

print(countdown(5))

print("Print and Return")
# Your function will receive an array with two numbers. Print the first value, and return the second.

def printAndReturn(arr):
	print(arr[0])
	return arr[1]

print(printAndReturn([4,8]))

print("First Plus Length")
# Given an array, return the sum of the first value in the array, plus the array's length.

def firstPlusLength(arr):
	return arr[0]+len(arr)

print(firstPlusLength([4,8]))

print("Values Greater than Second")
# Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.
# Print how many values this is. If the array is only one element long, have the function return False

def valuesGreaterSecond(arr):
	if len(arr)<=1:
		return False
	output = []
	for i in arr:
		if i > arr[1]:
			output.append(i)
	print(len(output))
	return output

print(valuesGreaterSecond([1,2,3,4,5,6,7,8,9,1,1,3]))

print("This Length, That Value")
# Write a function called lengthAndValue which accepts two parameters, size and value.
# This function should take two numbers and return a list of length size containing only the number in value.
# For example, lengthAndValue(4,7) should return [7,7,7,7].

def lengthAndValue(len, val):
	output = []
	for i in range(len):
		output.append(val)
	return output

print(lengthAndValue(4,7))