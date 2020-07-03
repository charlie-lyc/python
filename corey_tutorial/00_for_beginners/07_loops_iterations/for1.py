nums = [1, 2, 3, 4, 5]


for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)
print()


for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)
