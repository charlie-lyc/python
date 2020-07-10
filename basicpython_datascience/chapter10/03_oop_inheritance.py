# OOP Characteristics : Learning Java is recommended.
# 1. Inheritance
# 2. Polymorphism
# 3. Visibility - Encapsulation

# Inheritance(상속) : 부모클래스로 부터 attribute와 method를 물려받은 자식클래스를 생성

# Example01 : Korean클래스는 Person클래스를 상속받고, Person클래스는 object를 상속받는다.
#                object
#                   |
#                Person
#                   |
#                Korean
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Korean(Person):
    pass


first_korean = Korean('Young', 35)
print(first_korean.name)
print()


# Example02
#                   Person
#                      |
#                   Eployee
#           ___________|___________
#          |           |           |
#       Manager      Staff       Hourly
class Person(object):  # 부모 클래스 Person 선언
    def __init__(self, name, age, gender):
        self.name = name  # attribute 선언
        self.age = age
        self.gender = gender

    def about_me(self):  # method 선언
        print('저의 이름은 ' + self.name + '이구요, 나이는 ' + str(self.age) + '살 입니다.')


class Employee(Person):  # 부모 클래스 Person으로부터 상속
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)  # 부모객체 사용
        self.salary = salary
        self.hire_date = hire_date  # attribute 추가

    def do_work(self):  # method 추가
        print('열심히 일을 합시다.')

    def about_me(self):  # 부모 클래스 method 재정의
        super().about_me()  # 부모 클래스 method 사용
        print('제 급여는 ' + str(self.salary) + '원 이구요, 입사일은 ' + self.hire_date + '입니다.')


myPerson = Person('John', 34, 'Male')
myEmployee = Employee('Young', 34, 'Male', 3000000, '2021/07/01')
myPerson.about_me()
myEmployee.about_me()
myEmployee.do_work()
