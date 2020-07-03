print('Imported my_module...')
print()

def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1


### For testing find_index() function
test = 'Test String'
# print(find_index(test, 'e'))
