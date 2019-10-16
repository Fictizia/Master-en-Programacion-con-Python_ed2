# Dado un número entero decir si es primo

# ún número primo solo es divisible entre si mismo y entre 1
    # lo que significa, que no puede ser divisible entre números anteriores a el
        # "ningún número es divisible por un numero superior a este"
# todos los numeros pares menos el 2 no son primos


num = int(input('Introduce un número entero por favor :> '))
es_uno_o_dos = num == 1 or num == 2

if es_uno_o_dos:
    print(f'El número {num} es primo')

if num % 2 != 0 and not es_uno_o_dos:
    es_primo = True
    for numero_precedente in range(3,num,2):
        if num % numero_precedente == 0:
            es_primo = False

    if es_primo:
        print(f'El número {num} es primo')
    else:
        print(f'El número {num} NO es primo')

elif not es_uno_o_dos:
    print(f'El número {num} NO es primo')