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


