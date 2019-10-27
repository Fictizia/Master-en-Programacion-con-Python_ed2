import random


class Jugador:
    def __init__(self, mascotas):
        self.mascotas = mascotas
        self.luchador = None

    def elegir_mascota_por_teclado(self):
        for mascota in self.mascotas:
            print(self.mascotas[mascota])
        id_mascota = input('Indica el número de la mascota que eliges: ')
        self.luchador = self.mascotas[id_mascota]
        print(f'Has elegido a {self.luchador}')

    def elegir_mascota_random(self):
        clave = random.choice(list(self.mascotas))
        self.luchador = self.mascotas[clave]

        # def anadir_mascota(self, mascota, clave_mascota):
        #     self.mascotas.append(clave_mascota, mascota)
