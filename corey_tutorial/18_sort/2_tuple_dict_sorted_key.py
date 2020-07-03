
tup = (9, 1, 8, 2 ,7, 3, 6, 4, 5)

# Result of 'sorted()' must be "list"! 
sorted_tup = sorted(tup)
print('After  Sorting: ', sorted_tup)
print('Original Tuple: ', tup)
print()


di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}

### Sort only 'keys'
sorted_di = sorted(di)
print('After Sorting: ', sorted_di)
print('Original Dict: ', di)
print()

 
li = [-6, -5, -4, 1, 2, 3]

sorted_li = sorted(li)
print('Sorted     List: ', sorted_li)
# Set the key of 'sorted()' by "abs()" : key must be a function!!!
sorted_li_abs = sorted(li, key=abs)
print('Sorted by abs(): ', sorted_li_abs)
print()


