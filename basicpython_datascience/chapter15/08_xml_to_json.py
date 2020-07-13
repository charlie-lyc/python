# 연습 : XML Read -> JSON Write
# - CSV로 저장된 ipa110106.XML 파일을 JSON 으로 변환하기
# - 분할된 특허 문서로 부터 특허의 등록번호, 등록일자, 출원번호, 출원일자, 상태, 특허 제목을 추출하여
#   JSON으로 만들 것 
# - 각 문서의 key 값으로 Application Document Number를 활용함
#
# https://s3.ap-northeast-2.amazonaws.com/teamlab-gachon/ipa110106.XML


import json
import os
from bs4 import BeautifulSoup

def write_json_file(patent_info):
    with open('output/patent_data.json', 'w') as f:
        json.dump(patent_info, f)

patent_dir = 'data'
file_list = os.listdir(patent_dir)

patent_info = {}
for patent_file_name in file_list:
    full_path = patent_dir + '/' +  patent_file_name
    if os.path.isfile(full_path):
        with open(full_path, 'r') as patent_document_file:
            patent_contents = ''.join(patent_document_file.readlines())
            soup = BeautifulSoup(patent_contents, 'lxml')

            patent_document = {} 
            pub_ref = soup.find('publication-reference')
            patent_document['pubDocNumber'] = pub_ref.find('doc-number').get_text()
            patent_document['pubDate'] = pub_ref.find('date').get_text()
            patent_document['pubKind'] = pub_ref.find('kind').get_text()
            app_ref = soup.find('application-reference')
            patent_document['appDocNumber'] = app_ref.find('doc-number').get_text()
            patent_document['appDate'] = app_ref.find('date').get_text()
            patent_document['title'] = soup.find('invention-title').get_text()

            patent_key_value = patent_document['appDocNumber']
            patent_info[patent_key_value] = patent_document

patent_document_file.close()
print(patent_info)
print()

for key, value in patent_info.items():
    print(f'{key} => ', end='')
    for k, v in value.items():
        print(f'{k}: {v},', end=' ')
    print()

