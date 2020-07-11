
# Exception 종류
# - IndexError : 리스트의 인덱스 범위를 넘어갈 때
# - NameError : 존재하지 않는 변수를 호출할 때
# - ZeroDivisionError : 0으로 숫자를 나눌 때
# - ValueError : 변환할 수 없는 문자/숫자를 변환할 때
# - FileNotFoundError : 존재하지 않는 파일을 호출할 때


# Exception Handling : 기본 "try ~ except" 구문
# for 구문 전체를 모두 예외 처리 : 적합하지 않음.
try:
    for i in range(10):
        print(10 / i)
except ZeroDivisionError:
    print('Not divided by zero')
print()


# for 구문내의 에러 발생부분만 예외 처리.
for i in range(10):
    try:
        print(10 / i)
    except ZeroDivisionError:
        print('Not divided by zero')
print()


# 파이썬시스템에서 미리 정해놓은 해당 에러의 자체메시지 출력.
# "try ~ except ~ as" 구문
for i in range(10):
    try:
        print(10 / i)
    except ZeroDivisionError as e:
        print(e)
