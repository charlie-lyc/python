# Web Scrapping

# HTML Data
# - 비록 Programming Language는 아니지만 HTML page도 하나의 프로그램으로 볼수 있다.
# - 즉, 정해진 규칙에 따라 데이터를 수집할 수 있는 대상이 된다.
# - 간단한 실례로써 엑셀을 이용해 네이버 증시 정보를 다운 받을 수 있다.

# 웹에서 데이터 다운로드
# - 웹상에 있는 파일을 로컬폴더에 저장함
# - built-in 모듈인 urllib 의 urlretrieve() 함수 이용

import urllib.request

url = 'http://storage.googleapis.com/patents/grant_full_text/2014/ipg140107.zip'

print('Start Download')
fname, header = urllib.request.urlretrieve(url, 'ipg140107.zip')

print('End Download')