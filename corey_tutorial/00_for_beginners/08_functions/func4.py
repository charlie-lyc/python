def hello():
    return 'Hello functions!'

print(hello())
print(hello())
print(hello())
print()


def hello():
    return 'Hello functions!'

print(hello()*3)
print()


def hello():
    return 'Hello functions!'

print((hello()+'\n') * 3, end='')
print()


def hello(num):
    return ('Hello functions!'+'\n') * num

print(hello(3), end='')
print()
