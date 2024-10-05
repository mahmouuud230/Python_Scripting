# Dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustand",
    "year": 1964
}

# Dictionary Data Types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print("--------------------\n") 

# Can't have Unhashable Keys* 
thisdict = {

    1: "ford",
    (1, 2, 3): "Mustand",
    # [4, 5, 6]: "Hello World"
}
print(thisdict)
print("--------------------\n")

# Can have Unhashable Values
thisdict = {
    "brand": "Ford",
    "model": "Mustand",
    "year": 1964,
    "colors": ["red", "white", "blue"],
    "tuple": (1, 2, 3)
}
print(thisdict)
print("--------------------\n")

# Dictionary Length
thisdict = {
    "Name": "John",
    "Age": 36,
    "Country": "Norway",
    "Job": "Developer"
}
print(len(thisdict))
print("--------------------\n")

# Dictionary Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict["name"])

print("------------------------------------------------------------------------\n")

# Accessing Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["model"])
print("--------------------\n")

# Usind the get() Method
thisdict = {
    "brand": "Ford",
    "model": "Mustand",
}
print(thisdict.get("model"))
print("--------------------\n") 

# Get the dictionary keys
thisdict = {
    "brand": "Ford",
    "model": "Mustand",
    "year": 1964
}
x = thisdict.keys()
y = thisdict.values()
z = thisdict.items()
print(x)
print(y)
print(z)
print("--------------------\n")
thisdict["color"] = "red"
print(x)
print(y)
print(z)
print("--------------------\n")

# Check if Key Exists
thisdict = {
    "brand": "Ford",
    "model": "Mustand",
    "year": 1964
}

if "Ford" in thisdict:
    print("yes")
print("--------------------\n")

print("------------------------------------------------------------------------\n")

# Change Values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
print("--------------------\n") 
