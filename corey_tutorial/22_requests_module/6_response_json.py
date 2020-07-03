
############ https://httpbin.org/ ############

import requests


payload = {'user': 'Corey', 'passwd': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)


print(dir(r))
print()
print(r.json)
# <bound method Response.json of <Response [200]>>
print()

print(r.json())
### Same result of "print(r.text)"
# {
# 	'args': {}, 
# 	'data': '', 
# 	'files': {}, 
# 	'form': {
# 		'passwd': 'testing', 
# 		'user': 'Corey'
# 	}, 
# 	'headers': {
# 		'Accept': '*/*', 
# 		'Accept-Encoding': 'gzip, deflate', 
# 		'Content-Length': '34', 
# 		'Content-Type': 'application/x-www-form-urlencoded', 
# 		'Host': 'httpbin.org', 
# 		'User-Agent': 'python-requests/2.24.0', 
# 		'X-Amzn-Trace-Id': 'Root=1-5efe7c7a-a5865cc0910b7210109381c8'
# 	}, 
# 	'json': None, 'origin': '112.223.48.67', 
# 	'url': 'https://httpbin.org/post'
# }
print()

r_dict = r.json()
print(r_dict['form'])


