# List

thislist = ["apple", "banana", "cherry"]
print(thislist)
print("--------------------\n")

# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
print("--------------------\n")

# List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"] # List can contain diffenert datatypes

# List Type
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
print("--------------------\n")

# The list() Constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)
print("--------------------\n")

print("------------------------------------------------------------------------\n") 

# Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print("--------------------\n")

# Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
print("--------------------\n")

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mandarin"]
print(thislist[2:5])
print("--------------------\n")

print(thislist[:4])
print("--------------------\n")

print(thislist[2:])
print("--------------------\n")

# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "Orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
print("--------------------\n")

# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
print("--------------------\n")

print("------------------------------------------------------------------------\n")

# Change Item Value
thislist[1] = "blackcurrant"
print(thislist)
print("--------------------\n")

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
print("--------------------\n")

thislist = ["apple", "banana", "ceryy"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
print("--------------------\n")

# Insert Items
thislist = ["apple", "banana", "cheryy"]
thislist.insert(2, "watermelon")
print(thislist)
print("--------------------\n")

print("------------------------------------------------------------------------\n")

# Append Items -- To add an item to the end of the list, we user the append method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
print("--------------------\n")

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
print("--------------------\n") 

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ("mango", "pineapple", "Papaia")
thislist.extend(tropical)
print(thislist)

print("------------------------------------------------------------------------\n")

# Remove Specified Item
thislist = ["apple", "banana", "ceryy"]
thislist.remove("banana")
print(thislist)
print("--------------------\n")

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
print("--------------------\n")

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print("--------------------\n")

# Remove the Last Item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
print("--------------------\n")

# Delete Specified Index using del keyword
thislist = ["apple", "banana", "cheryy"]
del thislist[0]
print(thislist)
print("--------------------\n")

# Delete the entire list using del keyword
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) # This will cause an error because "thislist" no longer exists
print("--------------------\n") 

# Clear the List -- The List still exists but i has no content
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print("--------------------\n")

print("------------------------------------------------------------------------\n")

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
print("--------------------\n")

# Loop Through the Index Numbers
thislist = ["apple", "banana", "cheryy"]
for i in range(len(thislist)):
    print(thislist[i])
print("--------------------\n")

# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1
print("--------------------\n")

# Looping Using List Comprehension
[print(x) for x in thislist]
print("--------------------\n")
