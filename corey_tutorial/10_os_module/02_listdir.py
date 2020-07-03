import os

print(os.getcwd())
# change working directory
os.chdir('/Users/charlie/Documents/CoreySchafer_PythonTutorial')
print(os.getcwd())
print()

# get information of "os.listdir()"
print(help(os.listdir))
# ... Return a "list" containing the names of the files in the directory. ...
print()

# print out the list of files and folders in working directory.
for ld in os.listdir():
	print(ld)
print()
