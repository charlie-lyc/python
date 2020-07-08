# Reduce : map function과 달리 각 element가 아닌 list에 함수를 적용해서 통합.

from functools import reduce

# 이웃한 element들 끼리 덧셈을 하여 값을 반환하되, 덧셈을 더이상 할 수 없을때까지 계속함.
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print()


# 대표적으로 팩토리얼 함수를 생성할 수 있다. : 이웃한 element들 끼리 곱셈
def factrorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))


# Summary :
# lambda, map, reduce는 간단한 코드로 다양한 기능 제공
# 그러나 직관성이 떨어져 lambda, reduce는 PEP권장사항이 아님
# 그럼에도 불구하도 Legacy Library나 다양한 머신러닝 코드에서 여전히 사용중이므로 알고는 있어야함.
