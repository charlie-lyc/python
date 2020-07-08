# split() : 공백이 몇칸인지는 관계없이 주어진 문자열을 공백 기준으로 분리해서 리스트를 생성
# split(' ') : 공백 한칸을 기준으로 문자열을 분리
items = 'zero one two three'.split()
print(items)
print()

example1 = 'python,jquery,javascript'
print(example1.split(','))
print()

# Unpack
a, b, c = example1.split(',')
print(a, b, c)
print()

# Unpack
example2 = 'cs50.gachon.edu'
subdomain, domain, tld = example2.split('.')
print(subdomain, domain, tld)
