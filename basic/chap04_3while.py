# chapter04-03

# WHILE statement

####################
# while <expr>     #
# 	<statement(s)> #
####################

# example01 : <<< Cancel : control + c >>>
# n = 5
# while n > 0:
# 	print(n) 

# example02
a = ['foo', 'bar', 'baz']
while a:
	print(a.pop())
print()

# example03 : break
n = 5
while n > 0:
	n -= 1
	if n == 2:
		break
	print(n)
print('Loop Ended.')
print()

# example04 : continue
m = 5
while m > 0:
	m -= 1
	if m == 2:
		continue
	print(m)
print('Loop Ended.')
print()

# example05 : nested if
i = 1
while i <= 10:
	print('i :', i)
	if i == 6:
		break
	i += 1
print()

# example06 : WHILE ELSE statement
n = 10
while n > 0:
	n -= 1
	print(n)
else:
	print('Else out.')
print()

# example07
a = ['foo', 'bar', 'baz', 'qux']
s = 'kim'
i = 0
while i < len(a):
	if a[i] == s:
		break
	i += 1
else:
	print(s, 'is not fount in list a.')
print()

# Infinite Iteration : <<< Cancel : control + c >>>
# while True:
# 	print('Foo')

# example08
a = ['foo', 'bar', 'baz', 'qux']
while True:
	if not a:
		break
	print(a.pop())
print()

a = ['foo', 'bar', 'baz', 'qux']
while a:
	print(a.pop())


























