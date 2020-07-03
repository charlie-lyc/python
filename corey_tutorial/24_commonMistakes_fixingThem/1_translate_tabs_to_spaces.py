# Indentation Error
nums = [11, 30, 44, 54]

for num in nums:
    square = num ** 2
    print(square)

# IndentationError: unindent does not match any outer indentation level
# 겉으로 보이기엔 똑같은 것 같지만  분명히 다르고 이로 인해 위와 같은 에러가 발생한다.
# line5 |  \t |square = num ** 2
# line6 |_ _ _|print(square)

# 해결법 : Sublime Text - Preference - Settings 에서 아래와 같이 설정
# "translate_tabs_to_spaces": true

# Sublime Text 닫았다가 다시 시작
# 이 파일을 열어서 line5의 |  \t |를 지웠다가 다시 탭으로 간격을 띄움
# 다시 실행하면 이번에는 IndentationError가 발생하지 않는다.