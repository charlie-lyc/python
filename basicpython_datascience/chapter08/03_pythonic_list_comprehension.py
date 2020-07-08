# List Comprehensions :
# 기존 리스트를 사용하여 간단히 다른 리스트를 만드는 기법
# 포괄적인 리스트, 포함되는 리스트라는 의미로 사용
# 파이썬에서 가장 많이 사용되는 기법
# 일반적으로 for loop + append 보다 속도가 빠름
import time

# General
result1 = []
for i in range(10):
    result1.append(i)
print(result1)
print()

# List Comprehension
# Exmple01
result2 = [i for i in range(10)]
print(result2)
print()
# Exmple02 : if 가 필터 역할을 함
result3 = [i for i in range(10) if i % 2 == 0]
print(result3)
print()
# Exmple03
word_1 = 'Hello'
word_2 = 'World'
result4 = [i+j for i in word_1 for j in word_2]
print(result4)
print()
# Exmple04
case_1 = ['A', 'B', 'C']
case_2 = ['D', 'E', 'A']
result5 = [i+j for i in case_1 for j in case_2]
result6 = [i+j for i in case_1 for j in case_2 if not(i == j)]
result7 = [[i+j for i in case_1] for j in case_2]
print(result5)
print(result6)
print(result7)
print()
# Exmple05
words = 'The quick brown fox jumps over the lazy dog'.split()
stuffs = [[word.upper(), word.lower(), len(word)] for word in words]
for stuff in stuffs:
    print(stuff)
