x = 4 
x = "Sally"
print(x)
print("-----------------")

# Force the Data Type of the varaible using the following functions
x = str(3)
y = int(3)

print(type(x))
print(type(y))
print("-----------------")

# Variable names are case-sensitive
a = 5
A = "John"

print(a)
print(A)
print("-----------------")

# Assign multiple values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)
print("-----------------")

# Assign one value to multiple variables
x = y = z = "Orange"

print(x)
print(y)
print(z)
print("-----------------")

# Unpack a Collection // while upacking the number of variables should be equal to the number of elements in the collection
fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

print(x)
print(y)
print(z)
print("-----------------")

# Outpu Variables
x = "Python"
y="is"
z = "awesome"

print(x, y, z)
print("-----------------")

x = "Python"
y="is"
z = "awesome"

print(x + y + z)
print("-----------------")

# Global Variables

x = "awesome"

def myfunc():
    print("Python is", x)

myfunc()
print("-----------------")

# Create a variable inside a function, with the same name as the global variable

x = "awesoem"

def myfunc():
    x = "fantastic"
    print("Python is", x)
myfunc()
print("Python is", x)
print("-----------------")

# The global Keyword

x = "awesome"

def myfunc():
    global x
    x = "fantastic"
    print("Pythons is", x)

myfunc()
x = "Hello"

print("Pythos is", x)
print("-----------------")

