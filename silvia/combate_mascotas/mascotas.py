from random import randint


class Mascota:
    def __init__(self, identificador, nombre, ataque, defensa, vida):
        self.identificador = identificador
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida

    def atacar(self):
        dado_ataque = randint(1, 5)
        dado_ataque += self.ataque
        return dado_ataque

    def defenderse(self):
        dado_defensa = randint(1, 5)
        dado_defensa += self.defensa
        return dado_defensa

    def esta_vivo(self):
        if self.vida > 0:
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.identificador} - {self.nombre}. Ataque: {self.ataque}. Defensa: {self.defensa}. Vida: {self.vida}'
