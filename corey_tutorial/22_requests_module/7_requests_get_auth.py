
############ https://httpbin.org/ ############

import requests

### 웹브라우저 주소창에 'https://httpbin.org/basic-auth/Corey/testing' 입력.
### 유저와 패스워드 입력 창이 뜨고 여기에 순서에 맞게 'Corey/testing' 입력하면 아래와 같이 데이터 출력.
### 유저와 패스워드가 맞게 입력되지 않으면 계속에 입력 창 출력.
# {
#   "authenticated": true, 
#   "user": "Corey"
# }


r = requests.get('https://httpbin.org/basic-auth/Corey/testing', auth=('Corey', 'testing'))

print(r)
print()
print(r.text)
print()
print(r.json())
print()


# re = requests.get('https://httpbin.org/basic-auth/Corey/testing', auth=('coreyms', 'testing'))
# print(re)
# <Response [401]>


