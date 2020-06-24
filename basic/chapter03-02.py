# chapter03-02
# string

str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you'''
print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))
print()

# empty string
str1_t1 = ''
str2_t2 = str()
print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))
print()

# escape
print("I'm a boy")
print('I\'m a boy')
print('a\"to\"b')
escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)
print()

# new tab, new line
t_s1 = "Click\tStart!"
t_s2 = "New Line\nCheck!"
print(t_s1)
print(t_s2)
print()

# raw string
escape_s = 'D:\\python\\test'
raw_s = r'D:\python\test'
print(escape_s)
print(raw_s)
print()

# multi line
multi_str1 = '''
String
Multi Line
Test
'''
# binding
multi_str2 = \
'''
String
Multi Line
Test
'''
# multi_str2 = 
# '''
# String
# Multi Line
# Test
# '''
multi_str3 = \
'String' \
'Multi Line' \
'Test'
print(multi_str1)
print(multi_str2)
print(multi_str3)
print()

# string opreration
str_o1 = "python"
str_o2 = "apple"
str_o3 = "How are you doing"
str_o4 = "Seoul, Daejeon, Busan, Jinju"
print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('p' not in str_o1)
print('P' not in str_o1)
print()

# type transformation
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))
print()

# function : captitalize, count, endswith, isalnum, isalpha, replace, sorted, split, startswith, upper...
print('Capitalize: ', str_o1.capitalize())
print('Endswith: ', str_o2.endswith('!'))
print('Replace: ', str_o1.replace('thon', ' good'))
print('Sorted: ', sorted(str_o1))
print('Split: ', str_o3.split(' '))
print('Split: ', str_o4.split(', '))
print()

# iteration(sequence) : __iter__
im_str = 'Good Boy'
print(dir(im_str))
for i in im_str:
    print(i)
print()

#####***** slicing *****#####
str_sl = 'Nice Python'
print(len(str_sl))
# practice
print(str_sl[0:3])
print(str_sl[5:])
print(str_sl[:len(str_sl)])
print(str_sl[1:9:2])
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])
print()

# ASCII code (or Unicode)
a = 'z'
# from character to ascii
print(ord('z'))
print(ord(a))
# from ascii to character
print(chr(122))
