# Beautiful Soup Module
# - find_all() : 정규표현식의 findall()과 마찬가지로 해당 패턴을 모두 반환
#   find("invention-title") : "invention-title"라는 'tag name' 하나를 반환
# - get_text() : 반환된 태크 내의 값 반환, 태그와 태그 사이의 값 반환
#
# <invention-title id='d2e43'> 
# Adjustable shoulder device for hard upper torso suit
# </invention-title>


# Example
# - 미국 특허청(USPTO) 특허 데이터는 XML로 제공됨
# - 해당 데이터 중 등록번호 '08621662'인 
#   "Adjustable shoulder device for hard upper torso suit" 분석
# - 참고 : http://www.google.com/patents/US20120260387
#         https://s3.ap-northeast-2.amazonaws.com/teamlab-gachon/US08621662-20140107.XML
# - XML 데이터를 Beautiful Soup를 통해 데이터 추출


# 실습 1)
# - 데이터 다운로드 : 아래 해당 페이지로 이동해서 오른쪽 마우스 클릭 'Save As'해서 동일한 파일이름으로 저장
#   https://s3.ap-northeast-2.amazonaws.com/teamlab-gachon/US08621662-20140107.XML
 

import urllib.request
from bs4 import BeautifulSoup


with open('US08621662-20140107.XML', 'r', encoding='utf8') as patent_xml:
    xml = patent_xml.read()
    soup = BeautifulSoup(xml, 'lxml')
    # find_all() : 찾고자 하는 태그가 복수개일 때 
    # inv_tit_tag = soup.find_all('invention-title') # 리스트로 반환
    inv_tit_tag = soup.find('invention-title') # 문자열로 반환
    print(inv_tit_tag)
    print(inv_tit_tag.get_text())


