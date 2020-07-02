## chapter08-01

## Built-in Functions
## 자주 사용하는 함수, 사용하다 보면 자연스럽게 숙달

###############################################################
# str(), int(), float(), list(), tuple(), dict(), set()       #
###############################################################
# type(), id(), len(), chr(), ord(), range()                  #
###############################################################
# abs(), round(), pow(), sum(), max(), min()                  # 
###############################################################
# all(), any(), enumerate(), sorted(), zip(), filter(), map() #
###############################################################

## type : 자료형 확인
print(type(3))
print(type([]))
print(type({}))
print(type(()))
print()


## id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(5))
print()
print(id(6))
print()


## len : 요소의 길이 반환
print(len('abcdefg'))
print(len([1, 2, 3, 4, 5, 6]))
print()


## chr : 아스키 -> 문자
## ord : 문자 -> 아스키
print(chr(67))
print(ord('C'))
print()


## range : 반복 가능한 객체(Iterable) 반환
print(range(1, 10, 2))
print(type(range(1, 10, 2)))
print(list(range(1, 10, 2)))
print()


## abs : 절대값 반환
print(abs(-3))
print()


## round : 반올림
print(round(6.5781))
print(round(6.5781, 2))
print()


## pow : 제곱값 반환
print(pow(2, 10))
print()


## sum : 반복 가능한 객체(Iterable) 합 반환
print(sum([6, 7, 8, 9, 10]))
print(sum(range(1, 101)))
print()


## max, min : 최대값, 최소값
print(max([1, 2, 3]))
print(max('python study')) # 아스키코드로 인식하여 가장 큰값 반환
print()
print(min([1, 2, 3]))
# print(min('python study')) # 가장 작은 값이 공백이어서 공백을 결과값으로 출력
print(min('pythonstudy'))
print()


## all : iterable 요소 검사(True or False), "and" 조건 
## 값 중에 0 또는 ''이 하나라도 있으면 false, 즉 각 요소 모두 True이면 True를 반환
print(all([1, 2, 0])) 
print(all([1, 2, '']))
print()


## any : iterable 요소 검사(True or False), "or" 조건
## 각 요소 중에 하나라도 True이면 True를 반환 
print(any([0, 0, 2]))
print(any([0, 0, 'a']))
print()


## enumerate : 인덱스 + iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
	print(i, name)
print()


## sorted : 반복 가능한 객체(Iterable) 정렬 후 반환
print(sorted([6, 7, 4, 3, 1, 2]))
print(sorted(['p', 'y', 't', 'h', 'o', 'n']))
print()


## zip : 반복 가능한 객체(Iterable)의 요소들을 묶어서 반환
print(zip([10, 20, 30], [40, 50, 60]))
print(type(zip([10, 20, 30], [40, 50, 60])))
print()
print(list(zip([10, 20, 30], [40, 50, 60]))) # [(10, 40), (20, 50), (30, 60)] : 인덱스별로 묶음
print(list(zip([10, 20, 30], [40, 50]))) # [(10, 40), (20, 50)] : 인덱스별로 묶음, 짝이 안 맞는 것은 버림
print()
print(type(list(zip([10, 20, 30], [40, 50, 60]))[0]))
print()


## filter : 반복 가능한 객체 요소로 부터 지정한 함수 조건에 맞는 값 추출

# def convert_position(x):
# 	return abs(x) > 2
# print(convert_position(-3))
# print(convert_position(-2))
# print(list(filter(convert_position, [-3, -2, -1, 0, 1, 2, 3])))
# print()

print(list(filter(lambda x: abs(x) > 2, [-3, -2, -1, 0, 1, 2, 3])))
print()


## map : 반복가능한 객체 요소에 대하여 지정한 함수 실행 후 추출

# def convert_abs(x):
# 	return abs(x)
# print(convert_abs(-3))
# print(list(map(convert_abs, [-3, -2, -1, 0, 1, 2, 3])))
# print()

print(list(map(lambda x: abs(x), [-3, -2, -1, 0, 1, 2, 3])))
print()



