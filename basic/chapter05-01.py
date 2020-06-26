# chapter05-01

# Define Function, Lambda Function

####################################
# def funtction_name(parameter):   #
# 	code                           #
####################################

# example01
def first_func(w):
	print('Hello,', w)

print(type(first_func))
word = 'Good Boy'
first_func(word)
print()

# example02
def return_func(w1):
	return 'Hello, ' + w1

word1 = 'Good Girl'
print(return_func(word1))
print()

# example03 : Multi Returns
def func_mul1(x):
	y1 = x * 10
	y2 = x * 20
	y3 = x * 30
	return y1, y2, y3

q, w, e = func_mul1(10)
print(type(q), type(w), type(e))
print(q, w, e)
print()

# example04 : List Return
def func_mul2(x):
	y1 = x * 10
	y2 = x * 20
	y3 = x * 30
	return [y1, y2, y3]

a = func_mul2(20)
print(type(a))
print(a)
print()

# example05 : Tuple Return
def func_mul3(x):
	y1 = x * 10
	y2 = x * 20
	y3 = x * 30
	return (y1, y2, y3)

b = func_mul3(30)
print(type(b))
print(b)
print()

# example06 : Set Return
def func_mul4(x):
	y1 = x * 10
	y2 = x * 20
	y3 = x * 30
	return {y1, y2, y3}

c = func_mul4(40)
print(type(c))
print(c)
print()

# example07 : Dictionary Return
def func_mul5(x):
	y1 = x * 10
	y2 = x * 20
	y3 = x * 30
	# return {'v1': y1, 'v2': y2, 'v3': y3}
	# return dict([('v1', y1), ('v2', y2), ('v3', y3)])
	return dict(v1=y1, v2=y2, v3=y3)

d = func_mul5(50)
print(type(d))
print(d)
print(d['v2'])
print(d.get('v3'))
print(d.keys())
print(d.values())
print(d.items())
print()


###########################
##  *args  ##  **kwargs  ##
###########################

# *args unpacking : 매개변수(tuple) 이름 자유
def args_func(*args):
	for i, v in enumerate(args): # enumerate() -> [(index0, value0), (index1, value1), ... ]
		print('Result : {}'.format(i), v)
	print('------')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')
print()

# *kwargs unpacking : 매개변수{dictionary} 이름 자유
def kwargs_func(**kwargs):
	for k in kwargs.keys():
		print('Result : {}'.format(k), kwargs[k])
	print('------')

# def kwargs_func(**kwargs):
# 	for k, v in kwargs.items():
# 		print('Result : {}'.format(k), v)
# 	print('------')

kwargs_func(name1='Choi')
### kwargs_func([('name1', 'Choi')]) ### XXX
### kwargs_func('name1': 'Choi') ### XXX
kwargs_func(name1='Choi', name2='Lim')
kwargs_func(name1='Choi', name2='Lim', name3='Han')
print()

# example08
def example(args_1, args_2, *args, **kwargs):
	print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)
print()

###########################

# Nested Function
def nested_func(num):
	def func_in_func(num):
		print(num)
	print('In func')
	func_in_func(num + 100)

nested_func(100)
# func_in_func(100) # NameError: name 'func_in_func' is not defined
print()

############### Lambda Function ###############
# 메모리 절약, 가독성 향상, 코드 간결                 #
# 함수는 객체 생성 -> 리소스(메모리) 할당              #
# lambda는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화 #
# 남발 시 가독성 오히려 감소                         #
################################################

def mul_func(x, y):
	return x * y

print(mul_func(10, 50))

# general function -> assignment
mul_func_var = mul_func
print(mul_func_var(10, 50))
print()

# lambda function -> assignment
lambda_mul_func = lambda x,y:x*y
print(lambda_mul_func(20, 50))
print()

# etc
def func_final(x, y, func):
	print(x * y * func(100, 100))

func_final(10, 20, mul_func)
func_final(10, 20, lambda x,y:x*y)


