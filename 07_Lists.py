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

print("------------------------------------------------------------------------\n")

# List Comprehension


# Without List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)
print(newList)
print("--------------------\n") 

# With List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x for x in fruits if 'a' in x]
print(newList)
print("--------------------\n") 

# Iterable
newlist = [x for x in range(10)]
print(newlist)
print("--------------------\n") 

# Iterable with a condition
newlist = [x for x in range(10) if x < 5]
print(newlist)
print("--------------------\n")

# Iterable with an expression
newlist = [x.upper() for x in fruits]
print(newlist)
print("--------------------\n")

# Set all the values in the List to "Hello"
thislist = ['Hello' for x in fruits]

# Return "Orange" instead of "Banana"
thislist = ["Apple", "JUice", "is", "great"]
newlist = [x if x != "banana" else "orange" for x in thislist]
print(newlist)
print("--------------------\n")     

print("------------------------------------------------------------------------\n")

# Sort List Alphanumerically
thislist = ["a1e", "ad", "ac", "ab", "a"]
thislist.sort(),
print(thislist)
print("--------------------\n")

# Sort List Numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
print("--------------------\n")  

# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)
print("--------------------\n") 

# Sort Descending Numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)
print("--------------------\n")

# Customize Sort Function
def myFun(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myFun)
print(thislist)
print("--------------------\n")


# Case Insensitive Sort // sort() method is case sensitive by default
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
print("--------------------\n")

# Case Insensitive Sort
thislist = ["A", "a", "d", "D", "B", "b"]
thislist.sort(key=str.lower)
print(thislist) 
print("--------------------\n")

# Reverse List Order
thislist = ["One","Two", "Three",]
thislist.reverse()
print(thislist)
print("--------------------\n") 

print("------------------------------------------------------------------------\n")

# Copy List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
print("--------------------\n")

# Another way to make a copy is to use the built-in method list()
thislist = ["apple", "banana", "cherry"]
mylist = thislist
print(mylist)
print("--------------------\n")

# Another way to make a copy is to use the built-in method list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
print("--------------------\n")

# Use the slice Operator to make a copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
print("--------------------\n")

print("------------------------------------------------------------------------\n")

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
print("--------------------\n") 

# Append List2 into List1

for x in list2:
    list1.append(x)
print(list1)
print("--------------------\n")

# Use the extend() method to add List2 at the end of List1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
x = len(list1)
print(x)