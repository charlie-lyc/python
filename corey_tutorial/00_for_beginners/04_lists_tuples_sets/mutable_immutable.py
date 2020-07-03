# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)
list_1[0] = 'Art'
print()
print(list_1)
print(list_2)
print()


# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
# tuple_1[0] = 'Art' # TypeError
print()
print(tuple_1)
print(tuple_2)
print()


# Sets
cs_courses = {'History', 'Math', 'Physics', 'ComSci', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design', 'Design'}
print(cs_courses) # random order, reomve duplicates
print(art_courses)
print()
print('Math' in cs_courses)
print('Physics' in art_courses)
print()
print(cs_courses.intersection(art_courses)) # intersection()
print(cs_courses.union(art_courses)) # union()
print()


# Empty Lists
empty_list_1 = []
empty_list_2 = list()
print(type(empty_list_1))
print(type(empty_list_2))
print()


# Empty Tuples
empty_tuple_1 = ()
empty_tuple_2 = tuple()
print(type(empty_tuple_1))
print(type(empty_tuple_2))
print()


# Empty Dictionaries
empty_dictionary_1 = {}
empty_dictionary_2 = dict()
print(type(empty_dictionary_1))
print(type(empty_dictionary_2))
print()


# Empty Sets
empty_set_1 = set()
empty_set_2 = {} # => This isn't right! It's a dict
print(type(empty_set_1))
print(type(empty_set_2))
print()






