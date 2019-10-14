numero = input('Dame un número: ')
numero = int(numero)

contador = 2

while numero > 1 and numero % contador != 0:
    contador += 1

if contador == numero:
    print(f'{numero} es primo')
else:
    print(f'{numero} no es primo')
