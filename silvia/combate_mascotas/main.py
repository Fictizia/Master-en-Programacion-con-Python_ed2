import random
from random import randint

from jugador import Jugador
from mascotas import Mascota
from mascotas_jug import mascotas_dict

valor_aleatorio = randint(1, 10)

albert = Mascota(1, 'Albert Rivera', valor_aleatorio, valor_aleatorio, 10)
pablo_i = Mascota(2, 'Pablo Iglesias', 7, 9, 10)
pedro = Mascota(3, 'Pedro Sánchez', 6, 4, 10)
pablo_c = Mascota(4, 'Pablo Casado', 8, 3, 10)
santiago = Mascota(5, 'Santiago Abascal', 9, 5, 10)
quim = Mascota(6, 'Quim Torra', 8, 5, 10)
oriol = Mascota(7, 'Oriol Junqueras', 4, 6, 10)
gabriel = Mascota(8, 'Gabriel Rufián', 5, 3, 10)
jordi = Mascota(9, 'Jordi Sánchez', 3, 5, 10)
carles = Mascota(10, 'Carles Puigdemont', 2, 4, 10)

opciones_maquina = [albert, pablo_i, pedro, pablo_c, santiago]
mascota_maquina = random.choice(opciones_maquina)

maquina = Jugador()

print(mascota_maquina)
print(maquina)

opciones_jugador = [quim, oriol, gabriel, jordi, carles]
jugador = Jugador()
# Falta implementar que el jugador elija la mascota

print(jugador)

# Comienza el combate

print(
    f'Aparece {mascota_maquina.nombre} y te va a atacar.\n===============\nElije tu mascota. ')

for _ in opciones_jugador:
    print(_)

mascota_jugador = jugador.elegir_mascota(
    mascotas_dict)  # OJO: revisar id mascota
print(mascota_jugador)
