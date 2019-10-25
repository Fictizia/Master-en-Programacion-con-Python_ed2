from items import (pera, manzana, platano, coca_cola,
                    fanta, sandwich)

slots_maquina = [pera, manzana, platano, coca_cola, fanta,
                 sandwich]

class NoQuedan(Exception):
    pass

class NoHaySaldo(Exception):
    pass

def seleccionar_item():
    imprimir_posibilidades()
    indice_seleccion = int(input('Introduce el número correspondiente al item deseado> '))
    return indice_seleccion

def imprimir_posibilidades():
    for index, item in enumerate(slots_maquina):
        print(f'{index} .-> {item}')

def comprobar_si_existe(item):
    if item.cantidad >0:
        return True
    raise NoQuedan

def comprobar_si_hay_saldo(saldo_tarjeta, item):
    if item.precio > saldo_tarjeta:
        raise NoHaySaldo
    
def entregar(item):
    # restar cantidad del item
    # restar pasta tarjeta
    # imprimir que aproveche
    # volver a empezar
    pass



saldo_tarjeta = int(input('Introduce el saldo tramposillo .... '))

def comienzo():
    item = seleccionar_item()
    try:
        comprobar_si_existe(item)
    except NoQuedan:
        print('No quedan, elige otra cosa')
        comienzo()
    try:
        comprobar_si_hay_saldo(tarjeta, item)
    except NoHaySaldo:
        print('No tienes saldo para eso')
        comienzo()
