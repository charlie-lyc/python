# OrderedDict  : 일반적인 dict와 달리 입력한 순서대로 data를 반환
from collections import OrderedDict

# General Dict
d = {}
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500
for k, v in d.items():
    print(k, v)
print()

# Ordered Dict
ordered_d = OrderedDict()
ordered_d['x'] = 100
ordered_d['y'] = 200
ordered_d['z'] = 300
ordered_d['l'] = 500
for k, v in ordered_d.items():
    print(k, v)
print()

############################################################

# dict는 기본적으로 key값만 list로 정렬이 된다.
# 그래서 command_analyzer.py 의 경우에서와 같이 dict를 list로 바꾸는 번거로움이 있었다.
sorted_d = sorted(d)
print(sorted_d)
print()


# dict의 (key,value)를 key값 기준으로 정렬할 때 이용
sorted_od = OrderedDict(sorted(d.items(), key=lambda x: x[0]))
print(sorted_od)
for k, v in sorted_od.items():
    print(k, v)
print()

# dict의 (key,value)를 value 기준으로 정렬할 때 이용
sorted_od = OrderedDict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print(sorted_od)
for k, v in sorted_od.items():
    print(k, v)
