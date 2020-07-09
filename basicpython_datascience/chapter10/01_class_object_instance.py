# 프로그램을 기능별로 나누어 재사용하는 방법
# 1. 함수
# 2. 객체
# 3. 모듈

# 클래스 이름 형태
# 1. snake_case
# 2. camelCase
# 3. PascalCase

# '__--__' : 특수한 예약함수나 변수
# __main__
# __str__
# __repr__
# __add__


# Class
# '클래스예약어' '클래스이름' '상속받는객체명'
class SoccerPlayer(object):
    # 객체 초기화 예약 함수
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print('Change back number of player : from %d to %d' % (self.back_number, new_number))
        self.back_number = new_number

    def __str__(self):
        return 'Hello, My name is %s. I play in %s in center.' % (self.name, self.position)


# Object(Instance)
# '객체명'    '클래스명'  '__init__함수 Interface' '초기값'
jinhyun = SoccerPlayer('Jinhyun', 'MF', 10)
print(jinhyun)
# 'def __str__(self):' 없을 때
# <__main__.SoccerPlayer object at 0x7fcb339c6fa0>
print('Present Back Number is ', jinhyun.back_number)
jinhyun.change_back_number(5)
print('Present Back Number is ', jinhyun.back_number)
jinhyun.back_number = 20
print('Present Back Number is ', jinhyun.back_number)

# 다수의 인원 정보 저장하기
# 이차원 리스트 사용
names = ['Jin', 'Young', 'Jun', 'Hong', 'Seo']
positions = ['MF', 'DF', 'CF', 'WF', 'GK']
numbers = [10, 15, 20, 3, 1]
players = [[name, position, number] for name, position, number in zip(names, positions, numbers)]

print(players)
print(players[0])
print()

# 클래스로 선언
players_objects = [SoccerPlayer(name, position, number)
                   for name, position, number in zip(names, positions, numbers)]
print(players_objects[0])
