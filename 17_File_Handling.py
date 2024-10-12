'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
'''

# Open a file for reading using Open() function -- 'r' mode by default
f = open("playground.py")
print(f.read())

# Equivalent to the above code
f = open("playground.py", "rt")
print(f.read())

'''
Make sure the file is there when using open() function with 'r'
If the file is not availabe, it will throw an error
'''



