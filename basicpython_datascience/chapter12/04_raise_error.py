# Raise <Exception Type>
# 필요에 따라 강제로 예외를 발생 시킴

while True:
    value = input('변활할 정수 값을 입력해 주세요')
    for digit in value:
        if digit not in '0123456789':
            raise ValueError('숫자값을 입력하지 않으셨습니다.')
        print('정수값으로 변환된 숫자 : ', int(value))
