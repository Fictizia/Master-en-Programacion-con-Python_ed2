numero_entrada = input('ESCRIBE un numero entero de hasta tres cifras $>>: ')

def unidades(numero):
    
    numero= [-1]
    numero=int(numero)
    
    if int(numero_entrada) <= 3:
        print(int(numero_entrada)*'I')
    if int(numero_entrada) == 4:
        print('IV')
    if int(numero_entrada) >= 5 and int(numero_entrada) < 9 :
        resta = int(numero_entrada) - 5
        i_detras_v = 'I' * resta
        print('V'+i_detras_v)
    else:
        print('IX')


if len(numero_entrada) == 3:
    pass

elif len(numero_entrada) == 2:
    pass

elif len(numero_entrada) == 1:
   unidades()





