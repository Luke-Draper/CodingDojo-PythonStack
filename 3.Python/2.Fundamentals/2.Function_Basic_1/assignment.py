def a1():
	return 5
print(a1())
# Prediction : 5
# Output : 5
print("--=#=--")

def a2():
	return 5
print(a2()+a2())
# Prediction : 10
# Output : 10
print("--=#=--")

def a3():
	return 5
	return 10
print(a3())
# Prediction : 5
# Output : 5
print("--=#=--")

def a4():
	return 5
	print(10)
print(a4())
# Prediction : 5
# Output : 5
print("--=#=--")

def a5():
	print(5)
#x = a5()
x=None
print(x)
# Prediction : 5,None
# Output : 5,None
print("--=#=--")

def a6(b,c):
	print(b+c)
# print(a6(1,2) + a6(2,3))
# Prediction : ERROR (None + None)
# Output : ERROR
print("--=#=--")

def a7(b,c):
	return str(b)+str(c)
print(a7(2,5))
# Prediction : 25
# Output : 25
print("--=#=--")

def a8():
	b = 100
	print(b)
	if b < 10:
		return 5
	else:
		return 10
	return 7
print(a8())
# Prediction : 100,10
# Output : 100,10
print("--=#=--")

def a9(b,c):
	if b<c:
		return 7
	else:
		return 14
	return 3
print(a9(2,3))
print(a9(5,3))
print(a9(2,3) + a9(5,3))
# Prediction : 7,14,21
# Output : 7,14,21
print("--=#=--")

def a10(b,c):
	return b+c
	return 10
print(a10(3,5))
# Prediction : 8
# Output : 8
print("--=#=--")

b = 500
print(b)
def a11():
	b = 300
	print(b)
print(b)
a11()
print(b)
# Prediction : 500,500,300,500
# Output : 500,500,300,500
print("--=#=--")

b = 500
print(b)
def a12():
	b = 300
	print(b)
	return b
print(b)
a12()
print(b)
# Prediction : 500,500,300,500
# Output : 500,500,300,500
print("--=#=--")


b = 500
print(b)
def a13():
	b = 300
	print(b)
	return b
print(b)
b=a13()
print(b)
# Prediction : 500,500,300,300
# Output : 500,500,300,300
print("--=#=--")

def a14():
	print(1)
	b1()
	print(2)
def b1():
	print(3)
a14()
# Prediction : 1,3,2
# Output : 1,3,2
print("--=#=--")

def a15():
	print(1)
	x = b2()
	print(x)
	return 10
def b2():
	print(3)
	return 5
y = a15()
print(y)
# Prediction : 1,3,5,10
# Output : 1,3,5,10
