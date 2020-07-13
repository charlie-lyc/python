# 이제 다시 돌아가서 아래 데이터는 어떻게 추출할 것인가?
#
# http://finance.naver.com/item/main.nhn?code=005930
#
# <dl class="bind">
#   <dt> 종목 시세 정보 </dt>
#   <dd> ~ </dd>
#        :
# </dl>


# 정규식 : 1)을 먼저 찾고 그 안에서 2)를 찾으면 된다.
#
# 1) "(\<dl class=\"bind\"\>)([\s\S]+?)(\<\/dl\>)"
# <dl class="bind">로 시작해서 (사이에 아무 문자열이 있고) </dl>로 끝내기
#
# 2) "(\<dd\>)([\s\S]+?)(\<\/dd\>)"
# <dd>로 시작해서 (사이에 아무 문자열이 있고) </dd>로 끝내기


import urllib.request
import re

url = 'http://finance.naver.com/item/main.nhn?code=005930'
# 보안 문제로 'SSLCertVerificationError'가 발생하여 아래의 코드를 실행할 수 없다.
html = urllib.request.urlopen(url)
contents = html.read()
# 'ms949': 한글 Codec, 'cp949'와 동일
html_contents = str(contents.decode('ms949'))

stock_results = re.findall("(\<dl class=\"bind\"\>)([\s\S]+?)(\<\/dl\>)", html_contents)
samsung_stock = stock_results[0]
samsung_index = samsung_stock[1]

index_list = re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", samsung_index)

for index in index_list:
    print(index[1])
