counter = 1
lista = list()

while counter <= 100:
    if counter % 3 == 0 and counter % 2 == 0:
        lista.append(counter)
    counter += 1
    if len(lista) == 10:
        break

print(lista)