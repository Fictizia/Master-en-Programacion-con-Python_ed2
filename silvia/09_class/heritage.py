class Humano():
    def __init__(self, estatura, barba, piel): # al nombrar clase, primera en mayuscula y resto camel case (Pascal case)
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

############### otro archivo ###############

# from archivo.inicial import Humano

class Mago(Humano): # hereda de Humano
    def hacer_magia(self):
        print('hocus pocus')

    def alardear(self):
        print('Yo puedo hacer magia y tú no') # machaca el anterior método alardear

harry = Mago(1.5, False, 'blanca')
harry.alardear()
harry.beber()
harry.hacer_magia()

alberto = Humano(1.8, True, 'blanca')
# alberto.hacer_magia() # AttributeError: 'Humano' object has no attribute 'hacer_magia'


