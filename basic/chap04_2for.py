# chapter04-02

# FOR statement : core of coding

########################
#  for in <collection> #
#  	 <loop body>       #
########################

for v1 in range(10):
	print('v1 :', v1)
print()

for v2 in range(1, 11):
	print('v2 :', v2)
print()

for v3 in range(1, 11, 2):
	print('v3 :', v3)
print()

for v4 in range(10, 1, -1):
	print('v4 :', v4)
print()


# sum of 1 ~ 100
sum1 = 0
for v in range(1, 101):
	sum1 += v
print('sum of 1 ~ 100 :', sum1)
print()

# internal function
print('sum of 1 ~ 100 :', sum(range(1,101)))
print('sum of 1 ~ 100 :', sum(range(2,101), 1)) # start : 1
print('sum of 1 ~ 10 :', sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print()
print(type(range(1, 101))) # <class 'range'>
print(dir(range(1, 101))) # __iter__
print()

# sum of 4 multiple in 1 ~ 100
print('sum of 4 multiples in 1 ~ 100 :', sum(range(4,101,4)))
print('sum of 4 multiples in 1 ~ 100 :', sum(range(8,101,4), 4)) # start : 4
print()


### Iterable Data Type : string, list, tuple, set, dictionary
### Iterable Functions : range(), reversed(), enumerate(), filter(), map(), zip()

# example01
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
for n in names:
	print('You are {}.'.format(n))
print()

# example02
lotto_numbers = [11, 19, 21, 28, 36, 37]
for n in lotto_numbers:
	print('Current number :', n)
print()

# example03
word = 'Beautiful'
for c in word:
	print('Character :', c)
print()

# example04
my_info = {
	'name': 'Lee',
	'age': 33,
	'city': 'Seoul'
}
for info in my_info:
	print('info :', info)
print()
for key in my_info: # 앞선 for문을 통해 딕셔너리에 적용하면 키가 반환된다는 것을 알게 되었으므로
	print('info :', my_info[key])
print()

# example05
for k in my_info.keys():
	print('key :', k)
print()
for v in my_info.values():
	print('value :', v)
print()
for i in my_info.items():
	print('item :', i)
print()

# example06
name = 'PineAppLE'
for n in name:
	if n.isupper():
		print(n, end='')
	else:
		print(n.upper(), end='')
print()

# Break : sequential search or linear search
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
	if num == 34:
		print('Found : 34!')
		break # 대상을 찾은 이후에 쓸데 없이 계속 검색을 할 필요가 없다.
	else:
		print('Not Found :', num)
print()

# Continue
lt = ['1', 2, 5, True, 4.3, complex(4)]
for v in lt:
	if type(v) is bool:
		continue
	print('Current type :', type(v))
	print('Multiply by 2 :', v * 2)
print()

# FOR ELSE statement
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
	if num == 49:
		print('Found : 49!')
		break
else:
	print('Not Found : 49')
print()

# multiplication table
for i in range(1, 10):
	for j in range(1, 10):
		# print('%i * %i = %2i' % (j, i, j * i), end='\t')
		print('{} * {} = {:2}'.format(j, i, j * i), end='\t')
	print()
print()

# Reverse I
sentence = 'I love you'
repeat_sentence = ''
reverse_sentence =''

for char in sentence:
	repeat_sentence = repeat_sentence + char
print('Repeat sentence :', repeat_sentence)
print()

for char in sentence:
	reverse_sentence = char + reverse_sentence
print('Reverse sentence :', reverse_sentence)
print()


# Reverse II
name2 = 'Aceman'
print('Reversed :', reversed(name2))
print('List :', list(reversed(name2)))
print('Tuple :', tuple(reversed(name2)))
print('Set :', set(reversed(name2))) # 순서x
print()

for char in list(reversed(name2)):
	print(char, end='')








