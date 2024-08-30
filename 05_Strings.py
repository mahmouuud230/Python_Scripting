# Strings
from sre_constants import CATEGORY_NOT_LINEBREAK


print("Hello")
print('Hello')
print("-----------------\n")

# Quotes Instide Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
print("-----------------\n")

# Assign String to a Variable
a = "Hello"
print(a)
print("-----------------\n")

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut  labore et dolore magna aliqua."""
print(a)
print("-----------------\n")

# Slicing
b = "Hello, World!"
print(b[2:5])
print("-----------------\n")

# Slicing From the Start
b = "Hello, World!"
print(b[:5]) # Zero is there by default
print("-----------------\n")

# Slicing to the End
b = "Hello, World!"
print(b[2:])
print("-----------------\n")

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])
print("-----------------\n")

# Upper Case
a = "Hello, World!"
print(a.upper())
print("-----------------\n")

# Lower Case
a = "Hello, World!"
print(a.lower())
print("-----------------\n")

# Remove Whitspace
a = " Hello, World! "
print(a.strip())
print("-----------------\n")

# Replace String
a = "HellO, World!"
print(a.replace("o", "J"))
print("-----------------\n")

# Splite String 
a = "Hello, World!"
print(a.split(","))
print("-----------------\n") 

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
print(a + " " + b)
print("-----------------\n")

# Format Strings
age = 36
txt = f"My name is John, and I am {age}"
print(txt)
print("-----------------\n")

# Perfome math operations in the curly brackets
txt = f"The price is {3*3} dollars"
print(txt)
print("-----------------\n")

a = "Test"
b = "TEST"
c = "test"
print(a.count('e'))

