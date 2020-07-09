# Linear Algebra : 선형 대수학 => 1차 함수 f(x) = ax + b

# Vector : 크기와 방향 모두 가지는 경우
# 3-dimensional column vector [9]
#                             [2]
#                             [3]
# 3-dimensional row vector  [9,2,3]
# 3-dimensional zero vector [0,0,0]

# Scalar : 크기만 가지는 경우

# Scalar x Vector product

# Matrix : 사각형으로 된 수의 배열 => 한 개 이상의 벡터
# row : m개, column : n개 로 구성 =>  m X n(m by n) 행렬
# row가 1개 뿐이면 row vector, column이 1개 뿐이면 column vector, m = n = 0이면 zero vector

# Matrix Representation
# 행렬 A의 i행, j열의 값을 "A의 ij번째 element"라 하고 'aij'로 표시함
#     [1 2 3]     a11 = 1
# A = [4 5 6]     a23 = 6
#     [7 8 9]     a31 = 7

# Matrix Equal : 동치
# 두개의 행열 A와 B가 같은 크기이면서 모든 i, j에 대하여 같은 값을 가지면 '동치''라고 한다.
# "aij = bij"라고 표시한다.

# Matrix Addition : 벡터와 마찬가지로 같은 인덱스별로 합한다.

# Scalar x Matrix product

# Matrix Transpose : 전치행렬
# 주어진 m X n 행렬의 행과 열을 바꾸어 만든 행렬
#                     [1 4]
# A = [1 2 3]    AT = [2 5]
#     [4 5 6]         [3 6]

# Matrix product : 행렬 곱셈
# 앞 행렬의 열과 뒤 행렬의 행을 dot product
# 앞 행렬 열의 수와 뒤 행렬 행의 수가 동일해야만
