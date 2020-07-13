# 앞에서 배운 CSV, HTML
# 이번에 배울 XML, JSON

# eXtensible Markup Language

# XML
# - 데이터의 구조(Tree구조)와 의미를 설명하는 tag(markup)를 사용하여 표시하는 언어
# - tag와 tag사이에 값이 표시되고, 구조적인 정보를 표현할 수 있음
# - HTML과 문법이 비슷, 대표적인 데이터 저장 방식
# - HTML이 데이터의 표현에 중점을 두었다면, XML은 데이터를 저장하고 전송하는데 중점을 둔다.
# - 정보 구조에 대한 정보인 스키마와 DTD등으로 메타정보가 표현되며,
# - 용도에 따라 다양한 형태로 변경이 가능하다.
# - XML은 컴퓨터간(PC <-> Smartphone)에 정보를 주고받기 매우 유용한 저장방식으로 사용된다.


# # Example01
# <?xml version = '1.0'?>
# <cat>
#     <name> Kitty </name>
#     <variety> sharm </variety>
#     <age> 6 </age>
#     <neutralize> yes </neutralize>
#     <declaw> no </declaw>
#     <number> lzz138bod </number>
#     <owner> Lee </owner>
# </cat >

# # Example02
# <?xml version = '1.0'?>
# <books>
#    <book>
#         <author> Carson </author>
#         <price format='dollar'> 31.95 </price>
#         <pubdate> 05/01/2001 </pubdate>
#     </book>
#     <pubinfo>
#         <publisher> MSPress </publisher>
#         <state> WA</state>
#     </pubinfo>
# </books>


# XML Parsing
# - XML도 HTML과 마찬가지로 구조적 MarkUp 언어
# - 정규표현식으로 parsing이 가능하다.
# - 그러나 좀더 손쉬운 도구들이 개발되어 있다.
# - 가장 많이 쓰이는 parser는 "Beautiful Soup"