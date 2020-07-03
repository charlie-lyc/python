
######################## Example01 ########################

try:
	f = open('testfile.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'testfile.txt'
# But too general!
except Exception: 
  # Custom message
	print('Oops, this file does not exist!')


######################## Example02 ########################

# try:
# 	f = open('test_file.txt')
# 	# NameError: name 'bad_var' is not defined
# 	var = bad_var
# except FileNotFoundError:
# 	print('This file does not exist!')
# except Exception:
# 	print("Something went wrong!")


######################## Example03 ########################

# try:
# 	f = open('test_file.txt')
# 	# NameError: name 'bad_var' is not defined
# 	var = bad_var
# except FileNotFoundError as e:
# 	# Error message from system
# 	print(e)
# except Exception as e:
# 	print(e)



