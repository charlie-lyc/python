
# pip install requests

import requests


response = requests.get('http://xkcd.com/353')
print(response)
# <Response [200]>
print()
print('>>>>>>>>>>>>>>>>>>>>>>>>')
print()
print(response.content)
print('>>>>>>>>>>>>>>>>>>>>>>>>')
print()
print(response.text)
print('>>>>>>>>>>>>>>>>>>>>>>>>')


# print(dir(response))
# print(help(response))
# :
# |  content                                => image by "binary code"
# |      Content of the response, in bytes.
# :
# |  text                                   => "str"
# |      Content of the response, in unicode.
# |      
# |      If Response.encoding is None, encoding will be guessed using
# |      ``chardet``.
# |      
# |      The encoding of the response content is determined based solely on HTTP
# |      headers, following RFC 2616 to the letter. If you can take advantage of
# |      non-HTTP knowledge to make a better guess at the encoding, you should 
# |      set ``r.encoding`` appropriately before accessing this property.
# :





