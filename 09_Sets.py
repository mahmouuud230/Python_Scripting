# Python Sets
myset = {"apple", "banana", "cherry"}
print(myset)
print("--------------------\n")

# Duplicates are ignored
myset = {"apple", "banana", "mango", "apple"}
print(myset)
print("--------------------\n") 

# True and 1 are considered the same value
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
print("--------------------\n")

print("------------------------------------------------------------------------\n") 

# Access set Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
print("--------------------\n")


thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("--------------------\n")

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)
print("--------------------\n")

print("------------------------------------------------------------------------\n")

# Add Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
print("--------------------\n")

# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
print("--------------------\n") 

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
print("--------------------\n")

print("------------------------------------------------------------------------\n")

# Remove Items -- If the item to remove does not exist, remove() will raise an error
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
print("--------------------\n")

# Remove an Item using discard() methods -- If not available will not raise an error
thisset = {"apple", "banana", "cherry"}
thisset.discard("banan")
print(thisset)
print("--------------------\n")

# Pop Will remove an Random item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
print("--------------------\n")

# Clear the Set -- Will return an empty set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
print("--------------------\n")

# Delete the Set -- Will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) # This will raise an error because the set no longer exists
print("--------------------\n")

print("------------------------------------------------------------------------\n")

# Jion Two Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print("--------------------\n")

# Using the | operator
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)
print("--------------------\n")

# Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "banana", "cherry"}

myset = set1.union(set2, set3, set4)
anotherset = set1 | set2 | set3 | set4

print(myset)
print(anotherset)
print("--------------------\n")

# Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y) # Using the union() method
print(z)
x.update(y)
print(x) # Using the update() method
print("--------------------\n")

# Intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)
print("--------------------\n")

# Intersection Using the & operator
x = {"apple", "banana", "cherry"}
y = {"goole", "microsoft", "apple"}

z = x & y 
print(z)
print("--------------------\n")

# Using Interseciton Update() Method
x = {"apple", "banana", "cherry"}
y = {"goole", "microsoft", "apple"}

x.intersection_update(y)
print(x)
print("--------------------\n")

# Difference 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)
print("--------------------\n")

# Difference Using the - operator
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
print("--------------------\n") 

# Difference Update() Method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)
print("--------------------\n")

# Symmetric Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)
print("--------------------\n")

# Symmetric Difference Using the ^ operator
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
print("--------------------\n")

# Symmetric Difference Update() Method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
print("--------------------\n")
