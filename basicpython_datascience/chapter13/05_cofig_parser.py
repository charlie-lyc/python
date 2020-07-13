# 실제 프로그램을 실행할 때 필요한 여러 설정들을 저장하여 데이터로 가지고 있다.
# - 데이터 파일 위치
# - 파일 저장 장소
# - operation type 등
# 1. Config Parser - 파일에서의 설정
# 2. Arg Parser - 실행 시점에서의 설정

# Configparser
# - 프로그램의 실생 설정을 파일에 저장
# - section, key, value 값의 형태로 설정된 설정 파일을 사용
# - 설정 파일을 Dict Type으로 호출 후 사용

# Config File
#
# [SectionOne]
# Status : Single
# Name : Derek
# Value : Yes
# Age : 30
# Single : True
# 
# [SectionTwo]
# FavoriteColor = Green
#
# [SectionThree]
# FamilyName : Johnson

import configparser

config = configparser.ConfigParser()
config.sections()

config.read('example.cfg')
config.sections()

# dict 구조에서 대문자로 된 key들을 추출하여 출력하니 소문자로 출력
# dict에 key를 입력하여 value를 얻고자 할 때는 반드시 대소문자 구별
for key in config['SectionOne']:
    print(key)
print()

print(config['SectionOne']['Status'])




