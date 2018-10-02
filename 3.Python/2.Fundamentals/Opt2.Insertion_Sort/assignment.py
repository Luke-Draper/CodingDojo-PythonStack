import random
import math
def randTestArray(min=0, max=100, length=20):
	output = []
	for i in range(0,length):
		output.append(random.randint(min, max))
	return output

def insertionSort(arr):
	print("Starting Array : ")
	print(arr)
	length = len(arr)
	swaps = 0
	comparisons = 0
	for nextIndex in range(1,len(arr)):
		for i in range(nextIndex,0,-1):
			if arr[i]<arr[i-1]:
				arr[i], arr[i-1] = arr[i-1], arr[i]
				swaps += 1
			else:
				break
			comparisons += 1
	print("Ending Array : ")
	print(arr)
	print("Length : " + str(length))
	print("Swaps : " + str(swaps))
	print("Comparisons : " + str(comparisons))
	return arr

test = randTestArray(0,1000,1000)
insertionSort(test)