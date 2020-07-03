import os


print(help(os.path.split))
# Split a pathname.  Returns tuple "(head, tail)" where "tail" is everything after the final slash.
print()
print(help(os.path.dirname))
# Returns the 'directory component(head)' of a pathname.
print()
print(help(os.path.basename))
# Returns the 'final component(tail)'' of a pathname
print()


# Practice using example of directory.
print(os.path.split('TEMP/tmp/test.txt'))
print(os.path.dirname('TEMP/tmp/test.txt'))
print(os.path.basename('TEMP/tmp/test.txt'))
print()
print(os.path.split('TEMP/tmp'))
print(os.path.dirname('TEMP/tmp'))
print(os.path.basename('TEMP/tmp'))
print()


