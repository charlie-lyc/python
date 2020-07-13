# 정규식 추출 연습
# - 연습장(https://regexr.com/) 이동
# - 구글 USPTO Bulk Download 데이터 페이지 소스 보기 클릭
#    http://www.google.com/googlebooks/uspto-patents-grants-text.html
# - 소스 전체 복사후 정규식 연습장에 붙여넣기
# - 상단 Expression 부분을 수정해 가며 추출


# zip 파일 다운로드 할 수 있는 url 추출
# 'http'문자열로 시작해서 'zip'문자열로 끝나며,
# 그 사이에 어떤 문자('.')가 오던 최소한 1개 이상인 문자열
#
# http.+zip
#
# 2098개의 매치되는 문자열을 찾음


# zip 파일 이름만 추출
#
# [^/]ipg.+zip
#
# 533개
#
# [^/i]pg.+zip
#
# 209개
#
# [^/]pftaps.+zip
#
# 1356개
