# General
colors = ['red', 'blue', 'green', 'yellow']
result1 = ''
for s in colors:
    result1 += s + ' '
print(result1)
print()


# Pythonic Code :
# 파이썬 특유의 문법을 사용하여 보다 심플하고 효율적이다.
# 코딩이 길어지고 복잡해질수록(고급 코드일수록) 더욱 필요해진다.
# 그에 따른 당연한 결과이지만 다른 개발자의 코드에 대한 이해도가 높아진다.

# Example : for loop보다 list가 더 빠르다.
result2 = ' '.join(colors)
print(result2)
print()

result3 = ', '.join(colors)
print(result3)
print()

result4 = '-'.join(colors)
print(result4)
print()
