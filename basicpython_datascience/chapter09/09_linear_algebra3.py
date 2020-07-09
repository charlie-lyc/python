
# 두개 이상의 Argument가 존재할 때
def vector_addition(*args):
    result = [sum(t) for t in zip(*args)]
    return result


print(vector_addition([1, 2], [2, 3], [3, 4]))


# Summary : 다음의 활용이 필수이다.!!!
# list comprehension,
# zip,
# asterisk
# lambda, map, reduce
