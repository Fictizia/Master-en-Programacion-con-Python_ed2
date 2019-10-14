# I = 1, V = 5, X = 1O, L = 50, C = 100

#separamos por unidades centenas y decenas
#Creamos un directorio por cada unidad

#Primero hacemos un len para saber cuantos cifras tiene
# una vez hecho eso lo que tenemos que hacer es un bucle for para recorrerlo una vez
# lo hemos recorrido le damos un valor 

numero_introducido = input('introduce tu numero')
numero = int(numero)

def decenas(numero):
    numero = numero[-2]
    numero = int(numero)
    





def unidades(numero):
    numero =[ -1]
    int(numero)
    if numero <= 3:
        print('I' * numero)
    if numero == 4:
        print('IV')
    if numero >= 5 and numero < 9:
        resta = numero - 5
        i_detras_v = 'I' * resta 
        print('V' + i_detras_v)
    else:
        print('IX')


# unidad[1 = I, 2 = II, 3 = III, 4 = IV, 5 = V, 6 = VI, 7 = VII, 8 = VIII, 9]