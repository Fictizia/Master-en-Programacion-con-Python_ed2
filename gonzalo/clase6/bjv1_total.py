import random

def crear_baraja():
    """
    Cargar un palo con 10 cartas del 1 al 10, y con las cuatro últimas q valen 10 (baraja francesa)
    """
palo = list(range(1,10))
for diez in range(4):
    palo.append(10)
#
baraja = palo + palo + palo + palo

def dar_carta():
    """
    Reparte una carta y la quita del mazo (al jugador o a la banca)
    """
    # dar carta
    carta = random.choice(baraja)
    # quitar carta de la baraja
    baraja.remove(carta)
    return carta

def primer_reparto():
    puntos_jugador = dar_carta()
    puntos_banca   = dar_carta()
    mostrar_puntuacion_jugador(puntos_jugador)
    return puntos_banca, puntos_jugador

def turno_banca():

            puntos_banca = repartir_carta()
            total_puntos_banca  = puntos_banca + total_puntos_banca

def siguientes_repartos(puntos_jugador, puntos_banca):
    if puntos_jugador < 21 and puntos_banca < 21:
        respta = quieres_carta()
        if respta == 'S':
            puntos_jugador = dar_carta()
            puntos_banca   = dar_carta()
            mostrar_puntuacion_jugador(puntos_jugador)
        else:
            turno_banca()
            evaluar_puntuacion()
            siguientes_repartos()
            return
    else:
        evaluar_puntuacion()
        return

