numero = input('Dame un número: ')
numero = int(numero)

contador = 2
es_primo = False

while numero > 1 and numero % contador != 0:
    contador += 1

if numero == contador:
    print(f'{numero} es primo')
    es_primo = True
else:
    print(f'{numero} no es primo')

lista_precedentes = list()

if es_primo == True:
    for num_precedente in range(numero):
        lista_precedentes.append(num_precedente)

lista_precedentes_primos = list()


for num in lista_precedentes:

    nuevo_contador = 2

    while num > 1 and num % nuevo_contador != 0:
        nuevo_contador += 1

    if num == nuevo_contador:
        lista_precedentes_primos.append(num)

print(lista_precedentes_primos)
