# Enumerate : list의 element를 번호를 붙여 추출
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

mylist = ['a', 'b', 'c', 'd']
print(enumerate(mylist))
print(list(enumerate(mylist)))
print()

# Pithonic Code
mydict = {i: v for i, v in enumerate(mylist)}
print(mydict)
print()

text = 'Gachon University is an academic institute located in South Korea'
words_list = text.split()
print(words_list)
words_dict = {i: v for i, v in enumerate(words_list)}
print(words_dict)
print()
