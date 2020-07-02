## chapter06-01

## OOP : Object Orinented Programming
## Calss, Instance, Self, Instance Method, Instance Variable

## 클래스와 인스턴스 차이 이해
## 네임스페이스 : 객체를 인스턴스화할 때 저장된 공간
## 클래스 변수 : 직접 접근 가능, 공유
## 인스턴스 변수 : 객체마다 별도 존재

# class Dog(object): # object Inheritance
#     pass

# class Dog():
#     pass

# class Dog:
#     pass


############### example01 ###############
class Dog:  # Object Inheritance
    # Class Attribute
    species = 'firstdog'
    # Initializing Method 
    def __init__(self, name, age):
    	# Instance Attribute
        self.name = name
        self.age = age

# class information
print(Dog)  # <class '__main__.Dog'>
print()

# instancing
a = Dog('Mickey', 2)
b = Dog('Mini', 3)
c = Dog('Mickey', 2)
print(type(a), a) # < class '__main__.Dog' > <__main__.Dog object at ... >
print(type(b), b) # class, object
print()

# compare
print(a == b)
print(a == c)
print(id(a), id(b), id(c))
print()

# name space
print('Dog1 :', a.__dict__)
print('Dog2 :', b.__dict__)
print()

# instance, class attribute
print('{} is {} and {} is {}.'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
	print('{} is a {}.'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)
# print(Dog.name)
# print(Dog.age)
print()


############### example02 ############### : self는 instance 자신을 의미한다.
class SelfTest:
	def func1(self):
		print('Func1 called')
	def func2():
		print('Func2 called')

f = SelfTest()

print(dir(f))
print()
print(id(f))
print()

f.func1()
# f.func2() # TypeError: func2() takes 0 positional arguments but 1 was given
print()

# SelfTest.func1() # TypeError: func1() missing 1 required positional argument: 'self'
SelfTest.func2()
print()


############### example03 ############### : Class Variable, Instance Variable
class Warehouse:
	# class variable
	stock_num = 0
	def __init__(self, name):
		# instance variable
		self.name = name
		Warehouse.stock_num += 1
	def __del__(self):
		Warehouse.stock_num -= 1

tool1 = Warehouse('hammer')
tool2 = Warehouse('saw')

print(Warehouse.stock_num) # class variable
# print(tool1.stock_num)
# print(tool2.stock_num)
print()
print(tool1.name) # instance variable
print(tool2.name) # intance variable
print()
print(tool1.__dict__) # instance name space : 클래스의 매개변수(stock_num)는 공유 된다고 했는데 인스턴스 네임 스페이스에서 보이지 않는다.
print(tool2.__dict__) # instance name space
print()
print(Warehouse.__dict__) # class name space : 인스턴스 네임 스페이스에서 보이지 않을 경우 클래스 네임 스페이스에서 찾을 수 있다.
print()

Warehouse.stock_num = 50 # Bad Approach !!!
print('Before : ', Warehouse.stock_num)
print()
print(Warehouse.__dict__)
print()

del(tool1)
# del tool1
print('After : ',Warehouse.stock_num)
print()


############### example04 ###############
class Doggie:

    species = 'firstdog'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
    	return '{} is {} years old.'.format(self.name, self.age)

    def speak(self, sound):
    	return '{} says {}!'.format(self.name, sound)

# instancing
doggie1 = Doggie('Julie', 4)
doggie2 = Doggie('Marry', 10)
# call method
print(doggie1.info())
print(doggie2.info())
print()
print(doggie1.speak('Mung Mung'))
print(doggie2.speak('Wal Wal'))
print()
















