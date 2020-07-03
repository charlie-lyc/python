# Pythonic1
def hello(greet):
    return f'{greet} functions!'

print(hello('Hi'))
print()


# Pythonic2
def hello(greet):
    return '{} functions!'.format(greet)

print(hello('Hi'))
print()


# Other options
def hello(greet):
    return greet + ' functions!'

print(hello('Hi'))
print()


def hello(greet):
    return '%s functions!' % greet

print(hello('Hi'))
print()


def hello(greet):
    return greet, 'functions!'

print(hello('Hi'))
print()
a, b = hello('Hi')
print(a, b)




