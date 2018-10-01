# Part 1

# Basic
# Print all the numbers/integers from 0 to 150.



# Multiples of Five
# Print all the multiples of 5 from 5 to 1,000,000.



# Counting, the Dojo Way
# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".



# Whoa. That Sucker's Huge
# Add odd integers from 0 to 500,000, and print the final sum.



# Countdown by Fours
# Print positive numbers starting at 2018, counting down by fours (exclude 0).



# Flexible Countdown
# Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.
# For (2,9,3), print 3 6 9 (on successive lines)



# Part 2

list1 = [3,5,1,2]
for i in list1:
	print(i)
	# This returns each of the items in the aray in order 3,5,1,2
list2 = [3,5,1,2]
#for i in range(list2):
#	print(i)
#	This does not work as it tries to reference list2 as an integer not an array
list3 = [3,5,1,2]
for i in range(len(list3)):
	print(i)
	# This returns the indexes of the items in the array 0,1,2,3
