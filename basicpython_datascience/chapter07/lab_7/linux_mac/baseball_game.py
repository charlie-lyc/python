# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    result = None
    if user_input_number.isdigit() == True:
        result = True
    else:
        result = False
    return result


def is_between_100_and_999(user_input_number):
    result = None
    number = int(user_input_number)
    if 100 <= number <= 999:
        result = True
    else:
        result = False
    return result


def is_duplicated_number(three_digit):
    result = None
    li = list(three_digit)
    se = set(three_digit)
    if len(li) == len(se):
        result = False
    else:
        result = True
    return result


def is_validated_number(user_input_number):
    result = None
    if is_digit(user_input_number) == True:
        if is_between_100_and_999(user_input_number) == True:
            if is_duplicated_number(user_input_number) == False:
                result = True
            else:
                result = False
        else:
            result = False
    else:
        result = False
    return result


def get_not_duplicated_three_digit_number():
    result = None
    while True:
        random_number = get_random_number()
        if is_validated_number(str(random_number)) == True:
            result = random_number
            break
    return result


def get_strikes_or_ball(user_input_number, random_number):
    result = [0, 0]
    rn_list = list(random_number)
    un_list = list(user_input_number)
    for i, vi in enumerate(rn_list):
        for j, vj in enumerate(un_list):
            if vi == vj:
                if i == j:
                    result[0] += 1
                else:
                    result[1] += 1
    return result


def is_yes(one_more_input):
    result = None
    if one_more_input.lower() == 'yes' or one_more_input.lower() == 'y':
        result = True
    else:
        result = False
    return result


def is_no(one_more_input):
    result = None
    if one_more_input.lower() == 'no' or one_more_input.lower() == 'n':
        result = True
    else:
        result = False
    return result


def main():
    print("Play Baseball")
    random_number = 999
    # ===Modify codes below=============
    while True:
        if random_number == 999:
            random_number = str(get_not_duplicated_three_digit_number())
            # random_number = str(694)
            # random_number = str(468)
            # random_number = str(572)
            print("Random Number is : ", random_number)
        user_input = input("Input guess number : ")
        if user_input == "0":
            break
        elif is_validated_number(user_input) == False:
            print("Wrong Input, Input again")
            continue
        result = get_strikes_or_ball(user_input, random_number)
        if sum(result) == 0:
            print("Wrong Input, Input again")
            continue
        elif sum(result) > 0:
            print(f"Strikes : {result[0]} , Balls : {result[1]}")
            if result[0] == 3:
                one_more_input = None
                while True:
                    one_more_input = input("You win, one more(Y/N) ?")
                    if is_no(one_more_input) == True or is_yes(one_more_input) == True:
                        break
                    print("Wrong Input, Input again")
                if is_no(one_more_input) == True:
                    break
                random_number = 999
    # ==================================
    print("Thank you for using this program")
    print("End of the Game")


if __name__ == "__main__":
    main()
