import unittest
import calc_module


class TestCalc(unittest.TestCase):

	### OK case.
	def test_add(self):
		result = calc_module.add(10, 5)
		self.assertEqual(result, 15)
	### .
	### ----------------------------------------------------------------------
	### Ran 1 test in 0.000s
	### OK

	### Not run in tests and skipped case.
	### Every name starts with 'test_' and ends with its own function.
	### (like 'add', 'subtract', 'multiply', 'divide')	
	# def add_test(self):
	# 	result = calc_module.add(10, 5)
	# 	self.assertEqual(result, 15)
    ###
	### ----------------------------------------------------------------------
	### Ran 0 tests in 0.000s
	### OK

	### Failed case.
	# def test_add(self):
	# 	result = calc_module.add(10, 5)
	# 	self.assertEqual(result, 14)
	### F
	### ======================================================================
	### FAIL: test_add (__main__.TestCalc)
	### ----------------------------------------------------------------------
	### Traceback (most recent call last):
	###   File "/Users/charlie/Documents/CoreySchafer_PythonTutorial/20_unittest_module/1_test_calc.py", line 29, in test_add
	###     self.assertEqual(result, 14)
	### AssertionError: 15 != 14
	# ----------------------------------------------------------------------
	# Ran 1 test in 0.001s
	# FAILED (failures=1)


# In Terminal:
# python 1_test_calc_TestCase.py
# (No error message... but no result of execution... because this is module file not executable file)

# python -m unittest 1_test_calc_TestCase.py
# AttributeError: 'module' object has no attribute 'py'

# python3 -m unittest 1_test_calc_TestCase.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK

if __name__ == '__main__':
	unittest.main()

# In Terminal:
# python 1_test_calc_TestCase.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK

# Build in SublimeText: [ command + b ]
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK



