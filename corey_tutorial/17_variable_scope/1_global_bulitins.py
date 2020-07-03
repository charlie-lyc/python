'''
LEGB : Local < Enclosing < Global < Built-in

'''
#################### Example01 ####################

x = 'global x'

def test():
	y = 'local y'
	print(x)
	# print(y)

test()
print(x)

### NameError: name 'y' is not defined
# print(y)

#################### Example02 ####################

# x = 'global x'

# def test():
# 	x = 'local x'
# 	print(x)

# test()
# print(x)

#################### Example03 ####################

# x = 'global x'

# def test():
# 	global x
# 	x = 'local x'
# 	print(x)

# test()
# print(x)

#################### Example04 ####################

# def test():
# 	global x
# 	x = 'local x'
# 	print(x)

# test()
# print(x)

#################### Example05 ####################

# def test():
# 	x = 'local x'
# 	print(x)

# test()
### NameError: name 'x' is not defined
# print(x)

#################### Example06 ####################

# def test(z):
# 	x = 'local x'
# 	print(z)

# test('local z')
### NameError: name 'z' is not defined
# print(z)

#################### Example07 ####################

# m = min([5, 1, 4, 2, 3])
# print(m)
# print()

import builtins

# print(builtins)
# print()
# print(dir(builtins))

#################### Example08 ####################

# def min():
# 	pass

### TypeError: min() takes 0 positional arguments but 1 was given
# m = min([5, 1, 4, 2, 3])
# print(m)

#################### Example09 ####################

# def my_min():
# 	pass

# m = min([5, 1, 4, 2, 3])
# print(m)


