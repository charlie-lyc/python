## chapter07-01

## Exception
###################################################################
# SyntaxError, ZeroDivisionError, NameError, IndexError, KeyError #
###################################################################
# AttributeError, ValueError, FileNotFoundError, TypeError        #
###################################################################
# 문법적으로는 예외가 없지만, 코드 실행 프로세스에서 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.(처리를 다른쪽으로 넘김)
# 4. 예외를 무시(불가피할 경우에만. 왠만하면 처리하도록)


############### SyntaxError ############### : 문법 오류

# print('error)

# if True
# 	pass


############### ZeroDivisionError ############### : 0으로 나누기

# print(100/0)


############### NameError ############### : 참조 없음

# a = 10
# b = 15
# print(c)


############### IndexError ############### : 인덱스 없음

# x = [50, 70, 90]
# print(x[3])

# y = [10, 20, 30]
# print(y.pop())
# print(y.pop())
# print(y.pop())
# print(y.pop())


############### KeyError ###############

# dic = {'name': 'Lee', 'age': 41, 'city': 'Busan'}
# print(dic['hobby'])
# print(dic.get('hobby')) # No Error


##############################################################         ###############################
# EAFP Principle : Easier to Ask Forgiveness than Permission # <=====> # LBYL : Look Before You Leap #
##############################################################         ###############################
# Python Software Foundation 
# : 일단 예외가 없다고 가정하고 먼저 프로그램을 작성 => 런타임 예외 발생시 예외 처리 권장


############### AttributeError ############### : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())


############### ValueError ###############

# x = [10, 50, 90]
# x.remove(100)


############### FileNotFoundError ###############

# f = open('test.txt')


############### TypeError ############### : 자료형에 맞지 않는 연산을 수행할 경우

# x = [1, 2]
# y = (1, 2)
# z = 'test'
# print(x + y)
# print(y + z)
# print(x + z)
# print(x + list(y)) # No Error
# print(x + list(z)) # No Error


######################################
# 예외 처리 기본                         #
# try : 에러가 발생할 가능성이 있는 코드 실행  #
# except [ErrorName1] : 여러개 가능      #
# except [ErrorName2]                 #
#             :                       #
# else : try블록의 에러가 없을 경우 실행     #
# finally : 항상 실행                   #
######################################

## example01
name = ['Kim', 'Lee', 'Park']

try:
	z = 'Lee' # 'Cho'
	x = name.index(z)
	print('{} is found at the index {} of name list.'.format(z, x))
except ValueError: # 에러의 종류를 명확히 밝히고 처리 - 최상의 방법
	print('{} is not found. - Occured ValueError!'.format(z))
else:
	print('OK! - else out')
print()


## example02
# name = ['Kim', 'Lee', 'Park']

# try:
# 	z = 'Lee' # 'Cho'
# 	x = name.index(z)
# 	print('{} is found at the index {} of name list.'.format(z, x))
# except: # or "except Exception:" 모든 에러의 종류를 포용할 수 있다. 하지만 에러의 종류는 알수가 없다.
# 	print('{} is not found!'.format(z))
# else:
# 	print('OK! - else out')
# print()


## example03
# name = ['Kim', 'Lee', 'Park']

# try:
# 	z = 'Cho'
# 	x = name.index(z)
# 	print('{} is found at the index {} of name list.'.format(z, x))
# except Exception as e:
# 	print(e) # 에러내용을 출력
# else:
# 	print('OK! - else out')
# finally: # 예외가 발생하든 하지 않든 항상 실행해 주어야 하는 구문. 메모리 관리등의 목적.
# 	print('finally!')
# print()


## example04 : "raise"키워드를 이용해 의도적으로 예외를 직접 발생시킴
# try:
# 	a = 'Kim'
# 	if a == 'Park':
# 		print('OK! Pass!')
# 	else:
# 		raise ValueError # a의 값이 없거나 잘못된 것이 아닌데 의도적으로 에러를 발생시켜 'Kim'이외에는 접근하지 못하도록 막음 
# except ValueError:
# 	print('Occured ValueError!')
# else:
# 	print('OK! - else out')
# finally:
# 	print('finally!')





















