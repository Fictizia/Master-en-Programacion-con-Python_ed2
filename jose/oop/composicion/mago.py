from jose.oop.herencia.humano import Humano

class Mago(object):
    def __init__(self, humano):
        self.humano = humano
        self.estatura = humano.estatura
        self.barba = False
        
    def hacer_magia(self):
        print('hocus pocus')

    def alardear(self):
        print('Yo puedo hacer magia y tu no')

    def beber(self):
        self.humano.beber()

