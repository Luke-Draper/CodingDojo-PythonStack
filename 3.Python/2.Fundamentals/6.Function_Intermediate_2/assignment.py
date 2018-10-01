print("1.")
# Given

x = [ [5,2,3], [10,8,9] ] 
students1 = [
	{'first_name':'Michael', 'last_name':'Jordan'},
	{'first_name':'John', 'last_name':'Rosales'}
]
sports_directory = {
	'basketball':['Kobe', 'Jordan', 'James', 'Curry'],
	'soccer':['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x':10, 'y':20} ]

# How would you change the value 10 in x to 15? Once you're done x should then be [ [5,2,3], [15,8,9] ].
x[1][0] = 15

# How would you change the last_name of the first student from 'Jordan' to "Bryant"?
students1[0]["last_name"] = "Bryant"

# For the sports_directory, how would you change 'Messi' to 'Andres'?
sports_directory["soccer"][0] = "Andres"

# For z, how would you change the value 20 to 30?
z[0]["y"] = 30

print("2.")
# Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.
# For example, given the following list:

def printDictionary(dict):
	printVal = ""
	for key in dict:
		printVal+=key
		printVal+=" - "
		printVal+=dict[key]
		printVal+=", "
	printVal = printVal[:-2]
	print(printVal)

def iterateDictionary(dict_arr):
	for dict in dict_arr:
		printDictionary(dict)

students2 = [
	{'first_name':'Michael', 'last_name':'Jordan'},
	{'first_name':'John', 'last_name':'Rosales'},
	{'first_name':'Mark', 'last_name':'Guillen'},
	{'first_name':'KB', 'last_name':'Tonel'}
]
iterateDictionary( students2 )

# should output

# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

print("3.")
# Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.


def iterateDictionary2(key, dict_arr):
	for dict in dict_arr:
		print(dict[key])

iterateDictionary2('first_name', students2)

# should output

# Michael
# John
# Mark
# KB

print("4.")

# Create a function that prints the name of each location and also how many locations the Dojo currently has.
# Have the function also print the name of each instructor and how many instructors the Dojo currently has.

def printDojoInfo(dict):
	for key in dict:
		firstOut = str(len(dict[key]))
		firstOut += " " + key.upper()
		print(firstOut)
		for val in dict[key]:
			print(val)
		print("")

dojo = {
	'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
	'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printDojoInfo(dojo)

# should output

# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon