message = 'hellO worlD'
m1, m2 = message.split(' ')


print(message.lower())
print(message.upper())
print(m1.capitalize(), m2.capitalize())
print()

print(message.count('hellO'))
print(message.count('llo'))
print(message.count('l'))
print()

# "find()" : Return the value of the index from the string
# where the first letter of a string that you find starts
# As a result, below returns 6
print(message.find('worlD'))
# Below returns 0
print(message.find('hell'))
print()

# These return -1, because there is no string that you find
print(message.find('universe'))
print(message.find('world'))
