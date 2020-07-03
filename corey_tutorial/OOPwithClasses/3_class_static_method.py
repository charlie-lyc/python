# Class Methods and Static Methods

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@example.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Charlie', 'Lee', 90000)
emp_2 = Employee('Test', 'User', 50000)
print(Employee)
print(emp_1)
print(emp_2)
print()

emp_1.set_raise_amount(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

Employee.set_raise_amount(1.06)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()


emp_3_str = 'John-Doe-70000'
emp_4_str = 'Steve-Smith-30000'
emp_5_str = 'Jane-Doe-90000'
emp_3 = Employee.from_string(emp_3_str)
emp_4 = Employee.from_string(emp_4_str)
emp_5 = Employee.from_string(emp_5_str)
print(emp_3.__dict__)
print(emp_4.__dict__)
print(emp_5.__dict__)
print()

### TypeError: from_string() missing 1 required positional argument: 'emp_str'
# Employee.from_string()
### NameError: name 'emp_6' is not defined
# emp_6.from_string(emp_3_str)
### No Error, no execution    
# emp_5.from_string(emp_4_str)

import datetime

my_date = datetime.date(2019, 10, 21)
print(Employee.is_workday(my_date))
print()


 


