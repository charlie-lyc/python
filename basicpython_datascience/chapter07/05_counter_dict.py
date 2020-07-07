# Sequence type의 data element들의 갯수를 dict 형태로 반환
from collections import Counter

# 초기
c1 = Counter()

# List
c1 = Counter('gallahad')
print(c1)
# sort까지 실행되어 결과가 반환된다.
# Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
print()

c2 = Counter(['a', 'b', 'a', 'c', 'c', 'd'])
print(c2)
# sort까지 실행되어 결과가 반환된다.
# Counter({'a': 2, 'c': 2, 'b': 1, 'd': 1})
print()


# Dict
c3 = Counter({'red': 4, 'blue': 2})
print(c3)
print(c3.elements())
print(list(c3.elements()))
print()


# Parameter
c4 = Counter(cats=4, dogs=8)
print(c4)
print(c4.elements())
print(list(c4.elements()))
print()

# c5 = Counter([('ham', 4), ('eggs', 2)])
# print(c5)
# print(c5.elements())
# print(list(c5.elements()))
# print()

##############################################

# Set 연산들을 지원
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
print(c - d)  # 0과 마이너스 parameter값은 자동으로 삭제.
print(c + d)
print(c & d)
print(c | d)
c.subtract(d)  # (c - d)와 비교하면 마이너스 parameter값도 그대로 존재.
print(c)
print()


# Word Counter 기능 제공 : defaultdict보다 훨씬 쉽게 구현
text = """A press release is the quickest and easiest wqy to get free publicity. If well written, a press release can result in multiple published articles about your firm and its products. And that can mean new prospects contacting you asking you to sell to them."""
word_list = text.lower().split(' ')

print(Counter(word_list))
print(Counter(word_list)['and'])
print(Counter(word_list)['to'])
print(Counter(word_list)['a'])
