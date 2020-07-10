# Example02
# Product 객체를 Inventory 객체에 추가
# Inventory에는 오직 Product 객체만 들어감
# Inventory에 Product가 몇개인지 확인이 필요
# Inventory에 Product items 접근이 허용
class Product(object):
    pass


class Inventory(object):
    def __init__(self):
        self.__items = []

    # def items(self):
    #     return self.__items

    @property  # decorator
    def items(self):
        return self.__items

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

# print(myInventory.items())
print(myInventory.items)
print()


# 좋은 코드는 아님 : 클래스의 속성과 메소드를 통해 접근하는 것이 바람직
items = myInventory.items
# items.append(object) # 가능함
items.append(Product())
print(myInventory.get_number_of_items())
