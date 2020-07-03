import os

print(os.getcwd())
os.chdir('/Users/charlie/Documents/CoreySchafer_PythonTutorial')
print(os.getcwd())
print()

### Remove directory and sub-directory at once
# os.removedirs('os_module/sub_dir')
### If there is no sub-directory, this is possible.
# os.removedirs('os_module')

### This is also OK : step by step
# os.rmdir('os_module/sub_dir')
# os.rmdir('os_module')


### 해당 디렉토리가 없을 경우               : FileNotFoundError
### 해당 디렉토리내에 서브 디렉토리가 있을 경우 : OSError
# os.removedirs('os_module')

### 해당 디렉토리가 없을 경우 : FileNotFoundError
# os.rmdir('os_module/sub_dir')

### 디렉토리가 지워졌는지 확인
for ld in os.listdir():
	print(ld)
print()
