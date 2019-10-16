# Pasar de decimal a romano
# Primero solo unidades

numero_introducido = input('Introduce un número: ')


def centenas(numero):
    numero = numero_introducido[-3]
    numero = int(numero)
    if numero <= 3:
        result = 'C' * numero
    elif numero == 4:
        result = 'CD'
    elif numero >= 5 and numero < 9:
        resta = numero - 5
        d_detras_c = 'D' * resta
        result = 'C' + d_detras_c
    else:
        result ='CM'
    
    return result


def decenas(numero):
    numero = numero_introducido[-2]
    numero = int(numero)
    if numero <= 3:
        result = 'X' * numero
    elif numero == 4:
        result = 'XL'
    elif numero >= 5 and numero < 9:
        resta = numero - 5
        x_detras_l = 'X' * resta
        result = 'L' + x_detras_l
    else:
        result = 'XC'
    
    return result


def unidades(numero):
    numero = numero_introducido[-1]
    numero = int(numero)
    if numero <= 3:
        result = 'I' * numero
    elif numero == 4:
        result = 'IV'
    elif numero >= 5 and numero < 9:
        resta = numero - 5
        i_detras_v = 'I' * resta
        result = 'V' + i_detras_v
    else:
        result ='IX'
    
    return result


print(centenas(numero_introducido) + decenas(numero_introducido) + unidades(numero_introducido))
