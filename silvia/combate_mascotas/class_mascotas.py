from random import randint


class Mascota:
    def __init__(self, identificador, nombre, ataque, defensa, vida):
        self.identificador = identificador
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida

    def __repr__(self):
        return f'{self.identificador} - {self.nombre}. Ataque: {self.ataque}. Defensa: {self.defensa}. Vida: {self.vida}'

    def atacar(self):
        ataque = randint(1, 5)
        return ataque

    def defenderse(self):
        defensa = randint(1, 5)
        return defensa

    def esta_vivo(self):
        if self.vida > 0:
            return False
        else:
            return True
