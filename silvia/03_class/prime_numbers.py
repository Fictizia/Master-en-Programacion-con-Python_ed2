numero = input('Dame un número: ')
numero = int(numero)

contador = 2

if numero < 2:
    print(f'{numero} no es primo')
else:
    while contador <= numero:
        if numero == 2:
            print(f'{numero} es primo')
            break
        elif numero % contador == 0:
            print(f'{numero} no es primo')
            break
        else:
            print(f'{numero} es primo')
            break
        contador += 1
