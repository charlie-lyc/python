# 연습 : ipg140107.xml 분석
#
# https://s3.ap-northeast-2.amazonaws.com/teamlab-gachon/ipa110106.XML
#
# - ipa110106.XML 파일은 2011년 1월 첫째주에 출원된 특허를 모은 파일이다
# - 개별 특허들을 나눠서 CSV형태로 저장하는 연습을 해보자
# - 개별 특허 시작은 <?xml version='1.0'?>로 시작된다.
# - 분할된 특허 문서로 부터 특허의 등록번호, 등록일자, 출원번호, 출원일자, 상태, 특허 제목을 추출하여
# - CSV 파일로 만들어 보자.
# 
# invention-title
# application-reference : doc-number, date
# publication-reference : doc-number, date, kind


import csv
from bs4 import BeautifulSoup


fieldnames = ['pubDocNum', 'pubDate', 'pubKind', 'appDocNum', 'appDate', 'inventionTitle']
with open('ipa110106.XML', 'r', encoding='utf8') as xml_file:
    xml_read = xml_file.read()
    xml_list = xml_read.split('</us-patent-application>')
    with open('ipa110106.csv', 'w', encoding='utf8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='|', quotechar="'")
        csv_writer.writerow(fieldnames)      
        for xml in xml_list:
            if not xml:
                break
            row = []
            soup = BeautifulSoup(xml, 'lxml')
            pub_ref = soup.find('publication-reference')
            row.append(pub_ref.find('doc-number').get_text())
            row.append(pub_ref.find('date').get_text())
            row.append(pub_ref.find('kind').get_text())
            app_ref = soup.find('application-reference')
            row.append(app_ref.find('doc-number').get_text())
            row.append(app_ref.find('date').get_text())
            row.append(soup.find('invention-title').get_text())    
            csv_writer.writerow(row)

xml_file.close()
csv_file.close()
