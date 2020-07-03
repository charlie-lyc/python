
import requests


r = requests.get('https://imgs.xkcd.com/comics/python.png')

print(r)
print(r.status_code)
print(r.ok)
print(r.url)
print()

# print(r.headers)
# {
# 	'Connection': 'keep-alive', 
# 	'Content-Length': '90835', 
# 	'Server': 'nginx', 
# 	'Content-Type': 'image/png', 
# 	'Last-Modified': 'Mon, 01 Feb 2010 13:07:49 GMT', 
# 	'ETag': '"4b66d225-162d3"', 
# 	'Expires': 'Thu, 02 Jul 2020 22:43:39 GMT', 
# 	'Cache-Control': 'max-age=300', 
# 	'Accept-Ranges': 'bytes', 
# 	'Date': 'Thu, 02 Jul 2020 23:45:59 GMT', 
# 	'Via': '1.1 varnish', 
# 	'Age': '178', 
# 	'X-Served-By': 
# 	'cache-hnd18738-HND', 
# 	'X-Cache': 'HIT', 
# 	'X-Cache-Hits': '1', 
# 	'X-Timer': 'S1593733559.439909,VS0,VE1'
# }

# print(dir(r))

