# chapter03-05

# Dictionary : key - value
# 범용적으로 가장 많이 사용
# *** 순서x ***, *** 키 중복x ***, 수정o, 삭제o

# declaration
a = {}
b = dict()
print(type(a))
print(type(b))
print()

a = {'name': 'Kim', 'phone': '01012345678', 'birth': '881231'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])
f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)
print('a :', type(a), a)
print('b :', type(b), b)
print('c :', type(c), c)
print('d :', type(d), d)
print('e :', type(e), e)
print('f :', type(f), f)
print()
print("a['name'] :", a['name'])
# print("a['name1'] :", a['name1']) # KeyError: 'name1'
print("a.get('name') :", a.get('name'))
# result is just 'None' : No Error(safer in development)
print("a.get('name1') :", a.get('name1'))
print('b[0] :', b[0])
print('b.get(0) :', b.get(0))
print("c['arr'] :", c['arr'])
print("c.get('arr') :", c.get('arr'))
print("f.get('City') :", f.get('City'))
print("f.get('Age') :", f.get('Age'))
print()

# add
a['address'] = 'Seoul'
print('a :', a)
a['rank'] = [1, 2, 3]
print('a :', a)
print()

# length
print('length of a :', len(a))
print('length of b :', len(b))
print('length of c :', len(c))
print('length of d :', len(d))
print()

# function : __iter__
"""
dict_keys
dict_values
dict_items
"""
print('keys of a :', a.keys())
print('keys of b :', b.keys())
print('keys of c :', c.keys())
print('keys of d :', d.keys())
print()
print("list of a's keys :", list(a.keys()))
print("list of b's keys :", list(b.keys()))
print("list of c's keys :", list(c.keys()))
print("list of d's keys :", list(d.keys()))
print()
print('values of a :', a.values())
print('values of b :', b.values())
print('values of c :', c.values())
print('values of d :', d.values())
print()
print("list of a's values :", list(a.values()))
print("list of b's values :", list(b.values()))
print("list of c's values :", list(c.values()))
print("list of d's values :", list(d.values()))
print()
print('items of a :', a.items())
print('items of b :', b.items())
print('items of c :', c.items())
print('items of d :', d.items())
print()
print("list of a's items :", list(a.items()))
print("list of b's items :", list(b.items()))
print("list of c's items :", list(c.items()))
print("list of d's items :", list(d.items()))
print()

# function
print('a :', a)
a.pop('name')
print('a :', a)
print()
print('c :', c)
c.pop('arr')
print('c :', c)
print()
print('f :', f)
f.popitem()
print('f :', f)
f.popitem()
print('f :', f)
f.popitem()
print('f :', f)
f.popitem()
print('f :', f)
f.popitem()
print('f :', f)
# f.popitem() # KeyError: 'popitem(): dictionary is empty'
# print('f :', f)
print()

# correction
print('a :', a)
a['address'] = 'Daejeon'
print('a :', a)
a.update(birth='990101')
print('a :', a)
temp1 = {'address': 'Busan'}
a.update(temp1)
print('a :', a)
temp2 = {'gpa': 3.0}
a.update(temp2)
print('a :', a)
print()

# etc
print("'birth' in a :", 'birth' in a)
print("'birthday' in a :", 'birthday' in a)
print("'City' in d :", 'City' in d)


