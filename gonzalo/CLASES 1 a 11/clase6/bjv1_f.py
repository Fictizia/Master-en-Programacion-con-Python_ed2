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


def repartir_carta():
    """
    Reparte una carta y la quita del mazo (al jugador o a la banca)
    """
    # dar carta
    carta = random.choice(baraja)
    # quitar carta de la baraja
    baraja.remove(carta)
    return carta


def mostrar_puntuacion_jugador(num_puntos_jugador):
    """
    Imprime la puntuación (del jugador y de la banca)
    """
    # mostrar puntuacion
    print(" Tu puntuación es: ", num_puntos_jugador)


def primer_reparto_cartas():
    puntos_jugador = repartir_carta()
    puntos_banca = repartir_carta()
    mostrar_puntuacion_jugador(puntos_jugador)
    return puntos_banca, puntos_jugador


def quieres_carta():
    """
    Vuelve a preguntar si el jugador quiere otra carta
    """
    otra_carta = input(" ¿Quieres otra carta ?")
    if otra_carta.upper() == 'S':
        return True
    else:
        return False


def evaluar_si_blackjack(total_puntos_jugador, total_puntos_banca):
    """
    Evalúa si ya ha llegado o superado la puntuación 21 (jugador o banca)
    """
    if total_puntos_jugador == 21 and total_puntos_banca == 21:
        print(" Tú y la Banca tenéis puntuación 21. Gana la Banca ")
        return True
    elif total_puntos_jugador > 21 and total_puntos_banca < 21:
        print(" La puntuación de la Banca es: ", total_puntos_banca)
        print(" Tu puntuación es: ", total_puntos_jugador)
        print(" Ha ganado la Banca ")
        return True
    elif total_puntos_jugador < 21 and total_puntos_banca > 21:
        print(" La puntuación de la Banca es: ", total_puntos_banca)
        print(" Tu puntuación es: ", total_puntos_jugador)
        print(" Has GANADO !!! ")
        return True
    elif total_puntos_jugador > 21 and total_puntos_banca > 21:
        print(" La puntuación de la Banca es: ", total_puntos_banca)
        print(" Tu puntuación es: ", total_puntos_jugador)
        print(" FIN de JUEGO - Nadie gana ")
        return True
    else:
        if total_puntos_jugador == 21:
            print(" Tu puntuación es: ", total_puntos_jugador)
            print(" La puntuación de la Banca es: ", total_puntos_banca)            
            print(" Has GANADO!!! ")
            return True
        if total_puntos_banca == 21:
            print(" Tu puntuación es: ", total_puntos_jugador)            
            print(" La puntuación de la Banca es: ",total_puntos_banca)
            print(" Ha ganado la Banca ")
            return True
        else:
            return False

def quien_esta_mas_cerca_blackjack(total_puntos_jugador, total_puntos_banca):
    """
    Evalúa cuál de los dos está más cerca de 21 (jugador o banca)
    """
    if total_puntos_banca > 21:
        print(" La puntuación de la banca es: ", total_puntos_banca)
        print(" Tu puntuación es: ", total_puntos_jugador)
        print(" Has GANADO!!! ")
    else:
        if total_puntos_banca < total_puntos_jugador:
            print(" La puntuación de la banca es: ", total_puntos_banca)
            print(" Tu puntuación es: ", total_puntos_jugador)
            print(" Has GANADO!!! ")
        else:
            print(" La puntuación de la Banca es: ", total_puntos_banca)
            print(" Tu puntuación es: ", total_puntos_jugador)
            print(" Ha ganado la Banca ")


def sucesivos_repartos_cartas(total_puntos_jugador, total_puntos_banca):
    """
    Va acumulando puntos (banca y jugador) mientras el jugador pide carta
    Llama a la función q evalúa si alguno de los dos llega a 21 o lo supera
    """
    while quieres_carta():
        puntos_jugador = repartir_carta()
        puntos_banca = repartir_carta()
        #
        total_puntos_jugador = puntos_jugador + total_puntos_jugador
        total_puntos_banca   = puntos_banca   + total_puntos_banca
        #
        mostrar_puntuacion_jugador(total_puntos_jugador)
        if evaluar_si_blackjack(total_puntos_jugador, total_puntos_banca):
            ya_hay_blackjack = True
            break
        else:
            ya_hay_blackjack = False
    #
    if ya_hay_blackjack == False:
        while total_puntos_banca < 15:
            puntos_banca = repartir_carta()
            total_puntos_banca  = puntos_banca + total_puntos_banca
            
        quien_esta_mas_cerca_blackjack(total_puntos_jugador, total_puntos_banca)



# =============================================================================

print("                                     ")
print("                                     ")
print("#  ################################ #")
print("#  -------------------------------  #")
print("#  EMPIEZA el juego del BLACK JACK  #")
print("#  -------------------------------  #")
print("#  ################################ #")
print("                                     ")
print("                                     ")


# PRIMER  reparto de cartas
puntuacion_banca, puntuacion_jugador = primer_reparto_cartas()

# SEGUIR  jugando
sucesivos_repartos_cartas(puntuacion_banca, puntuacion_jugador)

