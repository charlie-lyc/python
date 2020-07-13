# CSV객체로 처리
# - 텍스트 파일 형태로 데이터 처리시 문장내에 들어가 있는 ',' 등에 대해 전처리가 필요
# - 파이썬에서는 간단히 CSV파일을 처리하기 위해 CSV객체를 제공
# - 예제 데이터는 국내 주요 상권의 유동인구 현황 공공정보
# - 한글로 되어 있어 한글 처리가 필요 *** 중요!!! ***


# CSV객체 활용 Attribute 
# - delimiter      [Default : ,  ]            : 글자를 나누는 기준, 구분자, 구획자
# - lineterminator [Default : \n ]            : 줄 바꿈 기준
# - quotechar      [Default : "  ]            : 문자열을 둘러싸는 신호 문자
# - quoting        [Default : QUOTE_MINIMAL ] : 데이터 나누는 기준이 quotechar에 의해 둘러싸인 레벨
#
# import csv
# reader = csv.reader(
#           f, 
#           delimiter='\t', 
#           lineterminator='\n', 
#           quotechar="'", 
#           quoting=csv.QUOTE_ALL
# )

import csv

row_num = 0
header = None
SeongNam_data = []

# 'cp949' : Codec of Korean in Python Library
with open('korea_floating_population_data.csv', 'r', encoding='cp949') as csvrf:
    csv_data = csv.reader(csvrf)
    for row in csv_data:
        if row_num == 0:
            header = row
        if row[7].find(u'성남시') != -1:
            SeongNam_data.append(row)
        row_num += 1

with open('seongnam_floating_population_data.csv', 'w', encoding='utf8') as csvwf:
    csv_writer = csv.writer(csvwf, delimiter='\t', quotechar="'", quoting=csv.QUOTE_ALL)
    csv_writer.writerow(header)
    for row in SeongNam_data:
        csv_writer.writerow(row)

csvrf.close()
csvwf.close()






