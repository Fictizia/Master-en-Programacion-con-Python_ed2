import csv

with open('./ejemplo.csv', 'w') as file:
    file.writelines('hola mundo')

with open('./ejemplo.csv', 'r') as csv_file:
    formato_csv = csv.reader(csv_file, delimiter = ',')
    for reg in formato_csv:
        print(reg)

