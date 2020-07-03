
############ https://httpbin.org/ ############

import requests

# timeout=3 : 3초까지 반응 수신
r = requests.get('https://httpbin.org', timeout=3)

print(r)
