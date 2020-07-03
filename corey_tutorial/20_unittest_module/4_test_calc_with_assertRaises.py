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
		# self.assertRaises(ValueError, calc_module.divide, 10, 0)
		### Context manager
		with self.assertRaises(ValueError):
			calc_module.divide(10, 0)


if __name__ == '__main__':
	unittest.main()


	