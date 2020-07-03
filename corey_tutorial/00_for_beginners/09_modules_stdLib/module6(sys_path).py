import sys
## 만약 모듈이 외부 폴더에 있을 경우 디렉토리를 추가할 수 있다.

## 아래와 같이 시스템 경로를 추가하고 'my_module'파일을 'Downloads'폴더에 옮겨 놓고 실행해 보자.
sys.path.append('/Users/charlie/Downloads')

from my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')

print(index)
print()

print(test)
print()

## 리스트의 마지막 부분에 경로가 추가된 것을 볼 수 있다.("module5.py"의 마지막 부분과 비교)
## 다만, 이것은 일시적인 추가로 파이썬 패키지처럼 영구히 추가하는 방법은 따로 있다.
print(sys.path)
# [
#	'/Users/charlie/Documents/CoreySchafer_PythonTutorial/00_for_beginners/09_modules_stdLib',
#	'/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip', 
#	'/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8', 
#	'/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload', 
#	'/Users/charlie/Library/Python/3.8/lib/python/site-packages', 
#	'/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages', 
#	'/Users/charlie/Downloads'
# ]