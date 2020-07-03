import os


print(os.getcwd())
os.chdir('/Users/charlie/Documents/CoreySchafer_PythonTutorial')
print(os.getcwd())
print()


print(help(os.walk))
### Directory Tree Generator
### Return tuple : (dirpath, dirnames, filenames)
print()


### os.listdir(path) : 주어진 디렉토리(path) 내의 폴더와 파일들을 리스트로 반환. path가 주어지지 않으면 현재 작업 디렉토리로 설정.
### os.walk(top) : 주어진 디렉토리(top)에 속하는 각 폴더들에 경로(dirpath), 그리고 그 폴더 안에 포함된 하위폴더들의 리스트(dirnames), 파일들의 리스트(filenames)를 반환. listdir()보다 한 단계 더 들어감
for dirpath, dirnames, filenames in os.walk('/Users/charlie/Documents/CoreySchafer_PythonTutorial'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files;', filenames)
    print()


