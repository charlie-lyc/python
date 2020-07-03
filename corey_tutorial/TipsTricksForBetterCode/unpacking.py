# Normal
items = (1, 2)
print(items)
print()

# Unpacking
a, b = (1, 2)
print(a)
print(b)
print()

# If one is can be ignored
a, _ = (1, 2)
print(a)
print()

# Not equal the number of variales and values
a, b, *c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
print()

# Not equal and can be ignored
a, b, *_ = (1, 2, 3, 4, 5)
print(a)
print(b)
print()

# Also possible like this
a, b, *c, d = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
print(d)
print()

# Can use like this as well
a, b, *_, d = (1, 2, 3, 4, 5)
print(a)
print(b)
print(d)
print()

### ValueError
# a, b, c = (1, 2, 3, 4, 5)  # too many values
# a, b, c, d, e = (1, 2, 3)  # not enough values



