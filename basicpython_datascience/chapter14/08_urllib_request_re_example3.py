import urllib.request
import re

base_url = 'http://web.eecs.umich.edu/~radev/coursera-slides'
# 아쉽게도 현재는 없어진 웹페이지이다. 따라서 이하 코드 실행이 안된다.
html = urllib.request.urlopen(base_url)
contents = html.read()
html_contents = str(contents.decode('utf8'))

file_list = re.findall(r'nlp[A-Za-z0-9\_\.]*\.pdf', html_contents)

for file in file_list:
    file_name = ''.join(file)
    full_url = base_url + file_name
    print(full_url)
    fname, header = urllib.request.urlretrieve(full_url, file_name)
    print(fname)
    print(header)
    print('End Download')
