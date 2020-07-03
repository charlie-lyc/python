
############ https://httpbin.org/ ############

import requests

### 웹브라우저 주소창에 'https://httpbin.org/basic-auth/delay/5' 입력.
### 그러면 3초 후에 반응(데이터)을 보냄
# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {}, 
#   "headers": {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
#     "Accept-Encoding": "gzip, deflate, br", 
#     "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6", 
#     "Host": "httpbin.org", 
#     "Sec-Fetch-Dest": "document", 
#     "Sec-Fetch-Mode": "navigate", 
#     "Sec-Fetch-Site": "none", 
#     "Sec-Fetch-User": "?1", 
#     "Upgrade-Insecure-Requests": "1", 
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", 
#     "X-Amzn-Trace-Id": "Root=1-5efe8842-ed5b5128584a581483cb342c"
#   }, 
#   "origin": "112.223.48.67", 
#   "url": "https://httpbin.org/delay/3"
# }


r = requests.get('https://httpbin.org/delay/1', timeout=3)
print(r)
print(r.ok)
print()


### raise 'ReadTimeout'
# re = requests.get('https://httpbin.org/delay/3', timeout=2)
# print(re)
###  :
###  :
### raise ReadTimeout(e, request=request)
### requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='httpbin.org', port=443): Read timed out. (read timeout=2)

