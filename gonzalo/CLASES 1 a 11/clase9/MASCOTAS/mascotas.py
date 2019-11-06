from random import randint

class Mascotas():

    def __init__(self, nombre, ataque, defensa, vida):
        self.nombre   = nombre
        self.ataque   = ataque
        self.defensa  = defensa
        self.vida     = vida

    def __repr__(self):
        return f' ** => Mascota: {self.nombre.upper()} **  Ataque: {self.ataque} / Defensa: {self.defensa} / Vida: {self.defensa}'


mascota1 = Mascotas('Rusky', randint(1,10), randint(1,10), randint(1,10))

mascota2 = Mascotas('Lusky', randint(1,10), randint(1,10), randint(1,10))

mascota3 = Mascotas('Tuski', randint(1,10), randint(1,10), randint(1,10))

mascota4 = Mascotas('Pusky', randint(1,10), randint(1,10), randint(1,10))

mascota5 = Mascotas('Ansky', randint(1,10), randint(1,10), randint(1,10))



