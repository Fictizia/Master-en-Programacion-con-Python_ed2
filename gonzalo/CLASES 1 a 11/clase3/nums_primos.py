
Es_Primo    = 'S'

numeros_primos_anteriores = list()
numeros_es_divisible = list()

numero_entrada = input('ESCRIBE un numero entero  $>>: ')

# Que no dé a "enter" sin poner un número
if len(numero_entrada) == 0:
  print("ERROR: DEBE introducir un valor NO vacío y NUMERICO")

else:

    numero_entrada = int(numero_entrada)

    if numero_entrada > 1:
        #numero_entrada == numero_entrada
        print(numero_entrada)

        #el único NUMERO PRIMO y PAR es el 2
        if numero_entrada%2 == 0:   # es un NUMERO PAR
            if numero_entrada == 2:
                print('El número introducido SI es PRIMO')
            else:
                print('El número introducido NO es PRIMO (es Par y no es 2)')

        else:  # es un NUMERO IMPAR

            # si el numero introducido es impar: solo miramos los impares, ya que el único PAR y PRIMO es el 2.
            cont = 0
            for num_rango in range(3,numero_entrada+1,2):
                if numero_entrada%num_rango == 0:
                    cont += 1
                    if numero_entrada == num_rango  and cont == 1:    # si es PRIMO
                        Es_Primo = 'S'
                        print("el número introducido SI es PRIMO")
                    if numero_entrada == num_rango  and cont != 1:    # no es PRIMO
                        Es_Primo = 'N'
                    if numero_entrada != num_rango:
                        Es_Primo = 'N'
                        num_divisible_por = num_rango
                        numeros_es_divisible.append(num_divisible_por)


        # Obtener los PRIMOS anteriores al numero introducido: 
        numero_leido = 1
        while numero_leido < numero_entrada:
            Cuenta_Num_Divisibles = 0

            for num_rango in range(3, numero_leido+1, 2):
                if numero_leido%num_rango == 0:
                    Cuenta_Num_Divisibles += 1

                    if numero_leido != num_rango and num_rango != 1: # NO es PRIMO
                        break
                    if numero_leido == num_rango and Cuenta_Num_Divisibles != 1:  # no es PRIMO
                        break
                    if numero_leido == num_rango and Cuenta_Num_Divisibles == 1:  # SI es PRIMO
                        numeros_primos_anteriores.append(num_rango)
            #
            numero_leido += 2

        if Es_Primo == 'N':
            numeros_es_divisible.append(1)
            print("El número introducido NO es PRIMO, ya que es divisible por: ", numeros_es_divisible)

        numeros_primos_anteriores.append(1)
        print("Y los números primos anteriores son: ", numeros_primos_anteriores)

    else:   # si numero_entrada es <= 1
        print(numero_entrada)
        print('ERROR: el numero ha de ser mayor que 1')


