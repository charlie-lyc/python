# chapter09-02

# CSV(Comma Separated Values) File Read & Write

## CSV : MEME - text/csv

####################################
# reader(), DictReader(), writer() #
####################################

import csv

## example01 : 읽기
with open('./resource/test1.csv', 'r') as f1:
    # delimiter=',' => default. '구획문자'를 명시
    reader1 = csv.reader(f1, delimiter=',')
    ### Header Skip ###
    next(reader1)
    # 객체 확인
    print(reader1)
    # 자료형 확인
    print(type(reader1))
    # 속성 확인 : __iter__ => 반복문을 사용할 수 있다.
    print(dir(reader1))
    print()
    # reader 출력 : __iter__ 이용
    for c in reader1:
        # print(type(c), c)
        print(' : '.join(c))
f1.close()
print()


# example02 : '구획문자'가 다를 경우
with open('./resource/test2.csv', 'r') as f2:
    reader2 = csv.reader(f2, delimiter='|')
    next(reader2)

    for c in reader2:
        print(' = '.join(c))
f2.close()
print()


# example03 :
with open('./resource/test1.csv', 'r') as f3:
    reader3 = csv.DictReader(f3)
    next(reader3)
    print(reader3)
    print(type(reader3))
    print(dir(reader3))
    print()
    for d in reader3:
        # print(type(t), t)
        for k, v in d.items():
            print(k, v)
        print()
f3.close()
print()


# example04
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
with open('./resource/write1.csv', 'w') as f4:
    print(dir(csv))
    print()
    wt = csv.writer(f4)
    print(wt)
    print()
    print(type(wt))
    print()
    ###########################################################################################
    ## writerow(), writerows() ## 'writer()'에만 있다. # reader()에는 readrow(),readrowas()가 없다. #
    ###########################################################################################
    print(dir(wt))
    for v in w:  # w의 한 요소인 리스트 한 개가 CSV파일에서 한 개의 레코드가 된다.
        wt.writerow(v)
f4.close()
print()


with open('./resource/write1.csv', 'r') as f5:  # 제대로 쓰여졌는지 확인
    reader5 = csv.reader(f5)

    for li in reader5:
        print(','.join(li))
f5.close()
print()


# example05
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
with open('./resource/write2.csv', 'w') as f6:
    # 필드명
    fields = ['One', 'Two', 'Three']
    # DictWriter
    wt = csv.DictWriter(f6, fieldnames=fields)
    # write header
    wt.writeheader()
    for v in w:
        wt.writerow({'One': v[0], 'Two': v[1], 'Three': v[2]})
f6.close()
print()


with open('./resource/write2.csv', 'r') as f7:  # 제대로 쓰여졌는지 확인
    reader7 = csv.DictReader(f7)
    for d in reader7:
        for k, v in d.items():
            print(k, v)
        print()
f7.close()
print()
