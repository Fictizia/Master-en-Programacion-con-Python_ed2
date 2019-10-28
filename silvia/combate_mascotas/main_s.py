import random
from random import randint

from jugador import Jugador
from mascotas import Mascota

def accion(atacante, defensor):
    print(f'{atacante.nombre} golpea a {defensor.nombre}')
    valor_ataque = atacante.atacar()
    valor_defensa = defensor.defenderse()

    resultado = valor_ataque - valor_defensa
    resultado = max(resultado, 0)

    print(f'{defensor.nombre} pierde {resultado} puntos de vida')

    defensor.vida -= resultado


def main():

    albert = Mascota(1, 'Albert Rivera', 8, 7, 10)
    pablo_i = Mascota(2, 'Pablo Iglesias', 7, 9, 10)
    pedro = Mascota(3, 'Pedro Sánchez', 6, 4, 10)
    pablo_c = Mascota(4, 'Pablo Casado', 8, 3, 10)
    santiago = Mascota(5, 'Santiago Abascal', 9, 5, 10)

    mascotas_maquina = {'1': albert,
                        '2': pablo_i,
                        '3': pedro,
                        '4': pablo_c,
                        '5': santiago, }

    maquina = Jugador(mascotas_maquina)

    maquina.elegir_mascota_random()
    print(
        f'Ha aparecido {maquina.luchador.nombre} y te va a atacar')

    quim = Mascota(6, 'Quim Torra', 8, 5, 10)
    oriol = Mascota(7, 'Oriol Junqueras', 4, 6, 10)
    gabriel = Mascota(8, 'Gabriel Rufián', 5, 3, 10)
    jordi = Mascota(9, 'Jordi Sánchez', 3, 5, 10)
    carles = Mascota(10, 'Carles Puigdemont', 2, 4, 10)

    mascotas_jugador = {'6': quim,
                        '7': oriol,
                        '8': gabriel,
                        '9': jordi,
                        '10': carles,
                        }

    jugador = Jugador(mascotas_jugador)

    try:
        jugador.elegir_mascota_por_teclado()
    except:
        print('Has seleccionado un indice de mascota incorrecto')

    turno = 0

    while (maquina.luchador.esta_vivo() and jugador.luchador.esta_vivo()):

        if (turno % 2 == 0):
            accion(maquina.luchador, jugador.luchador)
        else:
            accion(jugador.luchador, maquina.luchador)

        turno += 1

    if (maquina.luchador.vida > 0):
        print('Ha ganado la maquina')
    else:
        print('Ha ganado el jugador')


main()
