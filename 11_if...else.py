# If Statement
a = 10
b = 20
if b > a:
    print("b is greater than a")
print("--------------------\n") 

# Elif
a = 10
b = 20

if b > a: # if this condition is true, it won't continue to the next one
    print("b is greater than a")
elif b > a:
    print("Again b is greater than a")
print("--------------------\n")

# Else Statement
a = 10
b = 20

if b < a:
    print("A is greater than B")
elif b == 1:
    print("A is equal to B")
else: 
    print("B is greater than A")
print("--------------------\n")

# Short Hand If
a = 10
b = 20
if a < b: print("A is less than B")
print("--------------------\n")

# Short Hand If...Else
a = 10
b = 20
print("A") if a > b else print("B")
print("--------------------\n")

# Values 
a = 10
b = 20
c = 500

# And
if a < b and c > a:
    print("Both conditions are true")
print("--------------------\n")

# Or
if a < b or a > c:
    print("At least one of the conditions is true")
print("--------------------\n")

# Not 
if not a == b:
    print("The Condition is False")
print("--------------------\n")

# Nested If
x = 41

if x > 10:
    print("Above ten")
    if x > 20:
        print("and also above 20")
    else: 
        print("but not above 20")
elif x == 10:
    print("x is 10")
else:
    print("Below ten")

# Pass Statement -- Used as a placeholder for future modification
a = 33 
b = 200

if b > a:
    pass