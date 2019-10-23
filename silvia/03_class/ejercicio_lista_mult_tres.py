counter = 1
lista = list()

while counter <= 100:
    if counter % 3 == 0:
        lista.append(counter)
    counter += 1

print(lista)