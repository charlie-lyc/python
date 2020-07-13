
# Beautiful Soup
# - HTML, XML 등 MarkUp 언어 Scrapping을 위한 대표적인 도구
# - https://www.crummy.com/software/BeautifulSoup/


# lxml 과 html5lib 와 같은 Parser를 사용하기도 한다.
# - 속도는 상대적으로 느리나 간편히 사용할 수 있음


# 설치
# pip install beautifulsoup4
# pip install lxml


from bs4 import BeautifulSoup

with open('books.xml', 'r', encoding='utf8') as books_file:
    books_xml = books_file.read()
    print(books_xml)
    print()
    # 객체 생성             xml객체명 이용parser명
    soup = BeautifulSoup(books_xml, 'lxml')
    # find_all() : tag 찾는 함수 
    print(soup.find_all('author'))
    print()
    for author_info in soup.find_all('author'):
        print(author_info)
        # get_text() : tag 안의 텍스트 얻는 함수
        print(author_info.get_text())


