# defaultdict  : 일반적인 dict와 달리 기본값(default)을 지정, 신규값 생성시 사용
from collections import defaultdict
from collections import OrderedDict


# d = dict()
# # KeyError: 'first'
# print(d['first'])

# Default Dict 초기화
d = defaultdict(object)
# Default 값 설정 : 0
d = defaultdict(lambda: 0)
print(d['first'])
print()


####################################################

# Text Mining => Vector Space Model
# 하나의 지문에 각 단어들이 몇 개나 있는지?
text = """A press release is the quickest and easiest wqy to get free publicity. If well written, a press release can result in multiple published articles about your firm and its products. And that can mean new prospects contacting you asking you to sell to them."""
word_list = text.lower().split(' ')


# Default Dict
word_count = defaultdict(object)
word_count = defaultdict(lambda: 0)
for word in word_list:
    word_count[word] += 1
sorted_wc = OrderedDict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))
for k, v in sorted_wc.items():
    print(k, v)


# # General Dict
# word_count = {}
# for word in word_list:
#     if word not in word_count.keys():
#         word_count[word] = 1
#     else:
#         word_count[word] += 1
# sorted_wc = OrderedDict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))
# for k, v in sorted_wc.items():
#     print(k, v)
