with open('test2.txt', 'w') as f:
    # Writing Starts:
    f.write('Test')
        # Then go back to start
    f.seek(0)
    # And Overwrite
    f.write('R')

    print(f.seek)
    # <built-in method seek of _io.TextIOWrapper object at 0x7fb2a128d2b0>
    print()
    print(help(f.seek))
    # Change the stream position to the given byte offset.
    # Values for whence are:   
    #  * 0 -- start of stream (the default); offset should be zero or positive
    #  * 1 -- current stream position; offset may be negative
    #  * 2 -- end of stream; offset is usually negative
    # Return the new absolute position.
f.close()
print()


## TypeError: '<' not supported between instances of 'str' and 'int'
# with open('test2.txt', 'w') as f:
#     # 'str' is not supported in "seek()"
#     f.seek('t')
#     f.write('ful')
# f.close()
# print()


## io.UnsupportedOperation: not writable
# with open("test.txt", "r") as f:
#     f.write("Test")

