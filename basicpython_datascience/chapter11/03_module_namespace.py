# Namespace
# 모듈을 호출할 때 범위 정하는 방법
# 모듈 안에는 함수와 클래스 등이 존재 가능
# 필요한 내용만 골라서 호출할 수 있음
# from 과 import 키워드를 사용

# # Alias 설정 : 모듈명으로 별칭을 사용
import fah_converter as fah
print(fah.convert_c_to_f(41.6))

# # 모듈로부터 특정 함수 또는 클래스만 호출
# from fah_converter import convert_c_to_f
# print(convert_c_to_f(41.6))

# # 모듈로부터 모든 함수 또는 클래스를 호출 : 권장하지 않는다.
# # 다수개의 모듈을 이런식으로 호출하게 된다면 사용하는 함수의 출처가 불분명하여 혼란스럽다.
# from fah_converter import *
# print(convert_c_to_f(41.6))

# Built-in Modules : 파이썬이 기본 제공하는 라이브러리
# 문자처리, 웹, 수학 등 다양한 모듈이 제공됨
# 별다른 조치없이 import문으로 활용 가능

# 난수
# import random
# print(random.randint(0, 100))  # 0이상 ~ 100미만 사이의 정수 난수 생성
# print(random.random())  # 0이상 ~ 1미만 사이의 난수 생성

# 시간
# import time
# print(time.localtime())  # 현재 시간 출력
# print(time.time())

# 웹
# import urllib.request
# response = urllib.request.urlopen('http://cs50.gachon.ac.kr')
# print(response.read())
