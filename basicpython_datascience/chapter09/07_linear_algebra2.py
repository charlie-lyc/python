# Vector representation of Python
# 다양한 방법이 존재하며 최선의 방법은 없음
# column vector는 프로그램상 구현하기 어려움
# 값의 변경 유무, 속성값 유무에 따라 선택
# 이후 실습에서는 기본적으로 list로 vector연산 실시

vector_a = [1, 2, 10]  # list
vector_b = (1, 2, 10)  # tuple
vector_c = {'x': 1, 'y': 1, 'z': 10}  # dict
print(vector_a, vector_b, vector_c)
print()

#############################################
# Vector의 계산

u = [2, 3]
v = [2, 3]
z = [3, 5]

# Example01 : 덧셈 - 파이썬 답지 않음
result1 = []
for i in range(len(u)):
    result1.append(u[i] + v[i] + z[i])
print(result1)
print()

# Example02 : 덧셈 - 파이썬 답지 않음
result2 = []
for i in zip(u, v, z):
    result2.append(sum(i))
print(result2)
print()

# Example03 : 덧셈
result3 = [sum(t) for t in zip(u, v, z)]
print(result3)
print()

# Example04 : Scalar-Vector product 계산
u = [1, 2, 3]
v = [5, 5, 5]
alpha = 2
result4 = [alpha * sum(t) for t in zip(u, v)]
print(result4)
