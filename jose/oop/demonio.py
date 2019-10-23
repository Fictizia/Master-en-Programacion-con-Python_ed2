from jose.oop.mago import Mago
from jose.oop.duende import Duende

class Demonio(Duende, Mago):
    def rugir(self):
        print('ROARRRRR')

demon = Demonio('rojo')
demon.rugir()
demon.alardear()
demon.alardear()
demon.alardear()
demon.alardear()
demon.hacer_magia()