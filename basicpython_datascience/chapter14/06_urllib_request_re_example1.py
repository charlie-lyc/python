# Regular Expressin in Python
# - re 모듈을 import하여 사용
# - 함수 : search() 한개만 찾기, findall() 전체 찾기
# - 추출된 패턴은 'tuple'로 반환됨

# 연습 : 특정 페이지에서 ID만 추출하기
#       http://goo.gl/U7mSQl
# - ID패턴 파악 : [영문대소문자|숫자]{여러개} 그리고 asterisk로 끝남
# - 정규식 : "[A-Za-z0-9]+\*\*\*"


import urllib.request
import re

url = 'http://goo.gl/U7mSQl'
# 보안 문제로 'SSLCertVerificationError'가 발생하여 아래의 코드를 실행할 수 없다.
html = urllib.request.urlopen(url)
contents = html.read()
html_contents = str(contents)

id_results = re.findall(r"[A-Za-z0-9]+\*\*\*", html_contents)

for result in id_results:
    print(result)
