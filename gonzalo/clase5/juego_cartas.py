import random

carta_jugador = 0
carta_banca   = 0

puntuacion_jugador = 0
puntuacion_banca   = 0


def repartir_cartas():
    carta_jugador = random.choice(baraja)
    print(" Tu carta: ", carta_jugador)

    carta_banca = random.choice(baraja)
    print(" Mi carta: ", carta_banca)

def sacar_carta_baraja():
    baraja.remove[carta_jugador]
    baraja.remove[carta_banca]

palo = list(range(1,10))
for diez in range(4):
    palo.append(10)

baraja = palo + palo + palo + palo


# ==============================================

# Primera mano
repartir_cartas()

puntuacion_jugador = puntuacion_jugador + carta_jugador 
puntuacion_banca   = puntuacion_banca   + carta_banca 

print(" Su puntuación hasta ahora es: ", puntuacion_jugador)

sacar_carta_baraja()

# Siguientes manos
jugar = input(" Quieres otra carta: S/N(s/n)")

while jugar.upper() == 'S':
    jugar = input(" Quieres otra carta: S/N(s/n)")

    repartir_cartas()

    puntuacion_jugador = puntuacion_jugador + carta_jugador 
    puntuacion_banca   = puntuacion_banca   + carta_banca 

    print(" Su puntuación hasta ahora es: ", puntuacion_jugador)

    sacar_carta_baraja()

    if puntuacion_jugador == 21:
        print(" Ha ganado usted ")
        break
    elif puntuacion_banca == 21:
        print(" Ha ganado la banca ")
        break

    if puntuacion_jugador >= 21:
        print(" Ha ganado la banca ")
        break

    if puntuacion_banca >= 21:
        print(" Ha ganado usted ")
        break

# El jugador ha dicho que 'N', se ha plantado
# sigue la banca????
if jugar == 'N':
    while puntuacion_banca < 15:
        repartir_cartas()
        puntuacion_banca   = puntuacion_banca   + carta_banca 
        sacar_carta_baraja()

if 21 - puntuacion_banca < 21 - puntuacion_jugador:
    print(" Ha ganado la banca ")
else:
    print(" Ha ganado usted ")

