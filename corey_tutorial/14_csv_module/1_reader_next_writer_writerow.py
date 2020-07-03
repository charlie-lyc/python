import csv


### Corey's Code:
with open('./csv/names.csv', 'r') as csv_file:
	### delimiter = ',' ### : Default
    ### csv파일을 읽어 들이기 전에 먼저 열어서 반드시 확인할 것. 
    ### '-', '|', '\t', ' ' 등일 수도 있다.
	csv_reader = csv.reader(csv_file, delimiter=',')
	### Skip Header(Field Names) ###
	# next(csv_reader)

	with open('./csv/new_names.csv', 'w') as new_file:
		### delimiter = ',' ### : Default
		csv_writer = csv.writer(new_file, delimiter='\t')

		for line in csv_reader:
			csv_writer.writerow(line)
new_file.close()
csv_file.close()


with open('./csv/new_names.csv', 'r') as csv_file:
	# csv_reader = csv.reader(csv_file) # wrong coding : delimiter=',' default
	csv_reader = csv.reader(csv_file, delimiter='\t')

	for line in csv_reader:
		print(line)
csv_file.close()


### My Code: 
# with open('./csv/names.csv', 'r') as rf:
# 	with open('./csv/new_names.csv', 'w') as wf:
# 		# print(dir(csv.reader))
# 		# print(dir(csv.writer))
# 		# print()
# 		# print(dir(csv.reader(rf))) # __iter__
# 		# print(dir(csv.writer(wf))) # __iter__
# 		# print()
# 		# print(help(csv.reader(rf)))
# 		# print(help(csv.writer(wf)))
# 		# print()

# 		for row in csv.reader(rf, delimiter=','):
# 			# print(row)
# 			first_name, last_name, email = row
# 			# print(first_name, last_name, email)
# 			first_name = first_name.strip()
# 			last_name = last_name.strip()
# 			email = email.strip()
# 			# print('{}, {}, {}'.format(first_name, last_name, email))
# 			new_row = '{}, {}, {}'.format(first_name, last_name, email)
# 			new_row = new_row.split(', ')
# 			csv.writer(wf, delimiter='|').writerow(new_row)

# 		# print(csv.writer(wf).writerow)
# 		# print(dir(csv.writer(wf).writerow))
# 		# print(help(csv.writer(wf).writerow))
# 		# # writerow(iterable)
# 		# print(help(csv.writer(wf).writerows))
# 		# # writerows(iterable of iterables)
# wf.close()
# rf.close()



