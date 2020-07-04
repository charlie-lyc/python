# Inheritance and Subclasses

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


dev_1 = Developer('Charlie', 'Lee', 80000, 'Python')
dev_2 = Developer('Test', 'User', 50000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(issubclass(Manager, Employee))
print(issubclass(Employee, Manager))
print(issubclass(Manager, Developer))
print(issubclass(Developer, Manager))
print()

print(isinstance(mgr_1, Manager))
print(isinstance(dev_1, Developer))
print(isinstance(mgr_1, Employee))
print(isinstance(dev_1, Employee))
print()

print(mgr_1.email)
mgr_1.print_emps()
print()

mgr_1.add_emp(dev_2)
mgr_1.print_emps()
print()

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
print()

print(dev_1.email)
print(dev_1.prog_lang)
print()

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print()

print(mgr_1.pay)
mgr_1.apply_raise()
print(mgr_1.pay)
print()

print(dev_1.email)
print(dev_2.email)
print()


print(help(Employee))
print()
print(help(Developer))
print()
print(help(Manager))
print()


