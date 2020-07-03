import unittest
from employee_class import Employee


class TestEmployee(unittest.TestCase):

	### 1
	@classmethod
	def setUpClass(cls):
		print('Set Up Class')

	### 11
	@classmethod
	def tearDownClass(cls):
		print('Tear Down Class')

	### 2, 5, 8
	def setUp(self):
		print('Set Up')
		self.emp1 = Employee('Corey', 'Schafer', 50000)
		self.emp2 = Employee('Sue', 'Smith', 60000)

	### 4, 7, 10
	def tearDown(self):
		print('Tear Down\n')

	### 6 
	def test_email(self):
		print('Test email')
		self.assertEqual(self.emp1.email, 'Corey.Schafer@email.com')
		self.assertEqual(self.emp2.email, 'Sue.Smith@email.com')
		self.emp1.first = 'John'
		self.emp2.first = 'Jane'
		self.assertEqual(self.emp1.email, 'John.Schafer@email.com')
		self.assertEqual(self.emp2.email, 'Jane.Smith@email.com')

	### 9
	def test_fullname(self):
		print('Test fullname')
		self.assertEqual(self.emp1.fullname, 'Corey Schafer')
		self.assertEqual(self.emp2.fullname, 'Sue Smith')
		self.emp1.first = 'John'
		self.emp2.first = 'Jane'
		self.assertEqual(self.emp1.fullname, 'John Schafer')
		self.assertEqual(self.emp2.fullname, 'Jane Smith')

	### 3
	def test_apply_raise(self):
		print('Test apply_raise')
		self.emp1.apply_raise()
		self.emp2.apply_raise()
		self.assertEqual(self.emp1.pay, int(50000 * 1.05))
		self.assertEqual(self.emp2.pay, int(60000 * 1.05))
		self.emp1.pay = 70000
		self.emp2.pay = 80000
		self.emp1.apply_raise()
		self.emp2.apply_raise()
		self.assertEqual(self.emp1.pay, int(70000 * 1.05))
		self.assertEqual(self.emp2.pay, int(80000 * 1.05))


if __name__ == '__main__':
	unittest.main()


	