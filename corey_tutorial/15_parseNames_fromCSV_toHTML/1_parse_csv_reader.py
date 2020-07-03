import csv

html_output = ''
names = []

with open('./csv/patrons.csv', 'r') as data_file:
	csv_reader = csv.reader(data_file)
	### We don't want header and first line of bad data.
	### 헤더와 쓸모없는 데이터 레코드 두줄을 건너 뛴다.
	next(csv_reader)
	next(csv_reader)

	for line in csv_reader:
		if line[0] == 'No Reward':
			continue
		else:
			names.append(f'{line[0]} {line[1]}')

data_file.close()
html_output += f'<p>There are currently {len(names)} public contributors. Thank you!</p>'
html_output += '\n<ul>'

for name in names:
	html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'
print(html_output)





