import requests


r = requests.get('https://imgs.xkcd.com/comics/python.png')

with open('python_copy.png', 'wb') as wi:
	wi.write(r.content)

