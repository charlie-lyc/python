with open('i_have_a_dream.txt', 'r', encoding='utf8') as f1:
    i = 0
    while True:
        line = f1.readline()
        if not line:
            break
        # print()함수내에 '\n'이 있고, 각 line 끝에도 '\n'이 있다.
        print(str(i) + ' === ' + line, end='')
        i += 1
    print()
f1.close()
print()


with open('i_have_a_dream.txt', 'r', encoding='utf8') as f2:
    i = 0
    while True:
        line = f2.readline()
        if not line:
            break
        print(str(i) + ' === ' + line.replace('\n', ''))
        i += 1
f2.close()
print()