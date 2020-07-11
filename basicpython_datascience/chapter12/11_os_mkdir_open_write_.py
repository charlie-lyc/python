# Directory 만들기 : os모듈을 사용

import os

print(os.getcwd())
print()

# # "os.path.isdir()"
if not os.path.isdir('log'):
    os.mkdir('log')
else:
    print('Directory already exists.')
print()

# print(os.listdir())
# print()

# for d in sorted(os.listdir()):
#     print(d)
# print()

# # "os.path.exists()"
if not os.path.exists('log/count_log.txt'):
    with open('log/count_log.txt', 'w', encoding='utf-8') as f:
        f.write('기록이 시작됩니다.\n')
        f.close()
else:
    with open('log/count_log.txt', 'a', encoding='utf-8') as f:
        f.write('기록이 추가됩니다.\n')
        f.close()


import random, datetime

with open('log/count_log.txt', 'a', encoding='utf-8') as f1:
    for i in range(1, 11):
        stamp = str(datetime.datetime.now())
        value = str(random.random() * 1000000)
        log_line = stamp + '\t' + value + ' 값이 생성되었습니다.\n'
        f1.write(log_line)
f1.close()


# Summary :
# os.getcwd()
# os.listdir()
# os.path.isdir('<디렉토리명>')
# os.path.exists('<디렉토리명>/<파일명>')
