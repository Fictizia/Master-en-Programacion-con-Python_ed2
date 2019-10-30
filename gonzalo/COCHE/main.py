from view       import CocheView
from controller import CocheController
from model      import Coche

# modelo
coche_primero = Coche('Opel', 'Corsa', 'Rojo')
coche_segundo = Coche('Hyundai', 'Getz', 'Plata')
coche_tercero = Coche('Toyota', 'pepe', 'Azul')
coche_cuarto  = Coche('Nissan', 'hh', 'Verde')

#controlador
coche_controller = CocheController(coche_primero, coche_segundo, coche_tercero, coche_cuarto)

#vista
coche_view = CocheView(coche_controller)

def main(coche_view):
    coche_elegido = coche_view.elegir_coche()

    if coche_elegido == 1:
        print(coche_primero)
    elif coche_elegido == 2:
        print(coche_segundo)
    elif coche_elegido == 3:
        print(coche_tercero)
    elif coche_elegido == 4:
        print(coche_cuarto)
    else:
        print(" No eliges??")

main(coche_view)
