import os

print(os.getcwd())
os.chdir('/Users/charlie/Documents/CoreySchafer_PythonTutorial')
print(os.getcwd())
print()

### Make directory and sub-directory at once : this is very handy
# os.makedirs('os_module/sub_dir')
### Make directory without sub-directory
# os.makedirs('os_module')


### This is also OK : step by step
# os.mkdir('os_module')
# os.mkdir('os_module/sub_dir')


### 해당 디렉토리가 없을 경우 : "FileNotFoundError" (actually, "DirectoryNotFoundError")
### 해당 디렉토리가 있을 경우 : "FileExistsError"
# os.mkdir('os_module/sub_dir')

### 디렉토리가 만들어 졌는지 확인
for ld in os.listdir():
	print(ld)
print()
