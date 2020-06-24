# chapter03-01

# data type
"""
1. int : 정수
2. float : 실수
3. complex : 복소수
4. bool : 불린
5. str : 문자열(시퀀스)
6. list : 리스트(시퀀스)
7. tuple : 튜플(시퀀스)
8. set : 집합
9. dict : 사전
"""

str1 = 'python'
str2 = 'anaconda'
bool1 = True
float1 = 10.0
int1 = 7
list1 = [str1, str2]
dict1 = {
    "name": "machine learning",
    "version": 2.0
}
tuple1 = (7, 8, 9)
set1 = {3, 5, 7}
print(type(str1))
print(type(str2))
print(type(bool1))
print(type(float1))
print(type(int1))
print(type(list1))
print(type(dict1))
print(type(tuple1))
print(type(set1))
print()

# operator
"""
+ : addition
- : subtraction
* : multiplication
/ : division
// : share
% : remain
** : exponent
pow() : exponent ex) pow(x, y) x**y
abs() : absolute value
"""

i1 = 77
i2 = -14
big_int1 = 777777777788888888889999999999
big_int2 = 333333333322222222221111111111
f1 = 0.999
f2 = 3.141592
f3 = -3.9
f4 = 3/9

print(i1)
print(i2)
print(big_int1)
print(big_int2)
print(f1)
print(f2)
print(f3)
print(f4)
print()

print('>>>>> +')
print('i1 + i2 =', i1 + i2)
print('big_int1 + big_int2 =', big_int1 + big_int2)
print('f1 + f2 =', f1 + f2)
print('>>>>> -')
print('i1 - i2 =', i1 - i2)
print('big_int1 - big_int2 =', big_int1 - big_int2)
print('f1 - f2 =', f1 - f2)
print('>>>>> *')
print('i1 * i2 =', i1 * i2)
print('big_int1 * big_int2 =', big_int1 * big_int2)
print('f1 * f2 =', f1 * f2)
print('>>>>> /')
print('i1 / i2 =', i1 / i2)
print('big_int1 / big_int2 =', big_int1 / big_int2)
print('f1 / f2 =', f1 / f2)
print('>>>>> //')
print('i1 // i2 =', i1 // i2)
print('big_int1 // big_int2 =', big_int1 // big_int2)
print('f1 // f2 =', f1 // f2)
print('>>>>> %')
print('i1 % i2 =', i1 % i2)
print('big_int1 % big_int2 =', big_int1 % big_int2)
print('f1 % f2 =', f1 % f2)
print('>>>>> **')
print('i1 ** i2 =', i1 ** i2)
# print('big_int1 ** big_int2 =', big_int1 ** big_int2)
print('f1 ** f2 =', f1 ** f2)
print()

# type transformation
a = 3.
b = 6
c = .7
d = 12.7
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(float(b))
print(int(c))
print(int(d))
print(int(True))
print(int(False))
print(float(True))
print(float(False))
print(complex(d))
print(complex(True))
print(complex(False))
print()
# smart python
print(int('3'))
print(float('3'))
print()

# operation function
print(abs(-7))
x, y = divmod(100, 8) # share and remain
print(x, y)
print(pow(x, y), x ** y)
print()

# external module
import math

print(math.pi)
print(math.ceil(5.1)) # math.ceil(x) : minimum integer more than x
