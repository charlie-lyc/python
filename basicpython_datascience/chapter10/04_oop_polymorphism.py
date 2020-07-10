# Ploymorphism(다형성) : 같은 이름 method의 내부 로직을 다르게 작성
# dynamic typing특성으로 인해 파이썬에선ㄴ 같은 부모클래스의 상속에서 주로 발생
# OOP에서 중요한 개념이지만 너무 깊이 알 필요는 없다.


# 같은 부모 클래스를 상속받은 클래스들의 동일한 메소드 실행으로 다양한 결과를 얻음


# Example01
def get_some_data(self, name):
    pass


def get_some_data(self, name, date):
    pass


# Example02
class Person(object):
    pass


class Employee(Person):
    def do_work():
        print('Do work hard!')


class Student(Person):
    def do_work():
        print('Do study hard!')


# Example03
class Animal:
    def __init__(self, name):  # Construct of the class
        self.name = name

    def talk(self):  # Astract method, defined by convention ohly
        raise NotImplementError('Subclass must implement abstract mehod')


class Cat(Animal):
    def talk(self):
        return 'Meow!'


class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'


animals = [Cat('Missy'), Cat('Mr. Mistoffeless'), Dog('Lassie')]

for animal in animals:
    print(animal.name + ': ' + animal.talk())
