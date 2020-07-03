import os

### drag and drop a file from folder into terminal to know Absolute Directory.
### /Users/charlie/Documents/CoreySchafer_PythonTutorial/13_automateParsing_renameFiles/examples/exam01.py
# os.chdir('/Users/charlie/Documents/CoreySchafer_PythonTutorial/13_automateParsing_renameFiles/examples')

### but this is too long, so use Relative Directory.
print(os.getcwd())
# /Users/charlie/Documents/CoreySchafer_PythonTutorial/13_automateParsing_renameFiles
os.chdir('./examples')
print(os.getcwd())
print()

### Be careful invisible folders of files in working directory!!!

### Corey's Code:
for f in os.listdir():
	f_name, f_ext = os.path.splitext(f)
	f_title, f_course, f_num = f_name.split('-')
	# print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))

	f_num = f_num.strip()[1:].zfill(2)
	f_course = f_course.strip()
	f_title = f_title.strip()
	# print('{}-{}{}'.format(f_num, f_title, f_ext))

	new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
	os.rename(f, new_name)
print()


### Check whether file names change.
for f in sorted(os.listdir()):
	print(f)


