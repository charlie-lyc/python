from my_module import find_index, test
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')

print(index)
print()

print(test)
print()

print(sys.path)
# [
#	'/Users/charlie/Documents/CoreySchafer_PythonTutorial/00_for_beginners/09_modules_stdLib',
#	'/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip',
#	'/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8',
#   '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload',
#   '/Users/charlie/Library/Python/3.8/lib/python/site-packages', 
#   '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages'
# ]
