# Boolean Values
print(10 > 9)
print (10 == 9)
print(10 < 9)
print("--------------------\n")

# Booleans with Condiiotnal Statements
a=33
b = 20
if b > a:
    print("B is greater than A")
else:
    print("B is not greater than A")
print("--------------------\n")

# Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))
print("--------------------\n")

# Most Values are True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print("--------------------\n")

# Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print("--------------------\n")

# Functions can Return a Boolean

def myFunction():
    return True
print(bool(myFunction()))
print("--------------------\n")

if myFunction():
    print("Yes!")
else: print("NO!")
print("--------------------\n")

# Builtin function that return boolean

x = 20.2
print(isinstance(x, int))
print("--------------------\n")


