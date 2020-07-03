courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']


courses.append('Art')
print(courses)
print()

courses.insert(0, 'Art')
print(courses)
print()

courses.insert(0, courses_2)
print(courses)
print()

courses.extend(courses_2)
print(courses)
print()