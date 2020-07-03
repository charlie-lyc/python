### Switch
with open('testfile.txt', 'r') as f:
    file_contents = f.read()
    print(file_contents)
f.close()

### Switch
# f = open('testfile.txt', 'r')
# file_contents = f.read()
# print(file_contents)
# f.close()


words = file_contents.split(' ')
print(len(words))



