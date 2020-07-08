# Zip : 두개의 list 값들을 병렬적으로 추출
a_list = ['a1', 'a2', 'a3']
b_list = ['b1', 'b2', 'b3']


print(zip(a_list, b_list))
print(list(zip(a_list, b_list)))
print()


# print out tuples
for i in zip(a_list, b_list):
    print(i)
print()

# Unpack
for a, b in zip(a_list, b_list):
    print(a, b)
print()

for i, v in enumerate(zip(a_list, b_list)):
    print(i, v)
print()

for i, (a, b) in enumerate(zip(a_list, b_list)):
    print(i, a, b)
print()

a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)
print()


# Pythonic Code
sum_zip_tuple = [sum(i) for i in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))]
print(sum_zip_tuple)
