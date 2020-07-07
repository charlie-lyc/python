# chapter03-04

# Tuple : *** immutable ***
# 순서o, 중복o, *** 수정x*** , *** 삭제x ***

# declaration
a = ()
b = tuple()
c = (1)
d = (1,)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print()

# indexing
e = (11, 12, 13, 14)
f = (100, 1000, 'Ace', 'Base', 'Captain')
g = (100, 1000, ('Ace', 'Base', 'Captain'))
print('>>>>>')
print('e[1] :', e[1])
print('e[0] + f[1] :', e[0] + f[1])
print('f[-1] :', f[-1])
print('g[-1] :', g[-1])
print('g[-1][1] :', g[-1][1])
print('list(g[-1][1]) :', list(g[-1][1]))
print()

# correction
# d[0] = 1500 # TypeError: 'tuple' object does not support item assignment

# slicing
print('>>>>>')
print('f[:3] :', f[:3])
print('f[3:] :', f[3:])
print('g[2][1:3] :', g[2][1:3])
print()

# operation
print('>>>>>')
print('e + f :', e + f)
print('e * 3 :', e * 3)
print()

# function
a = [5, 2, 3, 1, 4, 2]
print('a :', a)
print('index of 3 :', a.index(3))
print('count of 2 :', a.count(2))
print()

# packing
t = ('foo', 'bar', 'baz', 'qux')
# t = 'foo', 'bar', 'baz', 'qux' # OK
print(t)
print(t[0])
print(t[-1])
print()

# unpacking
(x1, x2, x3, x4) = t
# x1, x2, x3, x4 = t # OK
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)
print()

# packing & unpacking practice
t1 = 1, 2, 3
t2 = 4,
x1, x2, x3 = t1
x4, x5, x6 = 4, 5, 6
print(t1)
print(t2)
print(x1, x2, x3)
print(x4, x5, x6)
print()

# Impossible
# print(t1.append(7))
# print(t1.remove(3))
