with open('test.txt', 'r') as f:
    ### Small Files: read all at once.
    f_contents = f.read()
    print(f_contents)
f.close()
print()


with open('test.txt', 'r') as f:
    ### Big Files: read all and store line by line in a list.
    f_contents = f.readlines()
    print(f_contents)
f.close()
print()


with open('test.txt', 'r') as f:
    ### Read a line at a time : with the extra lines: 
    f_contents = f.readline()
    print(f_contents)
    f_contents = f.readline()
    print(f_contents)
f.close()
print()


with open('test.txt', 'r') as f:
    # Read a line at a time : without the extra lines.
    f_contents = f.readline()
    print(f_contents, end='')
    f_contents = f.readline()
    print(f_contents, end='')
f.close()
print()


with open('test.txt', 'r') as f:
    # Check "__iter__"
    print(dir(f))
    print()
    ### Iterate through the file:
    for line in f:
        print(line, end='')
f.close()
print()


# Here, remember that everytime reading a file, 'cursor' keeps moving.
with open('test.txt', 'r') as f:
    ### Print out by 10 bytes(charaters).
    f_contents = f.read(10)
    print(f_contents, end='')
    # Print out one more time.
    f_contents = f.read(10)
    print(f_contents)
f.close()
print()


with open('test.txt', 'r') as f:
    # Iterate through small chunks: with 10 bytes(charaters).
    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)
f.close()
print()


with open('test.txt', 'r') as f:
    # Iterate through small chunks: with 10 bytes(charaters).
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents)
    ### Go back to start
    f.seek(0)
    f_contents = f.read(size_to_read)
    print(f_contents)
    print()

    print(f.tell)
    # <built-in method tell of _io.TextIOWrapper object at 0x7faccf38d930>
    print()
    print(help(f.tell))
    # Return "current stream position" by "bytes"
    print()

    ### Check current position of cusor from start
    print(f.tell())
f.close()
print()


with open('test.txt', 'r') as f:
    # Iterate through small chunks: with 10 bytes(charaters).
    size_to_read = 10
    f_contents = f.read(size_to_read)
    # Print out with '*' after reading a file
    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
f.close()
print()




















