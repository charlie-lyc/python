import unittest
from employee_class import Employee


class TestEmployee(unittest.TestCase):

	def test_email(self):
		emp1 = Employee('Corey', 'Schafer', 50000)
		emp2 = Employee('Sue', 'Smith', 60000)
		self.assertEqual(emp1.email, 'Corey.Schafer@email.com')
		self.assertEqual(emp2.email, 'Sue.Smith@email.com')
		emp1.first = 'John'
		emp2.first = 'Jane'
		self.assertEqual(emp1.email, 'John.Schafer@email.com')
		self.assertEqual(emp2.email, 'Jane.Smith@email.com')

	def test_fullname(self):
		emp1 = Employee('Corey', 'Schafer', 50000)
		emp2 = Employee('Sue', 'Smith', 60000)
		self.assertEqual(emp1.fullname, 'Corey Schafer')
		self.assertEqual(emp2.fullname, 'Sue Smith')
		emp1.first = 'John'
		emp2.first = 'Jane'
		self.assertEqual(emp1.fullname, 'John Schafer')
		self.assertEqual(emp2.fullname, 'Jane Smith')

	def test_apply_raise(self):
		emp1 = Employee('Corey', 'Schafer', 50000)
		emp2 = Employee('Sue', 'Smith', 60000)
		emp1.apply_raise()
		emp2.apply_raise()
		self.assertEqual(emp1.pay, int(50000 * 1.05))
		self.assertEqual(emp2.pay, int(60000 * 1.05))
		emp1.pay = 70000
		emp2.pay = 80000
		emp1.apply_raise()
		emp2.apply_raise()
		self.assertEqual(emp1.pay, int(70000 * 1.05))
		self.assertEqual(emp2.pay, int(80000 * 1.05))


if __name__ == '__main__':
	unittest.main()


	