from jose.oop.composicion.mago import Mago
from jose.oop.composicion.duende import Duende
from jose.oop.composicion.humano import Humano

class Demonio(object):
    def __init__(self, mago, duende):
        self.mago = mago
        self.duende = duende

    def rugir(self):
        print('ROARRRRR')

    def alardear_como_un_mago(self):
        self.mago.alardear()

    def alardear_como_duende(self):
        self.duende.alardear()

    def alardear(self):
        print('los demonios no alardeamos, os comemos')

    def hacer_magia(self):
        self.mago.hacer_magia()

gonzalo = Humano(1.9, False, 'tostada')
hermion = Mago(gonzalo)
duende = Duende('verde')

demon = Demonio(hermion, duende)
demon.rugir()
demon.alardear()
demon.alardear()
demon.alardear()
demon.alardear()
demon.hacer_magia()