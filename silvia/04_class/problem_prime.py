# Dado un número entero, decir si es primo

# Un número primo sólo es divisible entre sí mismo y entre 1
    # lo que significa que no puede ser divisible por números anteriores a él
    # "ningún número es divisible por un número superior a él"
# Todos los números pares menos el 2 no son primos


num = int(input('Introduce un número entero, por favor :> '))
es_uno_o_dos = num == 1 or num == 2

if es_uno_o_dos:
    print(f'El número {num} es primo')

if num % 2 != 0 and not es_uno_o_dos:
    es_primo = True
    for numero_precedente in range(3, num, 2):
        if num % numero_precedente == 0:
            es_primo = False

    if es_primo:
        print(f'El número {num} es primo')
    else:
        print(f'El número {num} NO es primo')

elif not num != 1 and num != 2:
    print(f'El número {num} NO es primo')
    