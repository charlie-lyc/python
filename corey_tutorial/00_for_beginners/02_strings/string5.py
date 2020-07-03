greeting = 'Hello'
name = 'Michael'

message1 = '%s, %s. Welcome!' % (greeting, name)
message2 = greeting + ', ' + name + '. Welcome!'
message3 = f'{greeting}, {name.upper()}. Welcome!'
message4 = '{}, {}. Welcome!'.format(greeting, name.upper())

print(message1)
print(message2)
print(message3)
print(message4)
