student_1 = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}

print(student_1)
print(student_1['name'])
# print(student['phone']) # KeyError
print()

print(student_1.get('name'))
print(student_1.get('phone')) # None => kind of error but more stable than "student['phone']"
print(student_1.get('phone', 'Not Founded'))
print()

student_1['phone'] = '555-5555'
print(student_1.get('phone'))
student_1['name'] = 'Jane'
print(student_1)
print()

student_1.update({'name': 'Tom', 'age': 26, 'phone': '777-7777'})
print(student_1)
print()

student_2 = {1: 'John', 2: 25, 3: ['Math', 'Comsci']}
print(student_2[1])
print()


