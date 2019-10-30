
# -- VIEW -------------------------------------
# ---------------------------------------------
class CocheView(object):
    def __init__(self, coche_controller):
        self.coche_controller = coche_controller

    def elegir_coche(self):
        selection = int(input('Elije un coche: 1, 2, 3 ó 4 >  '))
        return self.coche_controller.choose(selection)



# -- CONTROLLER -----------------------------------------------------
# -------------------------------------------------------------------
class CocheController(object):
    def __init__(self, coche_primero, coche_segundo, coche_tercero, coche_cuarto):
        self.coche_primero = coche_primero
        self.coche_segundo = coche_segundo
        self.coche_tercero = coche_tercero
        self.coche_cuarto  = coche_cuarto

    def choose(self, coche_elegido):
        return coche_elegido

#        if coche_elegido == 1:
            #self.coche_primero.imprime_coche_uno()
#            return self.coche_primero
#        elif coche_elegido == 2:
#            return self.coche_segundo
#        elif coche_elegido == 3:
#            return self.coche_tercero
#        elif coche_elegido == 4:
#            return self.coche_cuarto



# -- MODEL ---------------------------------
# -------------------------------------------
class Coche():
    def __init__(self, marca, modelo, color):
        self.marca  = marca
        self.modelo = modelo
        self.color  = color

#    def imprime_coche_uno(self):
#        print(' has elegido coche 1')

#    def imprime_coche_dos(self):
#        print(' has elegido coche 2')

    def __repr__(self):
        return f'Coche elegido:  Marca {self.marca}, Modelo {self.modelo}, Color {self.color}'



# -- MAIN -------------------------------
# ---------------------------------------
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

