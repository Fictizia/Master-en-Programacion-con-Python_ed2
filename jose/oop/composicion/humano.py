class Humano(object):
    def __init__(self, estatura, barba, piel):
        self.estatura = estatura
        self.barba = barba
        self.piel = piel
    
    def beber(self):
        print('Glo, glo, glo')

    def alardear(self):
        print(f'mido {self.estatura} y me encanta')

    def desmayarse(self):
        print(f'Hay Dio mío que está to borroso')


