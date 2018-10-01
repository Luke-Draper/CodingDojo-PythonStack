print("Biggie Size")
# Given an array, write a function that changes all positive numbers in the array to "big".
# Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

def biggieSize(arr):
	for i in arr:
		if i >= 0:
			i = "big"
	return arr

print(biggieSize([-1, 3, 5, -5]))

print("Count Positives")
# Given an array of numbers, create a function to replace last value with number of positive values.
# Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def countPositives(arr):
	acc = 0
	for i in arr:
		if i >= 0:
			acc += 1
	arr[len(arr)-1] = acc
	return arr

print(countPositives([-1,1,1,1]))

print("SumTotal")
# Create a function that takes an array as an argument and returns the sum of all the values in the array.
# For example sumTotal([1,2,3,4]) should return 10

def sumTotal(arr):
	sum = 0
	for i in arr:
		sum += i
	return sum

print(sumTotal([1,2,3,4]))

print("Average")
# Create a function that takes an array as an argument and returns the average of all the values in the array.
# For example multiples([1,2,3,4]) should return 2.5

def average(arr):
	return sumTotal(arr)/len(arr)

print(average([1,2,3,4]))

print("Length")
# Create a function that takes an array as an argument and returns the length of the array.
# For example length([1,2,3,4]) should return 4

def length(arr):
	return len(arr)

print(length([1,2,3,4]))

print("Minimum")
# Create a function that takes an array as an argument and returns the minimum value in the array.
# If the passed array is empty, have the function return false.
# For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(arr):
	min = arr[0]
	for i in arr:
		if i < min:
			min = i
	return min

print(minimum([1,2,3,4]))
print(minimum([-1,-2,-3]))

print("Maximum")
# Create a function that takes an array as an argument and returns the maximum value in the array.
# If the passed array is empty, have the function return false.
# For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maximum(arr):
	max = arr[0]
	for i in arr:
		if i > max:
			max = i
	return max

print(maximum([1,2,3,4]))
print(maximum([-1,-2,-3]))

print("UltimateAnalyze")
# Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

def ultimateAnalyze(arr):
	return {"sumTotal":sumTotal(arr),"average":average(arr),"minimum":minimum(arr),"maximum":maximum(arr),"length":length(arr)}

print(ultimateAnalyze([1,2,3,4]))

print("ReverseList")
# Create a function that takes an array as an argument and return an array in a reversed order.
# Do this without creating an empty temporary array.
# For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

import math

def reverse(arr):
	firstIndex = 0
	lastIndex = len(arr)-1
	middle = len(arr)/2
	if len(arr)/2%2 == 1:
		middle = math.ceil(middle)
	middle = int(middle)
	for i in range(firstIndex,middle):
		placeholder = arr[firstIndex+i]
		arr[firstIndex+i] = arr[lastIndex-i]
		arr[lastIndex-i] = placeholder
	return arr

print(reverse([1,2,3,4]))
print(reverse([1,2,3,4,5]))
print(reverse([1,2,3,4,5,6]))
print(reverse([1,2,3,4,5,6,7]))
