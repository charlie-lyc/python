# Special(Magic/Dunder) Methods

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@example.com'

        Employee.num_of_emps += 1
    ### Special Method #####################################
    ## feature prioity 1
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)   
    ## feature prioity 2
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
    ### Instance Method ####################################
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    ### Class method #######################################
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    ### Static method ######################################
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # or Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1 = Employee('Charlie', 'Lee', 80000)
emp_2 = Employee('Test', 'User', 50000)

print(emp_1)
print()

print(Employee.__str__(emp_1))
print(Employee.__repr__(emp_1))
print()

print(emp_1.__str__())
print(emp_1.__repr__())
print()

print(str(emp_1))
print(repr(emp_1))
print()

print(Employee.__add__(emp_1, emp_2))
print(emp_1.__add__(emp_2))
print(emp_2.__add__(emp_1))
print(emp_1 + emp_2)
### NameError: name 'add' is not defined
# print(add(emp_1, emp_2))
print()

### including 1 space
print(len(emp_1))
print(Employee.__len__(emp_1))
print(emp_1.__len__())
print()


### Example of Special Methods(I)
print(1 + 2)
print(int.__add__(1, 2))
print('a' + 'b')
print(str.__add__('a', 'b'))
print()

### Example of Special Methods(II)
print(len('test'))
print('test'.__len__())
print()






 



