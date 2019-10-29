class Automovil(object):
    def __init__(self, ruedas, motor, combustible):
        self.ruedas = ruedas
        self.motor = motor
        self.combustible = combustible

    def acelerar(self):
        print('brum brum, bruuuuuuuum')
        
    def frenar(self):
        print('igggggggg')

automovil = Automovil(8,'16v','diesel')
automovil.acelerar()

# Herencia

class Coche(Automovil):
    pass

coche = Coche(4, '8v','gasolina')
coche.acelerar()

# Composicion

class Moto(object):
    def __init__(self, automovil):
        self.ruedas = automovil.ruedas
        self.motor = automovil.motor
        self.combustible = automovil.combustible
        self.manillar = 'manillar'
        self.automovil = automovil

    def acelerar(self):
        return self.automovil.acelerar()

    def frenar(self):
        return self.automovil.frenar()

automovil_moto = Automovil(2,'1v','electrica')
moto = Moto(automovil_moto)
moto.acelerar()