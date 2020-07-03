import csv


with open('./csv/names.csv', 'r') as csv_file:
	csv_dictReader = csv.DictReader(csv_file)
	### DictReader()을 실행하면 파일의 첫 번째 줄은 자동으로 헤더(필드이름)로 인식하게 된다.
	### 이것은 역으로 얘기하면 DictReader()을 실행하기 위해 파일 첫째줄에 헤더(필드이름)이 반드시 있어야 한다.
	### 헤더(필드이름)을 건너 뛰기위해 next()사용할 필요없다. 오히려 첫번째 데이터를 건너뛰게 된다.
	# next(csv_reader)

	# for line in csv_dictReader:
	# 	for k, v in line.items():
	# 		print(k,':', v)
	# 	print()

	with open('./csv/dict_names.csv', 'w') as new_file:
		### DictWiter() 실행을 위해 반드시 'fieldnames'(header)가 있어야 한다. 없으면 TypeError 발생.
		### 'fieldnames'(header)은 순서대로 넣기 위해 list형으로 입력한다.
		### arguments로 입력시에는 반드시 맵핑되는 순서를 지켜야한다. 그렇지 않고 'key=value' 방식일 경우에는 상관없다.
			
		fieldnames=['first_name', 'last_name', 'email']
		csv_dictWriter = csv.DictWriter(new_file, fieldnames, delimiter='\t')
		# csv_dictWriter = csv.DictWriter(new_file, delimiter='\t', fieldnames=fieldnames)
		
		### writeheader()를 실행하지 않으면 'fieldnames'(header) 없는 파일이 생성된다.
		csv_dictWriter.writeheader()

		for line in csv_dictReader:
			del line['email']
			csv_dictWriter.writerow(line)
new_file.close()
csv_file.close()


