# Modified coding
with open('yesterday.txt', 'r') as lyric:
    lyric_read = lyric.read()
    print(type(lyric_read))
    lower_lyric = lyric_read.lower()
    counter = lower_lyric.count('yesterday')
    print(counter)
lyric.close()


# My coding
# with open('yesterday.txt', 'r') as yesterday:
#     yesterday_read = yesterday.read()
#     lines = yesterday_read.split('\n')
#     lower_y = 'yesterday'
#     capital_y = lower_y.capitalize()
#     counter = 0
#     for line in lines:
#         words = line.split(' ')
#         for word in words:
#             if lower_y in word or capital_y in word :
#                 counter += 1    
#     print(counter)
# yesterday.close()


# Teacher's coding : using "count()"
# with open('yesterday.txt', 'r') as f:
#     yesterday_lyric = ''
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         yesterday_lyric = yesterday_lyric + line.strip() + '\n'
# f.close()
# num_yesterday = yesterday_lyric.lower().count('yesterday')
# print(num_yesterday)