############### example00 ############### 
import chapter01
print()

############### example01 ###############

# import chapter06_02

# print('-' * 15)
# print('called! internal module!')
# print(chapter06_02.add(5, 5))
# print(chapter06_02.subtract(15, 5))
# print(chapter06_02.multiply(5, 5))
# print(chapter06_02.divide(10, 2))
# print(chapter06_02.power(5, 3))
# print('-' * 15)


############### example02 ##############

import sys

# print(sys) # <module 'sys' (built-in)>
# print()
# print(sys.path)
# print()
# print(type(sys.path)) # <class 'list'>
# print()

sys.path.append('/Users/charlie/Documents/Inflearn/WorkSpace/Python/MyModule') # 일시적인 path 등록방법이다!!! Python에 영구 등록하는 방법은 따로 있다.
print(sys.path)
print()

import arithmetics

print('-' * 15)
print('called! external module!')
print(arithmetics.add(5, 5))
print(arithmetics.subtract(15, 5))
print(arithmetics.multiply(5, 5))
print(arithmetics.divide(10, 2))
print(arithmetics.power(5, 3))
print('-' * 15)



