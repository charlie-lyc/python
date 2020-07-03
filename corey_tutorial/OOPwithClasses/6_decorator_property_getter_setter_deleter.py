# Property Decorators - Getter or Setter, and Deleter

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def fullname(self):
        if self.first == None or self.last == None:
            return None
        else:
            return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        if self.first == None or self.last == None:
            return None
        else:    
            return '{}.{}@exmaple.com'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        if self.first == None or self.last == None:
            return None
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

print(emp_1)
print()


### TypeError: 'str' object is not callable
# print(emp_1.fullname())
# print(emp_1.email())
print(emp_1.fullname)
print(emp_1.email)
print()
emp_1.first = 'Jim'
emp_1.last = 'Carey'
print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
print(emp_1.email)
print()


### Set fullname by assignment
emp_1.fullname = 'Charlie Lee'
print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
print(emp_1.email)
print()


### Delete fullname by del instruction
del emp_1.fullname
print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
print(emp_1.email)
print()


### AttributeError: 'NoneType' object has no attribute 'setter'
# emp_1.fullname.setter
# emp_1.fullname.deleter
# emp_1.fullname.setter()
# emp_1.fullname.deleter()
