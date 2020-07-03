
######################## Example01 ########################

# try:
# 	f = open('test_file.txt')
# 	# ValueError: I/O operation on closed file.
# 	# f.close()
# except FileNotFoundError as e:
# 	print(e)
# except Exception as e:
# 	print(e)
# else:
# 	print(f.read())
# 	f.close()

######################## Example02 ########################

# try:
# 	f = open('test_file.txt')
# except FileNotFoundError as e:
# 	print(e)
# except Exception as e:
# 	print(e)
# else:
# 	print(f.read())
# 	f.close()
# finally:
# 	print('Executing Finally...')

######################## Example03 ########################

try:
	f = open('currupt_file.txt')
	if f.name == 'currupt_file.txt':
		# Intentionally rasie error for specific purpose.
		raise Exception
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print('Error!')
else:
	print(f.read())
	f.close()
finally:
	print('Executing Finally...')

	

