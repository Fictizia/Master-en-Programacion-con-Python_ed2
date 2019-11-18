from funciones import *


def main():
    imprimir_amistad()

    opcion = inicio_amistad()

    usuario = validar_usuario(opcion)
    if opcion == 3:
        return
    if not usuario:
        return

    mostrar_solicitudes_amistad(usuario)

    opcion = mostrar_opciones_disponibles()
    opcion = tratar_opciones(opcion, usuario)
    if opcion == 2:
        main()
    elif opcion == 3:
        return


#
main()
