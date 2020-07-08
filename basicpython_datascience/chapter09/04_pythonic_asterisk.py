# Asterisk : 단순곱셈, 제곱연산, 가변인자 활용
def asterisk_test1(a, *args):
    print(a, args)
    print(type(args))


asterisk_test1(1, 2, 3, 4, 5, 6)
print()


def asterisk_test2(a, **kwargs):
    print(a, kwargs)
    print(type(kwargs))


asterisk_test2(1, b=2, c=3, d=4, e=5, f=6)
print()

###############################################

# Asterisk : unpacking a container
# tuple, dict 등 자료형에 들어가 있는 값을 unpacking
# 함수의 입력값, zip 등에 유용하게 사용


def asterisk_test3(a, args):
    print(a, *args)
    print(type(args))


# 두개의 인자 중 하나인 튜플 : print out 할때 unpacking asterisk
asterisk_test3(1, (2, 3, 4, 5, 6))
# 1 2 3 4 5 6
print()

# 가변인자 중 하나인 튜플
asterisk_test1(1, (2, 3, 4, 5, 6))
# 1 ((2, 3, 4, 5, 6),)
print()

# 다수개의 가변인자들의 모음인 튜플 : 인자들로 입력될때 unpacking asterisk
asterisk_test1(1, *(2, 3, 4, 5, 6))
# 1 (2, 3, 4, 5, 6)
print()


def asterisk_test4(a, *args):
    print(a, args[0])
    print(type(args))


asterisk_test4(1, (2, 3, 4, 5, 6))
# 1 (2, 3, 4, 5, 6)
print()

##################################################

# Asterisk : unpacking a container (continue...)

# Example01
a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)
print()

data = ([1, 2], [3, 4], [5, 6])
print(data)
print(*data)
print()


# Example02
def Asterisk_test(a, b, c, d):
    print(a, b, c, d)


data = {'b': 1, 'c': 2, 'd': 3}

# TypeError: Asterisk_test() missing 2 required positional arguments: 'c' and 'd'
# Asterisk_test(10, data)

# Arguments unpackging : *
# KeyWord Arguments unpacking: **
Asterisk_test(10, **data)
print()

# Example03
for data in zip(([1, 2], [3, 4], [5, 6])):
    print(data)
print()
for data in zip(*([1, 2], [3, 4], [5, 6])):
    print(data)
