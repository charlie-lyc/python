# Tuple형태로 Data Struct를 저장하는 방법 : 저장되는 data의 variable을 사전에 저장
from collections import namedtuple
import csv

# Name a Tuple like a Class
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(type(p))
print(p)
print(p[0], p[1])
print()

# Unpack, Properties
x, y = p
print(x, y)
print(p.x, p.y)
print(Point(x=11, y=22))

##############################################

# Where is 'users.csv'?
with open('users.csv', 'r') as cf:
    csv_reader = csv.reader(cf)
    next(csv_reader)
    stduent_list = []
    for line in csv_reader:
        student_list.append(line)
        print(line)

columns = ['user_id', 'integration_id', 'login_id', 'password', 'first_name',
           'last_name', 'full_name', 'sortable_name', 'short_name', 'email', 'status']

# Student = namedtuple('Student', ' '.join(columns))
Student = namedtuple('Student', columns)
student_namedtuple_list = []
for row in student_list:
    student = Student(*row)
    student_namedtuple_list.append(student)
print(student_namedtuple_list)
print(student_namedtuple_list[0].fullname)


# Asterisk in Argument
# 필요로 하는 args가 a, b, c 3개인데 주어지는 자료형이 [a, b, c]일때
# 각 element를 추출하여 입력한다는 의미로 '*'를 사용한다.

# 즉, namedtuple인 Student의 경우에 args가 columns의 element 갯수(11)만큼 있어야 하는데
# 주어진 것은 csv파일로 부터 읽어들인 1줄 데이터에 대한 list 1개이다.
# 따라서 이 list로 부터 각각의 element들을 args로 인식시키기 위해 '*'를 사용했다.
