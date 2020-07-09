# Matrix representation of Python
# Vector와 마찬가지로 다양한 방법이 존재
# 특히 dict로 표현할 때는 무궁무진한 방법이 있음
# 이후 실습에서는 기본적으로 2-dimensional list형태로 표현
# [[first row], [second row], [third row], ...]

matrix_a = [[3, 6], [4, 5]]  # list
matrix_b = [(3, 6), (4, 5)]  # tuple
matrix_c = {(0, 0): 3, (0, 1): 6, (1, 0): 4, (1, 1): 5}  # dict
print(matrix_a, matrix_b, matrix_c)
print()

########################################################
# Matrix의 계산

matrix_a = [[3, 6], [4, 5]]
matrix_b = [[5, 8], [6, 7]]

print(zip(matrix_a, matrix_b))
for t in zip(matrix_a, matrix_b):
    print(t)
print()

# Example01 : 덧셈 - 전혀 파이썬 답지 않음
result1 = []
for tup in zip(matrix_a, matrix_b):
    res = []
    for i in range(len(tup)):
        lis = []
        for j in range(len(tup)):
            lis.append(tup[j][i])
        res.append(sum(lis))
    result1.append(res)
print(result1)
print()

# Example02 : 덧셈
result2 = [[sum(es) for es in zip(*t)] for t in zip(matrix_a, matrix_b)]
print(result2)
print()

# Example03 : Scalar-Matrix product 계산
matrix_c = [[1, 2], [3, 4]]
alpha = 4
result3 = [[alpha * element for element in row] for row in matrix_c]
print(result3)
print()

# Example04 : Matrix Transpose(전치행렬) 얻기
matrix_d = [[1, 2, 3], [4, 5, 6]]
result4 = [[element for element in row] for row in zip(*matrix_d)]
print(result4)
print()

# Example05 : Matrix product 계산 - 곱셈
matrix_f = [[1, 1, 2], [2, 1, 1]]
matrix_g = [[1, 1], [2, 1], [1, 3]]
result5 = [[sum(f * g for f, g in zip(row_f, column_g))
            for column_g in zip(*matrix_g)] for row_f in matrix_f]
print(result5)
print()
