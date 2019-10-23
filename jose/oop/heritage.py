class Humano(object):
    def __init__(self, estatura, barba, piel):
        self.estatura = estatura
        self.barba = barba
        self.piel = piel
    
    def beber(self):
        print('Glo, glo, glo')

    def alardear(self):
        print(f'mido {self.estatura} y me encanta')

# silvia = Humano(1.7, False, 'blanca')
# silvia.alardear()
# print(silvia.piel)

########## otro archivo ##########

# from archivo.inicial import Humano

class Mago(Humano):
    def hacer_magia(self):
        print('hocus pocus')

    def alardear(self):
        print('Yo puedo hacer magia y tu no')

harry = Mago(1.5, False, 'blanca')
alberto = Humano(1.8, True, 'blanca')

#polimorfismo simplon
# IMAGINEMOS QUE ES OTRO ARCHIVO, PARA VERLO TODO JUNTO
from random import randint

randomize_object = [alberto, harry]
for _ in range(1, 10):
    index = randint(0,1)
    winner = randomize_object[index]
    winner.alardear()



