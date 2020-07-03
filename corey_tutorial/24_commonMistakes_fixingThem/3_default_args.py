# Confusing Default Args

def add_employee(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)

emps = ['John', 'Jane']

add_employee('Corey', emps)
add_employee('Charlie')
add_employee('Young')
print()

# 코딩 문맥 의미상 피고용자 리스트의 default값을 빈 리스트로 지정하고자 하였으나
# 의도와 다르게 'add_employee'메소드를 사용할 때 피고용자 리스트를 지정하지 않으면
# 새로운 리스트를 계속 발생 시킴

# 해결법 : 'add_employee'메소드 실행시 반드시 피고용자 리스트를 명시할 것.
# 또는 아래를 실행하여 정확한 디폴트 변수명을 확인하여 리스트명으로 사용하거나,
# 이미 사용되고 있는 리스트 명이 있다면 리스트명을 통합할 것. 
# print(help(add_employee))


###########################################################

import time
from datetime import datetime

# def display_time(time=datetime.now()):
#     print(time.strftime('%B %d, %Y %H:%M:%S'))

def display_time(time=None):
    if time == None:
        time = datetime.now()
    print(time.strftime('%B %d, %Y %H:%M:%S'))

display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()

# 'display_time' 메소드를 실행하여 매초 시간변화를 보여주고자 하였으나
# 'display_time' 메소드가 최초 실행될 때의 시간을 default값으로 인식하여 계속 그 시각만을 출력함.

# 해결법 : 'display_time' 메소드가 실행될때 마다 "datetime.now()"을 실행하도록 코딩.




