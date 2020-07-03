# Reserved Keyword Mistake
from math import radians, sin

### "radians"가 처음 사용할 때 'radians(90)'에서는 함수로써 사용됨.
# radians = radians(90)
# print(sin(radians))
# print()

rad90 = radians(90)
print(sin(rad90))
print()

### 하지만 두 번째 사용할 때 'radians(45)'에서는 이미 함수가 아님.
### 단지 'radians(90)'의 결과값을 할당 받은 변수임.
### 그래서 아래와 같은 에러 발생.
# TypeError: 'float' object is not callable
rad45 = radians(45)
print(rad45)

# 예약어는 변수의 이름으로 사용하지 않는 것이 원칙이다!!!
# 해결법 : 변수이름 수정



