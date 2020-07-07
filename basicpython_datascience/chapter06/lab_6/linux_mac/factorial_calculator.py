# -*- coding: utf-8 -*-
from math import factorial


def is_positive_number(integer_str_value):
    try:
        if int(integer_str_value) >= 1:
            return True
        else:
            return False
    except ValueError:
        return False


def get_factorial_value(integer_value):
    result = integer_value * factorial(integer_value - 1)
    return result


def main():
    while True:
        user_input = input('Input a positive number : ')
        result = is_positive_number(user_input)
        if user_input == '0':
            break
        elif result == True:
            print(get_factorial_value(int(user_input)))
        else:
            print('Input again, Please')
    print('Thank you for using this program')


if __name__ == "__main__":
    main()
