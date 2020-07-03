courses = ['History', 'Math', 'Physics', 'CompSci']


print(courses.index('CompSci'))
print()

print('Art' in courses)
print('Math' in courses)
print()

for course in courses:
    print(course)
print()

enum = enumerate(courses)
print(enum)
print()
print(type(enum))
print()
print(dir(enum))
print()
print(list(enum))
print()

c1, c2, c3, c4 = enumerate(courses)
print(c1, c2, c3, c4)
print()

for course in enumerate(courses):
    print(course)
print()

for index, value in enumerate(courses):
    print(index, value)
print()

for index, value in enumerate(courses, start=1):
    print(index, value)
print()

# print(courses.index('Art')) # ValueError


