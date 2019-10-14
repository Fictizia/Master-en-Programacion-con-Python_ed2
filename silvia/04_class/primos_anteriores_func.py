numero = input('Dame un número: ')
numero = int(numero)


def es_primo(cantidad):

    contador = 2
    resultado = False

    while cantidad > 1 and cantidad % contador != 0:
        contador += 1

    if cantidad == contador:
        resultado = True

    return resultado


primo = es_primo(numero)

if primo == True:
    print(f'{numero} es primo')
else:
    print(f'{numero} no es primo')


lista_precedentes = list()

if primo == True:
    for num_precedente in range(numero):
        lista_precedentes.append(num_precedente)

lista_precedentes_primos = list()


for num in lista_precedentes:

    primo_anterior = es_primo(num)

    if primo_anterior == True:
        lista_precedentes_primos.append(num)

print(lista_precedentes_primos)
