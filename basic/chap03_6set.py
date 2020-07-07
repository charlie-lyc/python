# chapter03-06

# Set
# *** 순서x ***, *** 중복x ***, 수정o, 삭제o

# declaration
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}
print('a :', type(a), a)
print('b :', type(b), b)
print('c :', type(c), c)
print('d :', type(d), d)
print('e :', type(e), e)
print('f :', type(f), f)
print()

# tuple transformation
t = tuple(b)
print('t :', type(t), t)
print('t[0] :', t[0])
print('t[1:3] :', t[1:3])
print()

# list transformation
l1 = list(c)
l2 = list(e)
print('l1 :', type(l1), l1)
print('l2 :', type(l2), l2)
print()

# length
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
print()

# function
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print('s1 & s2 :', s1 & s2)
print('intersection of s1 and s2 :', s1.intersection(s2))  # 교집합
print('s1 | s2 :', s1 | s2)
print('union of s1 and s2 :', s1.union(s2))  # 합집합
print('s1 - s2 :', s1 - s2)
print('difference of s1 and s2 :', s1.difference(s2))  # 차집합
print()
print('is disjoint? :', s1.isdisjoint(s2))  # 중복 유무 확인 : 결과값이 False일때 중복되는 부분이 있음음 의
print('is subset? (s1->s2) :', s1.issubset(s2))  # 부분 집합 여부 확인
print('is subset? (s2->s1) :', s2.issubset(s1))
print('is superset? (s1->s2) :', s1.issuperset(s2))
print('is superset? (s2->s1) :', s2.issuperset(s1))
print()

# add
s1 = set([1, 2, 3, 4])
print('s1 ;', s1)
s1.add(5)  # List : append
print('s1 ;', s1)
s1.update([6, 8, 9])  # List : extend
print('s1 ;', s1)
print()

# deletion
print('s1 ;', s1)
s1.remove(2)
print('s1 ;', s1)
# s1.remove(7) # KeyError: 7
s1.discard(3)
print('s1 ;', s1)
s1.discard(7)  # No Error
print('s1 ;', s1)
s1.clear()  # empty set
print('s1 ;', s1)
