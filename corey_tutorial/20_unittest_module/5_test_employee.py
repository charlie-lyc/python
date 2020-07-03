import unittest
from employee_class import Employee


class TestEmployee(unittest.TestCase):

	def test_email(self):
		emp1 = Employee('Corey', 'Schafer', 50000)
		self.assertEqual(emp1.email, 'Corey.Schafer@email.com')

	def test_fullname(self):
		emp1 = Employee('Corey', 'Schafer', 50000)
		self.assertEqual(emp1.fullname, 'Corey Schafer')

	def test_apply_raise(self):
		emp1 = Employee('Corey', 'Schafer', 50000)
		emp1.apply_raise()
		self.assertEqual(emp1.pay, int(50000 * 1.05))


if __name__ == '__main__':
	unittest.main()