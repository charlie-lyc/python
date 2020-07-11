# File Write
# mode : 'w', 'a'
# encoding : 'utf8'


# write() : mode 'w'
f1 = open('count_log.txt', 'w', encoding='utf8')
for i in range(1, 11):
    data = '%d번째 줄입니다.\n' % i
    f1.write(data)
f1.close()


# write() : mode 'a'
with open('count_log.txt', 'a', encoding='utf8') as f2:
    for i in range(11, 21):
        data = f'{i}번째 줄입니다.\n'
        f2.write(data)
f2.close()