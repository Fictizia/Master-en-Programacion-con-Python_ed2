class Maquina():

    def __init__(self, nombre, ataque, defensa, vida):
        self.nombre   = nombre
        self.ataque   = ataque
        self.defensa  = defensa
        self.vida     = vida

    def __repr__(self):
        return f' ** => Máquina: {self.nombre.upper()} ** Ataque: {self.ataque} / Defensa: {self.defensa} / Vida: {self.defensa}'


maquina = Maquina('Máquina', 10, 10, 10)

