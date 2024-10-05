# Creating a Function
def my_function():
    print("Hello from a function")
my_function()
print("--------------------\n")

# Arguments
def myfun(fname):
    print(fname + " Alakkad")
myfun("Mahmoud")
myfun("Ali")
myfun("Ahmed")
print("--------------------\n")

# Number of Arguments
def myfun(fname, lname):
    print(fname, lname)
myfun("Mahmoud", "Alakkad")
print("--------------------\n")

# If we try to call the function with 1 or 3 arguments, we will get an error:
# --> myfun("Mahmoud")

# Arbitrary Arguments, *args
def myfun(*kids):
    print("The youngest child is " + list(kids).pop())
myfun("Sam", "Ali", "Gabi")
print("--------------------\n")

# Arbitrary Keyword Arguments, **kwargs
def myfun(**kid):
    print("His last name is " + kid["lname"])
myfun("Hello World", fname = "Mahmoud", lname = "alakkad")
print("--------------------\n")

# Default Parameter Value
def myfun(country = "Norway"):
    print("I am from " + country)
myfun("Sweden")
myfun("India")
myfun()
myfun("Brazil")
print("--------------------\n")

# Passing a List as an Argument
def myfun(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
myfun(fruits)
print("--------------------\n")

# Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
print("--------------------\n")

# The pass Statement
def myfunction():
    pass

# Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)