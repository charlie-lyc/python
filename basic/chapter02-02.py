# python basic
# chapter02-2

# Variable

# declaration
n = 700
# output
print(n)
print(type(n))

# declaration at once
x = y = z = 700
print(x, y, z)

var = 75
# re-declaration
var = 'Change Value'
print(var)
print(type(var))
print()

# object references
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# example1
print(300)
print(int(300))

# example2
# n -> 777
n = 777
print(n, type(n))

# n -> 777 <- m
m = n
print(m,n)
print(type(m), type(n))

m = 400
print(m, n)
print(type(m), type(n))
print()

# id() : identify the object

# different object
# m = 800
# n = 655
# print(id(m))
# print(id(n))
# print(id(m)==id(n))

# same object
m = 800
n = 800
print(id(m))
print(id(n))
print(id(m) == id(n))

# various declaration

# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates -> Variable

# acceptable cases
age = 1
Age = 2
aGe = 3
agE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# unaccepable case : starting with number, reserved words
# 1age = 9 
# for = 10
"""
and as assert break class continue def del elif else except 
False finally for from global if in is import lambda None 
nonlocal not or pass raise return True try while with yield       
"""
