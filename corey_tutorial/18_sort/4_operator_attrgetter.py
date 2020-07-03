import operator

class Employee():

	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
		return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]
print(employees)
print()

sorted_employees1 = sorted(employees, key=operator.attrgetter('name'))
sorted_employees2 = sorted(employees, key=operator.attrgetter('age'))
sorted_employees3 = sorted(employees, key=operator.attrgetter('salary'))
print(sorted_employees1)
print(sorted_employees2)
print(sorted_employees3)
print()
