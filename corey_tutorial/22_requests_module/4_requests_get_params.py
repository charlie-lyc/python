
############ https://httpbin.org/ ############

import requests


# r = requests.get('https://httpbin.org/get?page=2&count=25')

payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)


print(r.url)
# https://httpbin.org/get?page=2&count=25
print()
print(r.text)
### Same result in web browser 'https://httpbin.org/get?page=2&count=25'
# {
#   "args": {
#     "count": "25", 
#     "page": "2"
#   }, 
#   "headers": {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
#     "Accept-Encoding": "gzip, deflate, br", 
#     "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6", 
#     "Host": "httpbin.org", 
#     "Sec-Fetch-Dest": "document", 
#     "Sec-Fetch-Mode": "navigate", 
#     "Sec-Fetch-Site": "none", 
#     "Upgrade-Insecure-Requests": "1", 
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", 
#     "X-Amzn-Trace-Id": "Root=1-5efe7440-8d1826134a86ffbfaf6758ff"
#   }, 
#   "origin": "112.223.48.67", 
#   "url": "https://httpbin.org/get?page=2&count=25"
# }

print(r.headers)
# {
# 	'Date': 'Thu, 02 Jul 2020 23:55:00 GMT', 
# 	'Content-Type': 'application/json', 
# 	'Content-Length': '362', 
# 	'Connection': 'keep-alive', 
# 	'Server': 'gunicorn/19.9.0', 
# 	'Access-Control-Allow-Origin': '*', 
# 	'Access-Control-Allow-Credentials': 'true'
# }


