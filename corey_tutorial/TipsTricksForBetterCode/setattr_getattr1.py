
class Person:
    pass


person = Person()


first_key = 'first'
first_val = 'Corey'
setattr(person, first_key, first_val)
print(getattr(person, first_key))
print(person.first)
print()


setattr(person, 'last', 'Schafer')
print(getattr(person, 'last'))
print(person.last)
print()


person.first = 'Chalie'
person.last = 'Lee'
print(person.first)
print(person.last)
print()


### AttributeError
# first_key = 'first'
# first_val = 'Corey'
# person.first_key = first_val
# print(person.first)


# print(dir(setattr))
# print(help(setattr))
# print()
# print(dir(getattr))
# print(help(getattr))
