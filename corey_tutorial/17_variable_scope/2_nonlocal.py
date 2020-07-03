'''
LEGB : Local, Enclosing, Global, Built-in

'''
#################### Example01 ####################

def outer():
	x = 'outer x'

	def inner():
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()

#################### Example02 ####################

# def outer():
# 	x = 'outer x'

# 	def inner():
# 		print(x)

# 	inner()
# 	print(x)

# outer()

#################### Example03 ####################

# def outer():

# 	def inner():
# 		x = 'inner x'
# 		print(x)

# 	inner()
# 	print(x)

### NameError: name 'x' is not defined
# outer()

#################### Example04 ####################

# def outer():
# 	x = 'outer x'

# 	def inner():
# 		nonlocal x
# 		x = 'inner x'
# 		print(x)

# 	inner()
# 	print(x)

# outer()

#################### Example05 ####################

# x = 'global x'

# def outer():
# 	x = 'outer x'

# 	def inner():
# 		nonlocal x
# 		x = 'inner x'
# 		print(x)

# 	inner()
# 	print(x)

# outer()
# print(x)

#################### Example06 ####################

# x = 'global x'

# def outer():
# 	x = 'outer x'

# 	def inner():
# 		print(x)

# 	inner()
# 	print(x)

# outer()
# print(x)

#################### Example07 ####################

# x = 'global x'

# def outer():

# 	def inner():
# 		print(x)

# 	inner()
# 	print(x)

# outer()
# print(x)

