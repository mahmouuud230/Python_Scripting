import os
f = open("file.txt", "x")
f.close()

# Delete a file
os.remove("file.txt")

# Check if file exists -- Before removing to avoid FileNotFoundError
if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("The files does not exist")

# Create a directory
os.mkdir("myPythonDir")

# Remove a directory
os.rmdir("myPythonDir")
