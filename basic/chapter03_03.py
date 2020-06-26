# chapter03-03

# List : *** mutable ***, 'array' in other languages
# 순서o, 중복o, 수정o, 삭제o

# declaration
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# indexing
print('>>>>>')
print('d :', type(d), d)
print('d[1] :', d[1])
print('d[0] + d[1] + d[1] :', d[0] + d[1] + d[1])
print('d[-1] :', d[-1])
print('e[-1][1] :', e[-1][1])
print('list(e[-1][1]) : ', list(e[-1][1]))

# slicing
print('>>>>>')
print('d[0:3] :', d[0:3])
print('d[2:] :', d[2:])
print('e[-1][1:3] :', e[-1][1:3])

# operation
print('>>>>>')
print('c + d :', c + d)
print('c * 3 :', c * 3)
# print("'Test' + c[0] :", 'Test' + c[0])
print("'Test' + str(c[0]) :", 'Test' + str(c[0]))
print()

# compare
print(c)
print(c[:3] + c[3:])
print(c == c[:3] + c[3:])
print()

# identify : id()
temp = c
print(c)
print(temp)
print(id(temp))
print(id(c))
print()

# correction
print('>>>>>')
print('c :', c)
c[0] = 4
print('c :', c)
c[1:2] = ['a', 'b', 'c']
print('c :', c)
c[1] = ['a', 'b', 'c']
print('c :', c)
c[1:2] = [['a', 'b', 'c']]
print('c :', c)
c[1:3] = [['a', 'b', 'c']]
print('c :', c)
print()

# deletion
c[1:3] = []
print('c :', c)
del c[2]
print('c :', c)
print()

# function
a = [5, 2, 3, 1, 4]
print('a :', a)
a.append(10)
print('a :', a)
a.sort()
print('a :', a)
a.reverse()
print('a :', a)
print('index of 3 :', a.index(3)) # 인덱스를 구하는 함수
a.insert(2, 7)
print('a :', a)
a.reverse()
print('a :', a)
# del a[6] # 데이터 갯수가 많을 때 인덱스를 세는 것은 불편하거나 거의 불가능
a.remove(10) # 지우고 싶은 값을 바로 입력
print('a :', a)
print('pop of a :', a.pop()) # append의 역순으로 pop
print('a :', a)
print('pop of a :', a.pop())
print('a :', a)
print('count of 1 :', a.count(1)) # 갯수 구하기
print('count of 5 :', a.count(5))
ex = [8, 9]
a.extend(ex)
print('a :', a)
a.append(ex)
print('a :', a)

# iteration
while a:
    data = a.pop()
    print(data)


