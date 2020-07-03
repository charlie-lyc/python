import unittest
import calc_module


class TestCalc(unittest.TestCase):

	def test_add(self):
		result = calc_module.add(10, 5)
		self.assertEqual(result, 15)
	
	def test_subtract(self):
		result = calc_module.subtract(10, 5)
		self.assertEqual(result, 5)

	def test_multiply(self):
		result = calc_module.multiply(10, 5)
		self.assertEqual(result, 50)

	def test_divide(self):
		result = calc_module.divide(10, 5)
		self.assertEqual(result, 2)


if __name__ == '__main__':
	unittest.main()

# In Terminal:
# python 2_test_calc_assertEqual.py
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.000s
# OK

# Build in SublimeText: [ command + b ]
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.000s
# OK


