# chapter02-1

import sys

# print function
print('python start!')
print('''python start!''')
print("""python start!""")
print()

# separator option
print('p', 'y', 't', 'h', 'o', 'n', sep='')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')
print('')

# end option
print('Welcome to', end=' ')
print('IT news', end=' ')
print('Web site')
print()

# file option
print('learn python', file=sys.stdout)
# print('learn python', file='test.txt')
print()

# format (d : 3, s : 'python', f; 3.14)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()

# %s
print('%10s' % 'nice')
print('{:>10}'.format('nice'))
print()
print('%-10s' % 'nice')
print('{:10}'.format('nice'))
print()
print('{:_>10}'.format('nice'))
print('{:$>10}'.format('nice'))
print('{:^10}'.format('nice'))
# print('{:10_}'.format('nice')) # XXX
print()
print('%5s' % 'pythonstudy')
print('%.5s' % 'pythonstudy')
# print('%5.s' % 'nice') # XXX
print()
print('{:10}'.format('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))
print('{:.10}'.format('pythonstudy'))
print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))
print()
print('%4d' % 42)
print('%4d' % 424242)
print('{:4d}'.format(42))
print('{:4d}'.format(424242))
print()

# %f
print('%f' % 3.1442)
print('%8f' % 3.1442)
print('%4f' % 3.1442)
print('%.2f' % 3.1442)
print('%.8f' % 3.1442)
print('%8.2f' % 3.1442)
print('%8.5f' % 3.1442)
print('%08.5f' % 3.1442)
print()
print('{:f}'.format(3.1442))
print('{:8f}'.format(3.1442))
print('{:4f}'.format(3.1442))
print('{:.2f}'.format(3.1442))
print('{:.8f}'.format(3.1442))
print('{:8.2f}'.format(3.1442))
print('{:8.5f}'.format(3.1442))
print('{:08.5f}'.format(3.1442))
print()

# list type !!!
print('Product: %10s, Price per unit: %10.2f.' % ('Apple', 5.243))
print('Product: {0:10s}, Price per unit: {1:10.2f}.'.format('Apple', 5.243))
print('Product: {:_>10s}, Price per unit: {:010.2f}.'.format('Apple', 5.243))
print('Price per unit: {1:010.2f}, Product: {0:_>10s}.'.format('Apple', 5.243))
print()

# dict type !!!
print('Product: %(name)10s, Price per unit: %(price)10.2f.' % ({'name': 'Apple', 'price': 5.243}))
print('Product: {name:10s}, Price per unit: {price:10.2f}.'.format(name='Apple', price=5.243))
