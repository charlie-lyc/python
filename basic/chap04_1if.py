# chapter04-01

# IF : conditional statement

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

# example02
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

# example03
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

# example04
score1 = 70
score2 = 'A'
if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')
print()

# example05
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('Administrator')

if id2 == 'admin' and grade == 'platinum':
    print('Super Administrator')
print()

# example6 : multi condition
num = 75
if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : c')
else:
    print('Fail')
print()

# Nested IF
grade = 'A'
total = 95
if grade == 'A':
    if total >= 90:
        print('scholarship 100%')
    elif total >= 80:
        print('scholarship 80%')
    else:
        print('scholarship 50%')
else:
    print('no scholarship')
print()

# in, not in
q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {'name': 'Lee', 'city': 'Seoul', 'grade':'A'}
r = (10, 12, 14)
print(15 in q)
print(90 in w)
print(12 not in r)
print('name' in e)
print('Seoul' in e.values())
print()


