import os
from datetime import datetime


print(os.getcwd())
os.chdir('/Users/charlie/Documents/CoreySchafer_PythonTutorial')
print(os.getcwd())
print()


print(help(os.stat))
### 딱히 정보가 없는 것 같아 직접 조사한 내용 발췌
### os.stat(path) : 주어진 경로(파일)과 관련된 시스템 통계(정보) 호출
# st_mode : 파일 모드
# st_ino : 아이노드 번호
# st_dev : 장비 식별자 
# st_nlink : 링크 번호
# st_uid : 유저 아이디
# st_gid : 유저가 속한 그룹 아이디
# st_size : 파일 사이즈
# st_atime : 마지막 액세스 시간
# st_mtime : 마지막 수정 시간
# st_ctime : 마지막 메타데이타 변경 시간
print()


print(help(datetime.fromtimestamp))
print()


mod_time = os.stat('demo.txt').st_mtime
print(mod_time)
print(datetime.fromtimestamp(mod_time))
print()

### etc
print(os.stat('demo.txt').st_mode)
print(os.stat('demo.txt').st_ino)
print(os.stat('demo.txt').st_dev)
print(os.stat('demo.txt').st_nlink)
print(os.stat('demo.txt').st_uid)
print(os.stat('demo.txt').st_gid)
print()
print(os.stat('demo.txt').st_size)
print(os.stat('demo.txt').st_atime)
print(os.stat('demo.txt').st_mtime)
print(os.stat('demo.txt').st_ctime)





