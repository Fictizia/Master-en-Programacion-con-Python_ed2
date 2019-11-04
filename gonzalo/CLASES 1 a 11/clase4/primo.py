numeros_primos_anteriores = list()


def validar_input():
    if len(numero_entrada) == 0:
        return False
    if len(numero_entrada) != 0:
        return True


def ver_primos_par():
    if numero_entrada % 2 == 0:
        if numero_entrada == 2:
            print('El número introducido SI es PRIMO')
        else:
            print('El número introducido NO es PRIMO (es Par y no es 2)')


def ver_primos_impar():
    if numero_entrada % 2 != 0:
        for numeros in range(3, numero_entrada + 2, 2):
            if numero_entrada % numeros == 0:
                if numero_entrada == numeros:
                    print("El número",numero_entrada,"SI es PRIMO")
                if numero_entrada != numeros:
                    print("El número",numero_entrada,"NO es PRIMO ")
                    break


def ver_primos_anteriores():
    numero_anterior_a_numentrada = 1

    while numero_anterior_a_numentrada < numero_entrada:
        for numero in range(3, numero_anterior_a_numentrada + 3, 2):
            if numero_anterior_a_numentrada % numero == 0:
                if numero_anterior_a_numentrada == numero:
                    numeros_primos_anteriores.append(numero_anterior_a_numentrada)
                if numero_anterior_a_numentrada != numero:
                    break

        numero_anterior_a_numentrada += 2
    #
    numeros_primos_anteriores.append(1)
    if numero_entrada > 2:
        numeros_primos_anteriores.append(2)

    print("Y los números primos anteriores son: ", numeros_primos_anteriores)


# ==================================== [ Cuerpo  Principal ] =========================================

numero_entrada = input('ESCRIBE un número entero  $>>: ')

if validar_input() is True:
    numero_entrada = int(numero_entrada)

    if numero_entrada > 1:
        print(numero_entrada)

        # -> Número introducido es PAR
        ver_primos_par()

        # -> Número introducido es IMPAR
        ver_primos_impar()

        # -> Obtener los PRIMOS anteriores al numero introducido:
        ver_primos_anteriores()

    else:
        print(numero_entrada)
        print('ERROR: el número ha de ser mayor que 1')

else:
    print("ERROR: DEBE introducir un valor NO vacío y NUMERICO")
