# pasar de decimal a romano
# primero solo unidades

numero_introducido = input('Introduce un numero del 1 al 9 >: ')

def decenas(numero):
    numero = numero[-2]
    numero = int(numero)

    if numero <= 3:

        print('I' * numero)

    if numero == 4:
        print('IV')

    if numero >= 5 and numero < 9:
        resta = numero - 5
        i_detras_v = 'I' * resta
        print('V'+i_detras_v)
    else:
        print('IX')

def unidades(numero):
    numero = [-1]
    int(numero)

    if numero <= 3:
        print('I' * numero)

    if numero == 4:
        print('IV')

    if numero >= 5 and numero < 9:
        resta = numero - 5
        i_detras_v = 'I' * resta
        print('V'+i_detras_v)
    else:
        print('IX')
    