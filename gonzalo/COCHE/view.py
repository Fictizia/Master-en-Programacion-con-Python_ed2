class CocheView(object):
    def __init__(self, coche_controller):
        self.coche_controller = coche_controller

    def elegir_coche(self):
        selection = int(input('Elije un coche: 1, 2, 3 ó 4 >  '))
        return self.coche_controller.choose(selection)
