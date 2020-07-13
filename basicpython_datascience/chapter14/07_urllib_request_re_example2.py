# 코딩하기 전에 regexr.com에서 연습하여 정규식을 확보하는 것이 우선이다.
import urllib.request
import re

url = 'http://www.google.com/googlebooks/uspto-patents-grants-text.html'
html = urllib.request.urlopen(url)
contents = html.read()
html_contents = str(contents.decode('utf8'))

# url_results = re.findall(r'(http)(.+)(zip)', html_contents)
# for url in url_results:
#     print(''.join(url))

url_results = re.findall(r'http.+zip', html_contents)
for url in url_results:
    print(url)

print(len(url_results))

# goole 페이지에서는 데이터 수집을 허용해 준다.
