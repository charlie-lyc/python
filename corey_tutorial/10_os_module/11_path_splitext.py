import os


print(help(os.path.splitext))
# Split the extension from a pathname. 
# Extension is everything from the last dot to the end.
# Returns tuple "(root, ext)"
print()


# Practice using example of directory.
print(os.path.splitext('TEMP/tmp/test.txt'))
print()


