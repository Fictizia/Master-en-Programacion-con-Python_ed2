class Car(object):
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __repr__(self):
        return (f'Marca: {self.marca}. Modelo: {self.modelo}. Color: {self.color}')

