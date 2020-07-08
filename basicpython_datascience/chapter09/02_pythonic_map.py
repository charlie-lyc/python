
import sys

# Map : sequence형 자료의 각 element에 대하여 동일한 function을 적용
example = [1, 2, 3, 4, 5]

# Atom에서 실행하면 자동으로 'def ~'형으로 변환
# f = lambda x : x ** 2
print(map(lambda x: x ** 2, example))
# <map object at 0x7fe068203250>
print()

print(list(map(lambda x: x ** 2, example)))
print()

print(list(map(lambda x, y: x + y, example, example)))
print()

# if 구문은 필터처럼 사용
print(list(map(lambda x: x ** 2 if x % 2 == 0 else x, example)))
print()

# print out 하기 위해서 list에 담아야 한다.
print(list(map(lambda x: x ** 2, example)))
print()

# 'map object' 자체로써 "__iter__"을 갖고있다.
# 리스트 등의 자료형이 되어야만 갖는 것이 아니다.
for i in map(lambda x: x ** 2, example):
    print(i)
print()

# 'map object' 자체로써 "__iter__"을 갖고있다.
result = map(lambda x: x ** 2, example)
print(result)
# <map object at 0x7f8537308a30>
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print()

# 오히려 단순 리스트에 담아버리면 객체의 속성을 잃어버린다.
# TypeError: 'list' object is not an iterator
# result = list(map(lambda x: x ** 2, example))
# print(next(result))


# 지속적인 궁금증이였는데 도대체 왜 자료형을 결정하여 반환하지 않고
# 결과를 메모리값에 그대로 두는가 ???
# 아래의 실행 결과를 보면 명확해 진다.
print(sys.getsizeof(example))  # 96
print(sys.getsizeof(map(lambda x: x ** 2, example)))  # 48
print(sys.getsizeof(list(map(lambda x: x ** 2, example))))  # 120
