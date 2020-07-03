# Module Name Mistake
from math import radians, sin

rads = radians(90)

print(sin(rads))

# 이 파일 이름을 "math.py"인 상태로 실행 하면 :
# ImportError: cannot import name 'radians' from partially initialized module 'math' 
# (most likely due to a circular import) 
# (/Users/charlie/Documents/CoreySchafer_PythonTutorial/24_commonMistakes_fixingThem/math.py)

# 기존 라이브러리에 이미 'math.py' 라는 모듈파일이 존재해서 생기는 에러이다.
# 해결법 : 이 파일을 모듈로 사용하고자 한다면 이 파일의 이름을 바꾸면 된다.
