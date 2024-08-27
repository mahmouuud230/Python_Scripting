# Floats
x = 35e3
y = 12E4

print(type(x))
print(type(y))
print(y)
print("-----------------")

# Complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
print(x)
print(y)
print(z)
print("-----------------")

# Type Conversion
x = 1
y = 2.8
z = 1j

#convert from int to float
a = float(x)
print(a)
#convert from float to int
b = int(y)
print(b)
#convert from int to complex
c = complex(x)
print(c)
print("-----------------")

# Random Number

import random

print(random.randrange(1, 10))
print("-----------------")
