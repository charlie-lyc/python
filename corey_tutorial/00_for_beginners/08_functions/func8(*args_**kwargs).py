def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info()
print()

student_info(courses, info)
print()

student_info(*courses, **info)
