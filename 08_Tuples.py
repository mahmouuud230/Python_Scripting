# This is Tuple
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
thistuple = (["apple"])
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

