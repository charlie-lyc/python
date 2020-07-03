
### Mode
## Text : 'r(t)',  'w(t)', 'a(t)'
## Image : 'rb', 'wb'


## Copy File
with open("test.txt", "r") as rf:
    with open("test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)

## Copy image starts, without chunks: 
with open('blow_fish1.jpg', 'rb') as rf:
    with open('blow_fish_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)


## Copy image with chunks:
with open('blow_fish.jpg', 'rb') as rf:
    with open('blow_fish_copy2.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


## UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
# with open('blow_fish.jpg', 'r') as rf:
#     with open('blow_fish_copy.jpg', "w") as wf:
#         for line in rf:
#             wf.write(line)
