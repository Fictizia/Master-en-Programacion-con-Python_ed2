from random import randint


class Mascota:
    def __init__(self, ataque, defensa, vida):
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida

    def atacar(self):
        ataque = randint(1, 5)

    def defenderse(self):
        pass

    def derrotado(self):
        if self.vida > 0:
            return False
        else:
            return True
