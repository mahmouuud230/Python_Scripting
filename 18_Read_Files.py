# Reading from a file
f = open("demo_file.txt", "r")
print(f.read())
print("--------------------\n")

# Read only parts of the file
f = open("demo_file.txt", "r")
print(f.read(5))
print("--------------------\n")

# Read one Line
f = open("demo_file.txt", "r")
print(f.readline())
print("--------------------\n")

# Read two Lines
f = open("demo_file.txt", "r")
print(f.readline())
print(f.readline())
print("--------------------\n") 

# Loop through the file lines 
f = open("demo_file.txt", "r")
for x in f:
    print(x)
print("--------------------\n")

# Close the file always after reading
f = open("demo_file.txt", "r")
print(f.readline())
f.close()
