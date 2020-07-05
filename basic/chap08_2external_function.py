## chapter08-02

## External Functions
## 실제 프로그램 개발 중 자주 사용

##############################################################
# sys, pickle, os, time, random, webbrowser, shutil, temfile #
##############################################################

## example01
import sys

print(sys.argv)
print()

## example02 : 강제 종료
# sys.exit() # Dangerous to execute!

## example03 : 파이썬 패키지 위치
print(sys.path)
print()


## example04 : 객체파일 쓰기
import pickle

f = open('test.obj', 'wb') # 쓰기 허용 상태로 파일을 열어 둠 : 'w'rite 'b'inary
obj = {1: 'python', 2: 'study', 3:'basic'}
pickle.dump(obj, f)
f.close() # 연 파일은 반드시 닫아야 한다 : 그래야 'wb'가 완료된다. 계속 열어두면 메모리 관리 문제

## example05 : 객체파일 읽기
fi = open('test.obj', 'rb') # 읽기 허용 상태로 파일을 열어 둠 : 'r'ead 'b'inary
data = pickle.load(fi)
print(type(data), data)
fi.close() # 연 파일은 반드시 닫아야 한다 : 메모리 관리
print()


## 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
######################################
# mkdir, rmdir(비어 있으면 삭제), rename #
######################################

## example06
import os

print(os.environ)
print()
# {
# 	'TERM': 'xterm-color', 
#  	'SHELL': '/bin/zsh', 
#   'CLICOLOR': '1', 
# 	'TMPDIR': '/var/folders/rg/65f998kx2jdg7l7p6cg8d2540000gn/T/', 
# 	'CONDA_SHLVL': '1', 
# 	'CONDA_PROMPT_MODIFIER': '(base) ', 
# 	'PYTHONIOENCODING': 'utf-8', 
# 	'USER': 'charlie', 
# 	'CONDA_EXE': '/Users/charlie/opt/anaconda3/bin/conda', 
# 	'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.Fdt1QoLE7W/Listeners', 
# 	'__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0x0', 
# 	'_CE_CONDA': '', 
# 	'LSCOLORS': 'Exfxcxdxbxegedabagacad', 
# 	'PATH': '/Users/charlie/opt/anaconda3/bin:/Users/charlie/opt/anaconda3/condabin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/share/dotnet:~/.dotnet/tools:/Library/Apple/usr/bin:/Library/Frameworks/Mono.framework/Versions/Current/Commands:/Library/Frameworks/Python.framework/Versions/3.8/bin', 
# 	'CONDA_PREFIX': '/Users/charlie/opt/anaconda3', 
# 	'PWD': '/Users/charlie/Documents/Inflearn/WorkSpace/Python/basic', 
# 	'XPC_FLAGS': '0x0', 
# 	'PS1': '(base) \\[\\e[0;33m\\]\\u\\[\\e[0m\\]@\\[\\e[0;32m\\]\\h\\[\\e[0m\\]:\\[\\e[0;34m\\]\\w\\[\\e[0m\\]\\$ ', 
# 	'_CE_M': '', 
# 	'XPC_SERVICE_NAME': '0', 
# 	'SHLVL': '1', 
# 	'HOME': '/Users/charlie', 
# 	'GREP_OPTIONS': '--color=auto', 
# 	'CONDA_PYTHON_EXE': '/Users/charlie/opt/anaconda3/bin/python', 
# 	'LOGNAME': 'charlie', 
# 	'CONDA_DEFAULT_ENV': 'base', 
# 	'_': '/Users/charlie/opt/anaconda3/bin/python', 
# 	'LC_CTYPE': 'UTF-8'
# }
print(os.environ['PATH'])
print(os.environ['HOME'])
print(os.environ['USER'])
print()

## example07 : 현재경로
print(os.getcwd()) 
print()


## example08 : 시간 관련 처리
import time

print(time.time())
print()

## example09 : 형태 변환
print(time.localtime(time.time()))
print()

## example10 : 간단 표현
print(time.ctime())
print()

## example11 : 형식 표현 *** 가장 많이 사용 ***
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%h %d %y'))
print(time.strftime('%D'))
print()

## example12 : 시간 간격 발생
for i in range(5):
	print(i)
	time.sleep(0.2)
print()


## example13 : 임의의 난수 반환
import random

print(random.random()) # 0 ~ 1 사이 실수
print(random.randint(0, 100)) # 0 ~ 100 사이정수
print()

## example14 : 섞기
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)
print()

## example15 : 무작위 선택
c = random.choice(d)
print(c)
print()


## example16 : 본인 os의 웹브라우저 실행
import webbrowser

webbrowser.open('http://google.com')
webbrowser.open_new('http://google.com')
webbrowser.open_new('http://google.com')

