import unittest
import calc_module


class TestCalc(unittest.TestCase):

	def test_add(self):
		self.assertEqual(calc_module.add(10, 5), 15)
		self.assertEqual(calc_module.add(-10, 10), 0)
		self.assertEqual(calc_module.add(-10, -5), -15)

	def test_subtract(self):
		self.assertEqual(calc_module.subtract(10, 5), 5)
		self.assertEqual(calc_module.subtract(-10, 10), -20)
		self.assertEqual(calc_module.subtract(-10, -5), -5)

	def test_multiply(self):
		self.assertEqual(calc_module.multiply(10, 5), 50)
		self.assertEqual(calc_module.multiply(-10, 10), -100)
		self.assertEqual(calc_module.multiply(-10, -5), 50)

	def test_divide(self):
		self.assertEqual(calc_module.divide(10, 5), 2)
		self.assertEqual(calc_module.divide(-10, 10), -1)
		self.assertEqual(calc_module.divide(-10, -5), 2)
		### In case of Float
		self.assertEqual(calc_module.divide(5, 2), 2.5)
		### In case of Raise Error
		self.assertRaises(ValueError, calc_module.divide, 10, 0)
		### AssertionError: ValueError not raised by divide
		# self.assertRaises(ValueError, calc_module.divide, 10, 5)
		### .F..
		### ======================================================================
		### FAIL: test_divide (__main__.TestCalc)
		### ----------------------------------------------------------------------
		### Traceback (most recent call last):
		###   File "/Users/charlie/Documents/CoreySchafer_PythonTutorial/20_unittest_module/3_test_calc_assertRaises.py", line 31, in test_divide
		###     self.assertRaises(ValueError, calc_module.divide, 10, 5)
		### AssertionError: ValueError not raised by divide
		### ----------------------------------------------------------------------
		### Ran 4 tests in 0.001s
		### FAILED (failures=1)


if __name__ == '__main__':
	unittest.main()


