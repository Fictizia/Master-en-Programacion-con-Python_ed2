# Dado un numero entero decir si es primo. 
#Condiciones para que un numero primo se de, un numero primo solo es divisible entre si mismo y entre 1
    #lo que significa, que no puede ser divisible entre numero anteriores a el, ningun numero es divisible por un numero superior a este
# todos lo n


num = int(input('Introduce un numero entero por favor >'))
es_uno_o_dos = num ==1 or num == 2

if es_uno_o_dos:
    print(f'el numero {num} es primo')

if num % 2 != 0 and not es_uno_o_dos:
    es_primo = True

    for  numero_precedent in range(3, num,2):
        if num % numero_precedent == 0
            es_primo = False



    if es_primo and num !=1 and num!= 2:
        print(f'el numero {num} es primo')
    else:
        print(f'El numero {num} NO es primo')
elif and not es_uno_o_dos:
    print(f'El numero {num} NO es primo')
