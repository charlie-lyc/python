# Iterator in Iterators
names = ['Peter Parker', 'Clark Kent', 'Wade Wilsom', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
identities = zip(names, heroes)

print(identities)
### Python 2.7 
# [
#     ('Peter Parker', 'Spiderman'), 
#     ('Clark Kent', 'Superman'), 
#     ('Wade Wilsom', 'Deadpool'), 
#     ('Bruce Wayne', 'Batman')
# ]
### python 3.8
# <zip object at 0x7f8088d0fdc0>
print(list(identities))
### Python 3.8
# [
#     ('Peter Parker', 'Spiderman'), 
#     ('Clark Kent', 'Superman'), 
#     ('Wade Wilsom', 'Deadpool'), 
#     ('Bruce Wayne', 'Batman')
# ]
print()

for identity in identities:
    print('{} is actually {}!'.format(identity[0], identity[1]))

