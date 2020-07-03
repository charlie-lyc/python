import unittest
import employee_class
from unittest.mock import patch


class TestEmployee(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('Set Up Class')

	@classmethod
	def tearDownClass(cls):
		print('Tear Down Class')

	def setUp(self):
		print('Set Up')
		self.emp1 = employee_class.Employee('Corey', 'Schafer', 50000)
		self.emp2 = employee_class.Employee('Sue', 'Smith', 60000)

	def tearDown(self):
		print('Tear Down\n')

	def test_email(self):
		print('Test email')
		self.assertEqual(self.emp1.email, 'Corey.Schafer@email.com')
		self.assertEqual(self.emp2.email, 'Sue.Smith@email.com')
		self.emp1.first = 'John'
		self.emp2.first = 'Jane'
		self.assertEqual(self.emp1.email, 'John.Schafer@email.com')
		self.assertEqual(self.emp2.email, 'Jane.Smith@email.com')

	def test_fullname(self):
		print('Test fullname')
		self.assertEqual(self.emp1.fullname, 'Corey Schafer')
		self.assertEqual(self.emp2.fullname, 'Sue Smith')
		self.emp1.first = 'John'
		self.emp2.first = 'Jane'
		self.assertEqual(self.emp1.fullname, 'John Schafer')
		self.assertEqual(self.emp2.fullname, 'Jane Smith')

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

	def test_monthly_schedule(self):
		print('Test monthly_schedule')
		### Context manager
		with patch('employee_class.requests.get') as mocked_get:
			### Test when response.ok == True
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'
			schedule = self.emp1.monthly_schedule('May')
			mocked_get.assert_called_with('http://company.com/Schafer/May')
			self.assertEqual(schedule, 'Success')
			### Test when response.ok == False
			mocked_get.return_value.ok = False
			schedule = self.emp2.monthly_schedule('June')
			mocked_get.assert_called_with('http://company.com/Smith/June')
			self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
	unittest.main()










