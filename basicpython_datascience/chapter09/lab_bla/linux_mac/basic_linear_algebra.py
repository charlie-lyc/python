from functools import reduce


def vector_size_check(*vector_variables):
    var_len_list = [len(var) for var in vector_variables]
    result = None
    for i, _ in enumerate(var_len_list):
        if i == len(var_len_list) - 1:
            result = True
        elif var_len_list[i] != var_len_list[i+1]:
            result = False
            break
    return result


def vector_addition(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    result = [sum(t) for t in zip(*vector_variables)]
    return result


def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    result = [reduce(lambda x, y: x - y, t) for t in zip(*vector_variables)]
    return result


def scalar_vector_product(alpha, vector_variable):
    result = [alpha * var for var in vector_variable]
    return result


def matrix_size_check(*matrix_variables):
    size_list = [[len(var), len(var[0])] for var in matrix_variables]
    result = None
    for i, _ in enumerate(size_list):
        if i == len(size_list) - 1:
            result = True
        elif size_list[i] != size_list[i+1]:
            result = False
            break
    return result


def is_matrix_equal(*matrix_variables):
    result = None
    if matrix_size_check(*matrix_variables) == True:
        value_list = [t for t in zip(*matrix_variables)]
        for val in value_list:
            for i, _ in enumerate(val):
                if i == len(val) - 1:
                    result = True
                elif val[i] != val[i+1]:
                    result = False
                    break
    else:
        result = False
    return result


matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]

print(is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y))  # Expected value: False
print(is_matrix_equal(matrix_x, matrix_x))  # Expected value: True


def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    result = [[sum(v) for v in zip(*var)] for var in zip(*matrix_variables)]
    return result


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    result = [[reduce(lambda x, y: x - y, v) for v in zip(*var)] for var in zip(*matrix_variables)]
    return result


def matrix_transpose(matrix_variable):
    result = [[v for v in var] for var in zip(*matrix_variable)]
    return result


def scalar_matrix_product(alpha, matrix_variable):
    result = [[alpha * v for v in var] for var in matrix_variable]
    return result


def is_product_availability_matrix(matrix_a, matrix_b):
    result = None
    if matrix_a and matrix_b:
        avail_list = [[len(row_a), len(col_b)] for col_b in zip(*matrix_b)
                      for row_a in matrix_a]
        for i, v in enumerate(avail_list):
            if v[0] != v[1]:
                result = False
                break
            elif i == len(avail_list) - 1:
                result = True
    else:
        result = False
    return result


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError
    result = [[sum(a * b for a, b in zip(row_a, col_b))
               for col_b in zip(*matrix_b)] for row_a in matrix_a]
    return result
