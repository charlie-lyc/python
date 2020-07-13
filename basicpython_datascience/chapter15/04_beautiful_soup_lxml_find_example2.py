
# # 실습 2)
# - 파일을 열어 보면 특허 출원번호, 출원일, 등록번호, 등록일, 상태, 특허명 등 다양한 정보를 추출할 수 있다. 
# - 하지만 동일한 태그 이름 ('document-id', 'doc-number', 'date' 등)에 다른 값이 있어
# - find_all()로는 모두다 구별할 수 없다. 따라서 구조(Tree)적으로 부모 태그가 무엇인지를 살펴 분기 시킨다. 
#
# <us-bibliographic-data-grant>
#     <publication-reference>
#         <document-id>
#             <country>US</country>
#             <doc-number>08621662</doc-number>
#             <kind>B2</kind>
#             <date>20140107</date>
#         </document-id>
#     </publication-reference>
#     <application-reference appl-type="utility">
#         <document-id>
#             <country>US</country>
#             <doc-number>13175987</doc-number>
#             <date>20110705</date>
#         </document-id>
#     </application-reference>
#               :    


import urllib.request
from bs4 import BeautifulSoup


with open('US08621662-20140107.XML', 'r', encoding='utf8') as patent_xml:
    xml = patent_xml.read()
    soup = BeautifulSoup(xml, 'lxml')

    publication_reference_tag = soup.find('publication-reference')
    p_document_id_tag = publication_reference_tag.find('document-id')
    p_country = p_document_id_tag.find('country').get_text()
    p_doc_number = p_document_id_tag.find('doc-number').get_text()
    p_doc_kind = p_document_id_tag.find('kind').get_text()
    p_doc_date = p_document_id_tag.find('date').get_text()

    application_reference_tag = soup.find('application-reference')
    a_document_id_tag = application_reference_tag.find('document-id')
    a_country = a_document_id_tag.find('country').get_text()
    a_doc_number = a_document_id_tag.find('doc-number').get_text()
    a_doc_date = a_document_id_tag.find('date').get_text()

    print(p_country, p_doc_number, p_doc_kind, p_doc_date)
    print(a_country, a_doc_number, a_doc_date)








