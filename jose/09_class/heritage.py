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
harry.alardear()
harry.beber()
harry.hacer_magia()

alberto = Humano(1.8, True, 'blanca')

