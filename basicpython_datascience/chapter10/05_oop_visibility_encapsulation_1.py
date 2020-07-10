# Visibility(가시성) : 객체의 정보를 볼 수있는 레벨을 조절하는 것
# 누구나 객체안의 모든 변수를 볼 필요가 없음
# 1) 객체를 사용하는 사용자가 임의로 정보 수정
# 2) 필요없는 정보에는 접근할 필요가 없음
# 3) 만약 제품으로 판매한다면? 소스의 보호 - Encapsulation

# Encapsulation : 캡슐화 또는 정보 은닉(information hiding)
# 클래스를 설계할 때, 클래스 간 간섭/정보공유의 최소화
# 캡슐이 던져지면, 인터페이스만 알아서 사용야 함
# 예를 들자면 심판 클래스가 축구선수 클래스 가족 정보를 알 필요은 없다.

# Example01
# Product 객체를 Inventory 객체에 추가
# Inventory에는 오직 Product 객체만 들어감
# Inventory에 Product가 몇개인지 확인이 필요
# Inventory에 Product items는 직접 접근이 불가
class Product(object):
    pass


class Inventory(object):
    def __init__(self):
        self.__items = []

    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print('New item added')
        else:
            raise ValueError('Invalid item')

    def get_number_of_items(self):
        return len(self.__items)


myInventory = Inventory()
myInventory.add_new_item(Product())
myInventory.add_new_item(Product())
print(myInventory.get_number_of_items())
print()

myInventory.add_new_item(object)
# print(myInventory.__items)
# # AttributeError: 'Inventory' object has no attribute '__items'
# # " '__'items " : 클래스 내부에서 사용은 가능하나 외부에서는 접근할 수 없는 변수
print()
