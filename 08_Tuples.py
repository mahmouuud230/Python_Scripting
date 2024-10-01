# This is Tuple
from re import M


thistuple = ("apple", "banana", "cherry")
print(thistuple)
print("--------------------\n") 

# Allow Duplicates Values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)    
print("--------------------\n")

# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
print("--------------------\n")

# Create Tuple with one Item
thistuple = ("apple",)
print(type(thistuple))
print("--------------------\n")

# Not a Tuple
thistuple = (("Apple"))
print(type(thistuple))
print("--------------------\n")

# Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
print("--------------------\n")

# Tuple Constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(type(thistuple))
print(thistuple)
print("--------------------\n")

print("------------------------------------------------------------------------\n")

# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print("--------------------\n")

# Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
print("--------------------\n") 

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mandarin")
print(thistuple[2:5])
print("--------------------\n")

# Start from Beginning
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mandarin")
print(thistuple[:4])
print("--------------------\n")

# End at the End
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mandarin")
print(thistuple[2:])
print("--------------------\n")

# Check if item exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
print("--------------------\n")

print("------------------------------------------------------------------------\n")

# Update Tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
print("--------------------\n")

# Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
print("--------------------\n")

# Add tuple to a tuple
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple1 += tuple2
print(tuple1)
print("--------------------\n")

# Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
print("--------------------\n")

# Remove Items
thistuple = ("apple", "banana", "cherry")
# del thistuple
print("--------------------\n")

print("------------------------------------------------------------------------\n")

# Unpack Tuple 
fruits = ("apple", "banana", "cherry")
green, yellow, red = fruits
print(green)
print(yellow)
print(red)
print("--------------------\n")

# Using Asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
green, yellow, *red = fruits
print(green)
print(yellow)
print(red)
print("--------------------\n")

# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
print("--------------------\n")

# Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
print("--------------------\n")

# Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1
print("--------------------\n") 

print("------------------------------------------------------------------------\n")

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple.index("apple"))

