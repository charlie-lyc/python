# -*- coding: utf-8 -*-

def main():
    print(sum_of_list([1, 2, 3, 4, 5]))
    print(sum_of_list([1, 2, 3, 4, 5, 6]))
    print(merge_and_sort([1, 2, 3, 10], [5, 6, 7, 8]))
    print(merge_and_sort(['a', 'b', 'z'], ['c', 'd', 'f']))
    print(delete_a_list_element([1, 2, 3, 10], 1))
    print(delete_a_list_element(['a', 'b', 'c', 'z'], 'd'))
    print(comparison_list_size([1, 2, 3, 4, 5, 6], [1, 2, 3]))
    print(comparison_list_size([1, 2, 3, 4, 5, 6], [1, 2, 3, 5, 7, 8, 9, 10]))
    print(odd_even_check(5, 6))
    print(odd_even_check(5, 5))
    print(discount_price(40000))
    print(discount_price(110000))
    print(find_smallest_value([1, 2, 3, 4, 5]))
    print(find_smallest_value([5, 4, 3, 0, 100, 200]))
    print(binary_converter(100))
    print(binary_converter(56))
    print(number_of_cases(['a', 'b', 'c']))
    print(number_of_cases(['a', 'a']))
    print(number_of_cases([1, 2, 3, 'a']))


def sum_of_list(list_data):
    result = sum(list_data)
    return result


def merge_and_sort(list_data_a, list_data_b):
    result = list_data_a
    result.extend(list_data_b)
    result.sort()
    return result


def delete_a_list_element(list_data, element_value):
    result = list_data
    if element_value in result:
        result.remove(element_value)
    else:
        result = 0
    return result


def comparison_list_size(list_data_a, list_data_b):
    len_a = len(list_data_a)
    len_b = len(list_data_b)
    result = None
    if len_a >= len_b:
        result = list_data_a
    else:
        result = list_data_b
    return result


def odd_even_check(a, b):
    sum = a + b
    result = None
    if sum % 2 == 0:
        result = 'Even'
    else:
        result = 'Odd'
    return result


def discount_price(price):
    result = None
    if price < 100000:
        result = price * 0.9
    else:
        result = price * 0.8
    return result


def find_smallest_value(list_data):
    result = min(list_data)
    return result


def binary_converter(decimal_number):
    result = ''
    while decimal_number > 0:
        remainder = decimal_number % 2
        decimal_number = decimal_number // 2
        result = str(remainder) + result
    return result


def number_of_cases(list_data):
    new_list_data = []
    for data in list_data:
        if type(data) != type(str(data)):
            data = str(data)
        new_list_data.append(data)
    result = []
    for data1 in new_list_data:
        for data2 in new_list_data:
            case = data1 + data2
            if case not in result:
                result.append(case)
            else:
                continue
    result.sort()
    return result


if __name__ == "__main__":
    main()
