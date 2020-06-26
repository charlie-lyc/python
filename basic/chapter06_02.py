## chapter06-02

## Module < Package
## 함수, 변수, 클래스 등 파이썬 구성 요소 들을 모아놓은 파일

############### example01 ###############

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

def power(x, y):
	return x ** y

# print('-' * 15)
# print('called! inner!')
# print(add(5, 5))
# print(subtract(15, 5))
# print(multiply(5, 5))
# print(divide(10, 2))
# print(power(5, 3))
# print('-' * 15)

if __name__ == '__main__': # 본 파일(__name__)이 실행파일(__main__)일 때 아래와 같이 실행된다. 즉, 모듈파일일 때는 실행되지 않는다.
	print('-' * 15)
	print('called! __main__')
	print(add(5, 5))
	print(subtract(15, 5))
	print(multiply(5, 5))
	print(divide(10, 2))
	print(power(5, 3))
	print('-' * 15)


