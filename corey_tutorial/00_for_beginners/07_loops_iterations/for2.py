nums = [1, 2, 3, 4, 5]


for num in nums:
    for letter in 'abc':
        print(num, letter)
print()


for num in nums:
    for letter in 'abc':
        print(num, letter, end=' ')
    print()
print()


for num in nums:
    for letter in 'abc':
        print(f'{num}{letter}', end=' ')
    print()
print()


