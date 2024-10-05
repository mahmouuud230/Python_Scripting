# python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
print("--------------------\n") 

# Looping Through a String
for x in "banana":
    print(x)
print("--------------------\n")

# The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        print("found it")
        break
print("--------------------\n")

# The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "apple":
        continue
    print(x)
else: print("Apple is execluded")
print("--------------------\n")

# The range() Function
for x in range(6):
    print(x)
print("--------------------\n")

# range(start, end)
for x in range(2, 6):
    print(x)
print("--------------------\n")

# range(start, end, incrementValue)
for x in range(2, 30, 3):
    print(x)
print("--------------------\n") 

# Else in For Loop
for x in range(6):
    print(x)
else: print("Finally Finished!")
print("--------------------\n")

# Else with Break -- Will not be executed
for x in range(6):
    if x == 3: break
    print(x)
else: print("Finally Finished!")
print("--------------------\n")

# Nested Loops
OuterLoop = ["{", "}"]
InnerLoop = ["A", "B", "C"]
for x in OuterLoop:
    print(x)
    if x == "}": break
    for y in InnerLoop:
        print(y)
print("--------------------\n")