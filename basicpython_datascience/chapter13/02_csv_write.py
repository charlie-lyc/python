# CSV 파일 쓰기

line_counter = 0
data_header = None
USA_customer_list = []

with open('customers.csv', 'r') as csvrf:
    while True:
        data = csvrf.readline()
        if not data:
            break
        if line_counter == 0:
            data_header = data.split(',')
        else:
            if data.split(',')[10].upper() == 'USA':
                USA_customer_list.append(data.split(','))
        line_counter += 1

print('Number of USA customers : ', len(USA_customer_list))
print()

print('Header : ', end='')
for header in data_header:
    print(header.replace('\n', ''), end='|')
print()

for i in range(len(USA_customer_list)):
    print(f'Data {i} : ', end='')
    for info in USA_customer_list[i]:
        print(info.replace('\n', ''), end=' | ')
    print()

with open('USA_customers.csv', 'w') as csvwf:
    csvwf.write(','.join(data_header))
    for customer in USA_customer_list:
        csvwf.write(','.join(customer))

csvrf.close()
csvwf.close()


# My Coding
with open('customers.csv', 'r') as csvrf1:
    with open('my_USA_customers.csv', 'w') as csvwf1:
        data = csvrf1.readline()
        csvwf1.write(data)
        while True:
            data = csvrf1.readline()
            if not data:
                break
            elif data.split(',')[10].upper() == 'USA':
                csvwf1.write(data)
csvrf1.close()
csvwf1.close()











