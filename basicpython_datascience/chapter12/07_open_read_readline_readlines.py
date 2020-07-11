# File I/O
# - 파이썬은 파일 처리를 위해 'open'키워드를 사용
# - 'open'명령의 모드 : 'r', 'w', 'a' (읽기, 쓰기, 추가)
# f = open('<file name>', '<mode>')


# File Read
# read() : 파일내의 내용 전체를 읽어 문자열로 반환
f1 = open('i_have_a_dream.txt', 'r', encoding='utf8')
content1 = f1.read()
print(type(content1))
print(content1)
f1.close()
print()


# readline() : 파일내의 내용 한줄만 읽어 문자열로 반환
f2 = open('i_have_a_dream.txt', 'r', encoding='utf8')
content2 = f2.readline()
print(type(content2))
print(content2)
f2.close()
print()


# readlines() : 파일내의 내용 전체를 한줄씩 읽어 문자열들의 리스트로 반환
f3 = open('i_have_a_dream.txt', 'r', encoding='utf8')
content3 = f3.readlines()
print(type(content3))
print(content3)
print()
print(content3[:2])
print()
for line in content3[:2]:
    print(line)
f3.close()






