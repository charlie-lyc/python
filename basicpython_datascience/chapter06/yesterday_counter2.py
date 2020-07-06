with open('yesterday.txt', 'r') as lyric:
    lyric_read = lyric.read()
    counter_Y = lyric_read.count('Yesterday')
    counter_y = lyric_read.count('yesterday')
    print(f"Number of 'Yesterday' in lyric : {counter_Y}")
    print(f"Number of 'yesterday' in lyric : {counter_y}")
lyric.close()
