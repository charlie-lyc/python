import os

print(os.getcwd())
os.chdir('/Users/charlie/Documents/CoreySchafer_PythonTutorial')
print(os.getcwd())
print()

### 현재 디렉토리내 대상파일 확인
for ld in os.listdir():
	if ld == 'test.txt':
		print("'test.txt' is founded.")
		break
else:
	print("There is no 'test.txt'!")
	exit()
print()

# Rename file
os.rename('test.txt', 'TEST.txt')


### 파일이름 바뀌었는지 확인
for ld in os.listdir():
	if ld == 'demo.txt':
		print("'test.txt' has renamed to 'TEST.txt'.")
		break
else:
	print("Something went wrong!")
	exit()
print()
