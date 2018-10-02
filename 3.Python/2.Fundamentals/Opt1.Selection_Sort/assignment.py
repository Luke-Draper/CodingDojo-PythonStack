import random
import math
def randTestArray(min=0, max=100, length=20):
	output = []
	for i in range(0,length):
		output.append(random.randint(min, max))
	return output

def selectionSort(arr):
	print("Starting Array : ")
	print(arr)
	length = len(arr)
	swaps = 0
	comparisons = 0
	for currentStart in range(len(arr)):
		min = currentStart
		for i in range(currentStart+1, len(arr)):
			if arr[i]<arr[min]:
				min = i
			comparisons += 1
		arr[min], arr[currentStart] = arr[currentStart], arr[min]
		swaps += 1
	print("Ending Array : ")
	print(arr)
	print("Length : " + str(length))
	print("Swaps : " + str(swaps))
	print("Comparisons : " + str(comparisons))
	return arr

test = randTestArray(0,1000,1000)
selectionSort(test)