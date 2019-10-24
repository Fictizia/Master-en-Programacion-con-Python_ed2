class Jugador:
    def __init__(self, mascota):
        self.mascota = mascota

    def elegir_mascota(self, id_mascota):
        mascota = int(input('Indica el número de la mascota que eliges: '))
        return mascota
