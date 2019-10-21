import random

def imprimir_pantalla_inicio_juego():
    print("                                     ")
    print("                                     ")
    print("#  ################################ #")
    print("#  -------------------------------  #")
    print("#  EMPIEZA el juego del BLACK JACK  #")
    print("#  -------------------------------  #")
    print("#  ################################ #")
    print("                                     ")
    print("                                     ")

def crear_baraja():
    """
    Cargar un palo con 10 cartas del 1 al 10, y con las cuatro últimas q valen 10 (baraja francesa)
    """
    palo = list(range(1,10))
    for _ in range(4):
        palo.append(10)
    #
    baraja = palo + palo + palo + palo

    return baraja

def evaluar_si_blackjack(player, banca):
    """
    Evalúa si ya ha llegado o superado la puntuación 21 (jugador o banca)
    """
    blackjack_conseguido = False

    if player == 21 and banca == 21:
        print(" Tú y la Banca tenéis puntuación 21. Gana la Banca ")
        blackjack_conseguido = True
    elif player > 21 and banca < 21:
        print(" La puntuación de la Banca es: ", banca)
        print(" Tu puntuación es: ", player)
        print(" Ha ganado la Banca ")
        blackjack_conseguido = True
    elif player < 21 and banca > 21:
        print(" La puntuación de la Banca es: ", banca)
        print(" Tu puntuación es: ", player)
        print(" Has GANADO !!! ")
        blackjack_conseguido = True
    elif player > 21 and banca > 21:
        print(" La puntuación de la Banca es: ", banca)
        print(" Tu puntuación es: ", player)
        print(" FIN de JUEGO - Nadie gana ")
        blackjack_conseguido = True
    else:
        if player == 21:
            print(" Tu puntuación es: ", player)
            print(" La puntuación de la Banca es: ", banca)
            print(" Has GANADO!!! ")
            blackjack_conseguido = True
        if banca == 21:
            print(" Tu puntuación es: ", player)
            print(" La puntuación de la Banca es: ",banca)
            print(" Ha ganado la Banca ")
            blackjack_conseguido = True
        else:
            blackjack_conseguido = False

    return blackjack_conseguido

def evaluar_resultado(player, banca):
    """
    Evalúa cuál de los dos está más cerca de 21 (jugador o banca)
    """
    #print(f'Player tiene {player}')
    #print(f'banca tiene {banca}')

    if banca > 21:
        print(" La puntuación de la banca es: ", banca)
        print(" Tu puntuación es: ", player)
        print(" Has GANADO!!! ")
    else:
        if banca < player:
            print(" La puntuación de la banca es: ", banca)
            print(" Tu puntuación es: ", player)
            print(" Has GANADO!!! ")
        else:
            print(" La puntuación de la Banca es: ", banca)
            print(" Tu puntuación es: ", player)
            print(" Ha ganado la Banca ")


def dar_carta(baraja):
    """
    Reparte una carta y la quita del mazo (al jugador o a la banca)
    """
    # dar carta
    carta = random.choice(baraja)
    # quitar carta de la baraja
    baraja.remove(carta)
    return carta

def mostrar_puntuacion_jugador(player):
    """
    Imprime la puntuación del jugador
    """
    # mostrar puntuacion
    print(" Tu puntuación es: ", player)

def reparte_primera_ronda(baraja):
    player = dar_carta(baraja)
    banca = dar_carta(baraja)
    mostrar_puntuacion_jugador(player)
    return player, banca

def pregunta_usuario():
    return input('¿Quieres otra carta? > (s/n)')

def turno_banca(banca, banca_se_planta, player, player_se_planta):
    if banca_se_planta:
        return
    if banca < 15:
        banca += dar_carta(baraja)
    else:
        banca_se_planta = True
    #
    turnos_sucesivos(player, banca, player_se_planta, banca_se_planta)


## recursividad
## ------------
def turnos_sucesivos(player, banca, player_se_planta, banca_se_planta):
    if player_se_planta and banca_se_planta:
        evaluar_resultado(player, banca)
        return

    if player_se_planta:
        turno_banca(banca, banca_se_planta, player, player_se_planta)
        return

    question = pregunta_usuario()
    if question.upper() == 'S':
        player += dar_carta(baraja)
        mostrar_puntuacion_jugador(player)
        fin_de_juego = evaluar_si_blackjack(player, banca)
        if fin_de_juego == True:
            return fin_de_juego
    if question.upper() == 'N':
        player_se_planta = True
    if len(question) == 0 or (question.upper() != 'N' and question.upper() != 'S'):
        print(f'Por favor escribe S o N, y nada más')
        #
        turnos_sucesivos(player, banca, player_se_planta, banca_se_planta)
    #
    turno_banca(banca, banca_se_planta, player, player_se_planta)



# ==============================================================================

imprimir_pantalla_inicio_juego()

baraja = crear_baraja()
player, banca = reparte_primera_ronda(baraja)
fin_de_juego = turnos_sucesivos(player, banca, False, False)
if fin_de_juego == False:
    evaluar_resultado(player, banca)

