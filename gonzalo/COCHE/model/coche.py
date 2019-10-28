class Coche():
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def elegir_coche(self):
        selection = int(input('Elije un coche: 1 ó 2 >  '))
        self.coche_controller.choose(selection)

    def imprime_coche_uno(self):
        print(' has elegido coche 1')
        
    def imprime_coche_dos(self):
        print(' has elegido coche 2')
    
