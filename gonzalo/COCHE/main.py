from view.coche import CocheView
from controller.coche import CocheController
from model.coche import Coche

coche = Coche()
coche_controller = CocheController(coche)
coche_view = CocheView(coche_controller)

def main(coche_view):
    coche_view.show_coche()


main(coche_view)