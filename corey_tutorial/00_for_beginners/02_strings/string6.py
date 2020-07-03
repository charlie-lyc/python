
greeting = 'Hello'

### type() : identify class of object
print(type(greeting))
# <class 'str'>
print()


### dir() : identify all attributes and method functions
print(dir(greeting))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
print()


### help() : identify all inforamation of class ('str')
print(help(str))
# Help on class str in module builtins:
# class str(object)
#  | ...
# None
print()

# identify partial information of class 'str', especially, method function 'lower'
print(help(str.lower))
# Help on method_descriptor:
# lower(self, /)
#     Return a copy of the string converted to lowercase.
# None
print()

# identify 'print' function
print(help(print))
# Help on built-in function print in module builtins:
# print(...)
#     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)    
#     Prints the values to a stream, or to sys.stdout by default.
#     Optional keyword arguments:
#     file:  a file-like object (stream); defaults to the current sys.stdout.
#     sep:   string inserted between values, default a space.
#     end:   string appended after the last value, default a newline.
#     flush: whether to forcibly flush the stream.
# None
