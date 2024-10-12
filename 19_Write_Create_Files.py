# Write to a file
f = open("demo_file.txt", "w")
f.write("Now the file has overritten the content!")
f.close()

# Open and read the file after overwriting
f = open("demo_file.txt", "r")
print(f.read())
f.close()

# Append to a file
f = open("demo_file.txt", "a")
f.write("\nNow the file has more content!")
f.close()

# Open and read the file after appending
f = open("demo_file.txt", "r")
print(f.read())
f.close()

# Create a file called "myfile.txt" -- If the file doesn't exist, it will be throw an error
f = open("myfile.txt", "x")
f.close()