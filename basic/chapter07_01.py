## chapter07-01

## Exception
##########################################################################################
# SyntaxError, ZeroDivisionError, NameError, IndexError, TypeError,  ValueError, KeyError #
##########################################################################################
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


############### IndexError ###############



















