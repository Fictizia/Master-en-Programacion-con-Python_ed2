import csv

with open('./example.csv', 'a') as file:
    file.write('c, d\n')

my_class = dict()

with open('./example.csv', 'r') as csv_file:
    format_csv = csv.reader(csv_file, delimiter=',')

    for row in format_csv:
        my_class.update({row[0]: row[1]})

print(my_class)