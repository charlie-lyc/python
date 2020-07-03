import csv


### Corey's Code :
html_output = ''
names = []
with open('./csv/patrons.csv', 'r') as data_file:
	csv_dictReader = csv.DictReader(data_file)
	### We don't want first line of bad data.
	### 헤더는 키로 자동 인식하므로 쓸모없는 데이터 레코드 한줄만 건너뛰면 된다.
	next(csv_dictReader)

	for line in csv_dictReader:
		if line['FirstName'] == 'No Reward':
			continue
		else:
			names.append(f"{line['FirstName']} {line['LastName']}")
data_file.close()
html_output += f'<p>There are currently {len(names)} public contributors. Thank you!</p>'
html_output += '\n<ul>'

for name in names:
	html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'
print(html_output)





### My Code :
# html_output = ''
# names = []
# with open('./csv/patrons.csv', 'r') as data_file:
# 	csv_dictReader = csv.DictReader(data_file)
# 	### We don't want first line of bad data.
# 	### 헤더는 키로 자동 인식하므로 쓸모없는 데이터 레코드 한줄만 건너뛰면 된다.
# 	next(csv_dictReader)
# 	for line in csv_dictReader:
# 		name = ''
# 		for k, v in line.items():
# 			if k == 'FirstName':
# 				if v == 'No Reward':
# 					break
# 				name += f'{v}'
# 			if k == 'LastName':
# 				name += f' {v}'	
# 		if name != '':
# 			names.append(name)
# data_file.close()
# html_output += f'<p>There are currently {len(names)} public contributors. Thank you!</p>'
# html_output += '\n<ul>'

# for name in names:
# 	html_output += f'\n\t<li>{name}</li>'

# html_output += '\n</ul>'
# print(html_output)





