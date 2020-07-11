# "try ~ except ~ else" 구문
# except이하는 예상 가능한 에러 처리
# else이하는 예상 불가능한 에러 처리
for i in range(10):
    try:
        print(10 / i)
    except ZeroDivisionError:
        print('Not divided by zero')
    else:
        print('Something went wrong')
print()


# "try ~ except ~ else ~ finally" 구문1
# finally 이하는 에러가 발생하든 아니든 무조건 실행되는 코드
for i in range(10):
    try:
        print(10 / i)
    except ZeroDivisionError as e:
        print(e)
    else:
        print('Something went wrong')
    finally:
        print('End of program')
print()


# "try ~ except ~ else ~ finally" 구문2
try:
    for i in range(10):
        result = 10 / i
        print(result)
except ZeroDivisionError:
    print('Not divided by zero')
else:
    print('Something went wrong')
finally:
    print('End of program')


# # Summary
# try:
#     pass
#     raise ErrorName
# # 의도적으로 발생시키거나, 예상되는 에러
# except ErrorName:
#     pass
# except ErrorName as e:
#     print(e)
# # 예상하지 못한 에러
# except Exceptions:
#     pass
# else:
#     pass
# # 'try except'구문 실행 후 무조건 실행
# finally:
#     pass
