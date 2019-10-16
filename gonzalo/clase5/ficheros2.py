import csv

with open('./ejemplo2.csv', 'a') as file:
    file.writelines('hola, mundo')

my_class = dict()

with open('./ejemplo2.csv', 'r') as csv_file:
    formato_csv = csv.reader(csv_file, delimiter = ',')
    for row in formato_csv:
        my_class.update({row[0]: row[1]})

print(my_class)
