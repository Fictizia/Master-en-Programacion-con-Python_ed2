from clase_productos import (pera, cacahuetes, chuches, cerveza, cafe, consome, fanta, sandwich)

slots_maquina = [pera, cacahuetes, chuches, cerveza, cafe, consome, fanta, sandwich]


def imprimir_posibilidades():
    print(" ================= Productos disponibles ================ ")
    print("                                                          ")
    #
    for index, producto in enumerate(slots_maquina):
        print(f'{index} .-> {producto}')
    #
    print("                                                          ")
    print(" ======================================================== ")

def introducir_saldo():
    saldo = int(input(" Introduce tu saldo: "))
    if saldo == 0:
        print(' El saldo ha de ser mayor que 0€')
        introducir_saldo()
    return saldo

def seleccionar_producto():
    imprimir_posibilidades()
    indice_seleccion = int(input(" Introduce el número del producto: "))
    producto = slots_maquina[indice_seleccion]
    return producto

def comprobar_si_queda_producto(producto):
    if producto.cantidad > 0:
        return True
    return False

def comprobar_saldo_tarjeta(saldo, producto):
    if saldo == 0:
        print(' Se te acabó el saldo. Adióoos!. Puedes empezar de nuevo introduciendo nuevo saldo')
        return 0
    elif saldo < producto.precio:
        #ver_si_saldo_es_menor_q_cualquier_producto
        print(f' No tienes saldo para ese producto. Elige otro o SALIR(Ctrl+C). Puedes empezar de nuevo introduciendo nuevo saldo')
        return 1

def actualizar_saldo_tarjeta(saldo, producto):
    saldo -= producto.precio
    return saldo

def actualizar_unidades_producto(producto):
    producto.cantidad -= 1

def entregar_producto(producto, saldo):
    print(f' Ha elegido {producto.nombre} . Que aproveche. Quedan {producto.cantidad} unidades. Su saldo es {saldo}€.')



# --- PRINCIPAL ---
def usar_maquina(saldo):

    producto = seleccionar_producto()

    if not comprobar_si_queda_producto(producto):
        print(f' No quedan unidades de {producto}. Elije otra opción')

    resul = comprobar_saldo_tarjeta(saldo, producto)
    if resul == 0:
        return
    elif resul == 1:
        usar_maquina(saldo)

    actualizar_unidades_producto(producto)

    saldo = actualizar_saldo_tarjeta(saldo, producto)

    entregar_producto(producto, saldo)

    if saldo == 0:
        print(' Se te acabó el saldo. Adióoos!. Puedes empezar de nuevo introduciendo nuevo saldo')
        return

    usar_maquina(saldo)


# ---------------------------------------------------------------------

saldo = introducir_saldo()

usar_maquina(saldo)

