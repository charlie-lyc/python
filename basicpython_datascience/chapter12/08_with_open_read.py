# # with 구문 : 좀더 논리적인 구성
with open('i_have_a_dream.txt', 'r', encoding='utf8') as f1:
    content = f1.read()
    print(content)
f1.close()
print()


with open('i_have_a_dream.txt', 'r', encoding='utf8') as f2:
    content = f2.read()
    line_list = content.split('\n')
    print(line_list)
    print()
    word_list1 = [line.split(' ') for line in line_list]
    print(word_list1)
    print()
    word_list2 = []
    for line in line_list:
        for word in line.split(' '):
            word_list2.append(word) 
    print(word_list2)
    print()
f2.close()
print('Total number of characters in content;', len(content))
print('Total number of lines ;', len(line_list))
print('Total number of words ;', len(word_list2))