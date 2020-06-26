## chapter06-03

## Packge
## 작성 및 사용법
## 패키지로 분할된 개별적인 모듈로 구성
## 상대경로 : ".."는 부모 디렉토리, "."는 현재 디렉토리를 의미 => 모듈 내부에서만 사용
## __init__.py : Python3.3부터는 없어도 팩키지로 인식 => 단, 하위 호환을 위해 빈 파일 작성 추천

############### example01 ###############
import sub.sub1.module1
import sub.sub2.module2

sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()
print()
sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()
print()
print()

############### example02 ###############
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # alias

module1.mod1_test1()
module1.mod1_test2()
print()
m2.mod2_test1()
m2.mod2_test2()
print()
print()

############### example03 ############### : 비추천. 만약 팩키지안에 모듈파일이 수백개라면 메모리에 영향을 줄 수 있다.
# from sub.sub1 import *
# from sub.sub2 import *

# module1.mod1_test1()
# module1.mod1_test2()
# print()
# module2.mod2_test1()
# module2.mod2_test2()
# print()
# print()

############### example03 ###############
# __init__.py : 일반적으로 빈 파일로 작성 - 이 파일이 포함된 폴더가 팩키지임을 명시, sub폴더 참조

# 모듈1,2에 대하여 모두에게 접근 허용 
# __all__ = ['module1', 'module2']

# 모듈2에서 해결할 수 없는 버그가 발생해서 사용하지 못하게
# __all__ = ['module1'] 












