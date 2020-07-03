
############ https://httpbin.org/ ############

import requests


payload = {'user': 'Corey', 'passwd': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)


print(r.url)
# https://httpbin.org/post
print()
print(r.text)
# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {
#     "passwd": "testing", 
#     "user": "Corey"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Content-Length": "34", 
#     "Content-Type": "application/x-www-form-urlencoded", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.24.0", 
#     "X-Amzn-Trace-Id": "Root=1-5efe7848-7b8a707266acef482a1ccee2"
#   }, 
#   "json": null, 
#   "origin": "112.223.48.67", 
#   "url": "https://httpbin.org/post"
# }


