# chapter04-01

# IF sentence

# 0이 아닌수, "abc", [1, 2, 3], (1, 2, 3), ...
print(type(True))
# 0, "", [], (), {}, ...
print(type(False))
print()

# example01
if True:
    print('Good')
if False:
    print('Bad')
if 'a':
    print('Good')
if '':
    print('Bad')
print()

# example2
if False:
    print('Bad!')
else:
    print('Good!')
print()

# relational operator : >, >=, <, <=, ==, !=
x = 15
y = 10
print(x == y)
print(x != y)
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
print()

# example3
city = ''
if city:
    print('You are in %s.' % city)
else:
    print('Plz enter your city :')
print()

city = 'Seoul'
if city:
    print('You are in {}.'.format(city))
else:
    print('Plz enter your city :')
print()

#####***** logical operator *****##### : and, or, not
a = 75
b = 40
c = 10
print('and :', a > b and b > c)
print('or :', a > b or b > c)
print('not :', not a > b)
print('not :', not b > c)
print('not True :', not True)
print('not False :', not False)
print()

# priority : arithmetic > relational > logical
print('e1 ;', 3 + 12 > 7 + 3)
print('e2 ;', 5 + 10 * 3 > 7 + 3 * 20)
print('e3 ;', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 ;', 5 + 10 > 0 and not 7 + 3 == 10)
print()

# example4
score1 = 70
score2 = 'A'
if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')

# example5
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 = 'admin':
    print('Entering Administrator')

