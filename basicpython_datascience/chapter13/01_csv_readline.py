# CSV (Comma Separate Value)
# - csv, 필드를 쉽표(,)로 구분한 텍스트 파일
# - 엑셀 같은 양식의 데이터를 프로그램에 상관없이 쓰기 위한 데이터 형식
# - 엑셀에서 '다른 이름 저장'기능으로 사용 가능
# - 탭구분(TSV), 스페이스구분(SSV) 등으로 구분해서 만들기도 함
# - 통칭하여 character-separated values(csv)라고 부름


# 읽기, 쓰기
# - 텍스트파일 형태로 데이터 처리
# - 일반적 텍스트파일을 처리하듯 파일을 읽어온 후, 한 줄씩 데이터를 처리함


# CSV 파일 읽기
line_counter = 0
data_header = None
customer_list = []
with open('customers.csv', 'r') as csvf:
    while True:
        data = csvf.readline()
        if not data:
            break
        if line_counter == 0:
            data_header = data.split(',')
        else:
            customer_list.append(data.split(','))
        line_counter += 1
csvf.close()

print('Number of customers : ', len(customer_list))
print()
print('Number of fieldnames : ', len(data_header))
print()

print('Header : ', end='')
for header in data_header:
    print(header.replace('\n', ''), end='|')
print()

for i in range(0, 10):
    print(f'Data {i} : ', end='')
    for info in customer_list[i]:
        print(info.replace('\n', ''), end=' | ')
    print()


# 출력해 보면 일반적인 스트링 메소드로는 제어하기 어려운 부분이 있다.
# 가장 눈에 띄는 에러 부분은 단순히 str.split(',')으로 처리했을 경우
# 한 문자열내에 있는 " ~ , - " 컴마를 필드네임 구획하는 컴마와 구별하여 사용할 수 없다는 것이다.
# 이 것은 자칫 엉뚱한 데이터를 추출하게 만들어 데이터 수집에 치명적 결과를 초래할 수 있다. 





















