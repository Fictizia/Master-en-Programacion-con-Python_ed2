class Jugador:
    # def __init__(self, mascota):
    #     self.mascota = mascota

    def elegir_mascota(self, opciones):
        id_mascota = int(input('Indica el número de la mascota que eliges: '))
        mascota = opciones[id_mascota]
        print(f'Has elegido a {mascota.nombre}')

        return mascota
