message = 'hello world'

print(message[0])
print(message[10])
print(message[0:10])
print(message[0:11])
print(message[0:5])
print(message[:5])
print(message[6:11])
print(message[6:])
print()

print(message[-1:])
print(message[:-1])
print(message[-6:-1])
print(message[-6:])
print()

print(message[:])
print()

# not printed : end of range should not be 0
print(message[-12:0])
