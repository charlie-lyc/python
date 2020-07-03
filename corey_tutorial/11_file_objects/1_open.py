### Context Managers : Read
with open('test.txt', 'r') as f:
	print(f)
	# <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
	print()
	print(dir(f))
	print()
	print(help(f))
	print()
	print(f.name)
	print(f.mode)
	print(f.encoding) # Default
f.close()
print()


### The Basics : Read
f = open('test.txt', 'r')
print(f.name)
print(f.mode)
print(f.encoding) # Default
print()
print(f.read())
print(f.closed) # Test whether a 'f(ile)' is closed.
print()
f.close()
print(f.closed) # Test again.
print()

### ValueError: I/O operation on closed file.
# print(f.read()) 


### Other Modes
## Write
# f = open('test.txt', 'w')
## Append
# f = open('test.txt', 'a')
## Read + Write
# f = open('test.txt', 'r+')


