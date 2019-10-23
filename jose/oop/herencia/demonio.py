from jose.oop.herencia.mago import Mago
from jose.oop.herencia.duende import Duende

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