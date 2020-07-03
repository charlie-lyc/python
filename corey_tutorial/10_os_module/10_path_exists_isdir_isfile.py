import os


print(help(os.path.exists))
# Test whether a path exists.  Returns False for broken symbolic links.
print()
print(help(os.path.isdir))
# Return true if the pathname refers to an existing directory.
print()
print(help(os.path.isfile))
# Test whether a path is a regular file
print()


# Practice using example of directory.
print(os.path.exists('TEMP/tmp'))
print(os.path.exists('TEMP/tmp/test.txt'))
print(os.path.isdir('TEMP/tmp'))
print(os.path.isfile('TEMP/tmp/test.txt'))
print()


# Try once.
#
# os.chdir('/Users/charlie/Documents/CoreySchafer_PythonTutorial')
# os.makedirs('TEMP/tmp')
# with open('TEMP/tmp/test.txt', 'w') as f:
# 	f.write('This is test fiel!')
# f.close()
#
# print(os.path.exists('TEMP/tmp'))
# print(os.path.exists('TEMP/tmp/test.txt'))
# print(os.path.isdir('TEMP/tmp'))
# print(os.path.isfile('TEMP/tmp/test.txt'))
# print(os.path.isdir('TEMP/tmp/test.txt'))
# print(os.path.isfile('TEMP/tmp'))



