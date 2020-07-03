student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci'], 'phone': '777-7777'}

del student['age'] # "del object" or "del(object)"
print(student)
print()

name = student.pop('name')
print(name)
print(student)
print()

print(len(student)) # the number of keys
print(student.keys()) # to see all keys
print(student.values()) # to see all values
print(student.items()) # to see all key and value pairs
print()

for key in student:
    print(key)
print()

for key in student.keys():
    print(key)
print()

for value in student.values():
    print(value)
print()

for item in student.items():
    print(item)
print()

for key, value in student.items():
    print(f'{key}: {value}')
print()


# for key, value in student: # ValueError
#     print(key, value)
# print()
