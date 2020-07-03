
def hello(greet='Hello'):
    return '{} functions!'.format(greet)

print(hello())
print(hello('Hi'))
print()


def hello(greet, name='World'):
    return '{}, {}'.format(greet, name)

print(hello('Hi'))
print(hello('Hi', 'Charlie'))
print(hello(name='Hi', greet='Charlie'))
