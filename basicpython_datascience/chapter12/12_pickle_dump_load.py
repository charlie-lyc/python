# Pickle
# - 파이썬의 객체를 영속화(persistence)하는 built-in 객체
# - 데이터, object 등 실행 중 정보를 저장 => 불러와서 사용
# - 저장해야하는 정보, 계산 결과(모델) 등 활용이 많음

# 눈치 챘겠지만 'wb'는 " encoding='ASCII' " 이다.
import pickle

with open('list.pickle', 'wb') as f1:
    test = [1, 2, 3, 4, 5]
    pickle.dump(test, f1)
f1.close()
with open('list.pickle', 'rb') as f2:
    test_pickle = pickle.load(f2)
    print(test_pickle)
f2.close()
print()


class Multiply(object):
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def multiply(self, number):
        return number * self.multiplier

multiply = Multiply(5)
print(multiply)
print(multiply.multiply(10))
print()


with open('multiply_object.pickle', 'wb') as f3:
    pickle.dump(multiply, f3)
f3.close()
with open('multiply_object.pickle', 'rb') as f4:
    multiply_pickle = pickle.load(f4)
    print(multiply_pickle)
    print(multiply_pickle.multiply(10))
f4.close()




