import os

# Get current working directory
print(os.getcwd())
# /Users/charlie/Documents/CoreySchafer_PythonTutorial/10_os_module
print()

# Change working directory
os.chdir('/Users/charlie/Documents/CoreySchafer_PythonTutorial')
print(os.getcwd())
# /Users/charlie/Documents/CoreySchafer_PythonTutorial
print()

# Get all attributes and methods 
print(dir(os)) # so many
print()

# print(help(os)) # too long
# print()

print(help(os.getcwd))
print()

print(help(os.chdir))

