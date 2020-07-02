## chapter09-01

## File Read & Write

# 읽기 모드 : r(ead)
# 쓰기 모드 : w(rite)
# 추가 모드 : a(ppend)
# 텍스트 모드 : t(ext) - 기본값(default)
# 바이너리 모드 : b(inary)

# 상대 경로 : "../ ", "./ "
# 절대 경로 : "/Users/charlie/ "


## example01 : read() 읽기

# f = open('/Users/charlie/Documents/Inflearn/WorkSpace/Python/basic/resource/it_news.txt', 'rt', encoding='UTF-8') # 절대 경로, 텍스트모드 읽기, 인코딩방식 명시
# f = open('./resource/it_news.txt', 'rt', encoding='UTF-8') # 상대 경로 
# f = open('resource/it_news.txt', 'r') # 현재경로 생략, 텍스트모드 생략, 인코딩방식 생략

f = open('./resource/it_news.txt', 'r', encoding='UTF-8')
# 자료형(클래스) 확인
print(f)
print(type(f))
print()
# 속성(의 종류) 확인
print(dir(f))
print()
# 파일 이름 확인
print(f.name)
print()
# 파일 모드 확인
print(f.mode)
print()
# 파일 인코딩 확인
print(f.encoding)
print()
# 파일 내용 출력
contents = f.read()
print(contents)
f.close() ###*** 열어서 실행한 작업이 끝났으면 반드시 다시 닫아라!!! ***###
print('-' * 15)


## example02

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as fi:
	cts = fi.read()
	print(cts)
	print(iter(cts))
	print(list(cts))
fi.close()
print()


## example03
# read() : 전체 읽기
# read(10) : 10byte 읽기

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as fil:
	con1 = fil.read(20)
	print(con1)
	con2 = fil.read(20) # 파일 내에 커서가 있어 앞서 읽어 들인 위치를 기억하고 있다.
	print(con2)
	fil.seek(0, 0) # 커서를 다시 처음 부분으로 이동시킴
	con3 = fil.read(20)
	print(con3)
fil.close()
print()


## example04
# readline() : 한 줄씩 읽기

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as file:
	line1 = file.readline()
	print(line1)
	line2 = file.readline(20)
	print(line2)
file.close()
print()


## example05
# readlines() : 전체를 읽은 후 라인 단위 리스트로 저장 *** 많이 사용 ***

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as file1:
	cont = file1.readlines() # 문단이 바뀔시 '\n'도 하나의 요소로 리스트에 저장
	print(cont)
	print()
	for c in cont:
		print(c, end='')
file1.close()
print()


## example06 : wirte() 쓰기

with open('./resource/contents1.txt', 'w') as f1: # 기존의 있던 파일이라면 덮어쓰게 되고, 기존에는 없던 새로운 파일이라면 파일 생성.
	f1.write('Hello, World!\n')
f1.close()

with open('./resource/contents1.txt', 'w') as f2:
	f2.write('I Love Python!\n')
f2.close()


## example07 : 'a'모드로 추가하여 쓰기
with open('./resource/contents1.txt', 'a') as f3:
	f3.write('I Love Python So Much!\n')
f3.close()


## example08
# writelines() : '리스트'를 '파일'에 쓰기 - "readlines()"를 활용하면 좋을 듯
with open('./resource/contents2.txt', 'w') as f4:
	li = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
	f4.writelines(li)
f4.close()


## example09 : anything else
with open('./resource/contents3.txt', 'w') as f5:
	print('Test Text Write!', file=f5)
	print('Test Text Write!', file=f5)
f5.close()










