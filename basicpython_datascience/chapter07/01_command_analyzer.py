import csv

with open('command_data.csv', 'r') as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(csv_read)
    next(csv_read)
    command_counter = {}
    for line in list(csv_read):
        if line[1] not in command_counter.keys():
            command_counter[line[1]] = 1
        else:
            command_counter[line[1]] += 1
csvfile.close()

counter_list = []
for k, v in command_counter.items():
    counter_list.append([k, v])
sorted_counter_list = sorted(counter_list, key=lambda x: x[1], reverse=True)
for counter in sorted_counter_list:
    print(f'{counter[0]} : {counter[1]}')
