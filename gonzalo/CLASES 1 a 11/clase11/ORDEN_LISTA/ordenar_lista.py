import random

lista_numeros = list()

for index in range(1, 10, 1):
    lista_numeros.append(random.randint(1,10))

print(f'lista numeros: {lista_numeros}')
lista_numeros.sort()
print(f'lista numeros ordenada: {lista_numeros}')
lista_numeros.reverse()
print(f'lista numeros ordenada reves: {lista_numeros}')

