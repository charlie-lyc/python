
names = ['Corey', 'Chris', 'Dave', 'Travis']

for index, name in enumerate(names):
    print(index, name)
print()

# start=0 : Default
for index, name in enumerate(names, start=1):
    print(index, name)
print()


index = 0
for name in names:
    print(index, name)
    index += 1
print()


print(dir(enumerate))
print()
print(help(enumerate))
