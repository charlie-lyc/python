# Argparser
# - 콘솔창에서 프로그램 실행시 setting 정보를 저장
# - 거의 모든 콘솔 기반 파이썬 프로그램에서 기본으로 제공
# - 특수 모듈도 많이 존재하지만(TF), 일반적을 argparser를 사용
# - Command-Line Option

# Examples
# % python -h
# % python --version
# % ls -l
# % ls -la
# % ls -lh

import argparse

parser = argparse.ArgumentParser(description='Sum two integers.')
#                 짧은이름   긴이름        표시명           Help설명           Argument Type
parser.add_argument('-a', '--a_value', dest='A_value', help='A integers', type=int)
parser.add_argument('-b', '--b_value', dest='B_value', help='B integers', type=int)

args = parser.parse_args()
# print(args)
# print(args.A_value)
# print(args.B_value)
print(args.A_value + args.B_value)

# 실제 실행
#
# $ python 06_arg_parse.py
# # Namespace(A_value=None, B_value=None)
# # None
# # None
# Traceback (most recent call last):
#   File "06_arg_parse.py", line 25, in <module>
#     print(args.A_value + args.B_value)
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
#
# $ python 06_arg_parse.py -a 5 -b 10
# # Namespace(A_value=5, B_value=10)
# # 5
# # 10
# 15
#
# $ python 06_arg_parse.py -h
# usage: 06_arg_parse.py [-h] [-a A_VALUE] [-b B_VALUE]
# Sum two integers.
# optional arguments:
#   -h, --help            show this help message and exit
#   -a A_VALUE, --a_value A_VALUE
#                         A integers
#   -b B_VALUE, --b_value B_VALUE
#                         B integers







