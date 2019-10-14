import csv

with open('./example.csv', 'w') as file: # with se asegura de que se ejecuta algo en el bloque al entrar y otra cosa al salir. Crea el archivo example, si no existe. Lo guarda en una variable file. rw = read, write. Si no se pone nada, entiende que es write
    file.writelines('greet, hello world')

my_class = dict()

with open('./example.csv', 'r') as csv_file:
    format_csv = csv.reader(csv_file, delimiter = ', ')

    for row in format_csv:
        my_class.update = {row[0]: row[1]}

print(my_class)