# 앞서 실습한 파일들이 대부분 보안문제로 접근할 수 없어
# 다시 종합하여 실습!!!

import urllib.request
import re

base_url = 'http://storage.googleapis.com/patents/grant_full_text/2015/'
url = 'http://www.google.com/googlebooks/uspto-patents-grants-text.html'
html = urllib.request.urlopen(url)
contents = html.read()
html_contents = str(contents.decode('utf8'))

# 해당 웹페이지에서 2015년도 zip파일 이름 추출
file_list = re.findall(r'[^/]ipg15[0-9]{4}.zip', html_contents)

# 파일 이름에서 필요없는 '\n' 제거
file_name_list = []
for file in file_list:
    file_name_list.append(file.replace('\n', ''))
# 웹페이지 파일 갯수와 추출된 갯수 비교 확인
print(len(file_name_list))
print(file_name_list)
print()

for file_name in file_name_list:
    full_url = base_url + file_name
    print(full_url)
    print()
    # urllib.request.urlretrieve(url, filename)
    # : 해당 경로에 있는 객체를 동일 파일명으로 내컴퓨터에서 복구한다(복사한다). 즉 '다운로드'된다.
    #   그리고 그 파일명(filename)과 파일의 메타데이터(header)가 tuple로 반환된다.(filename, headers)
    filename, headers = urllib.request.urlretrieve(full_url, file_name)
    print(filename)
    print()
    print(headers)
    # 파일들 용량이 커서 다운로드 받는데 한참 걸린다. 중간에 control + c
    print('======= End Download =======')
