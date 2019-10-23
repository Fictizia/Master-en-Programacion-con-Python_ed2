import random

def crear_baraja():
    pass

def evaluar_resultado(player, banca):
    print(f'Player tiene {player}')
    print(f'banca tiene {banca}')
    pass

def dar_carta():
    return random.randint(1,30)

def reparte_primera_ronda():
    player = dar_carta()
    banca = dar_carta()
    return player, banca

def pregunta_usuario():
    return input('¿Quieres otra carta? > (s/n)')

def turno_banca(banca, banca_se_planta, player, player_se_planta):
    if banca_se_planta:
        return
    if banca < 15:
        banca += dar_carta()
    else:
        banca_se_planta = True
        turnos_sucesivos(player, banca, player_se_planta, banca_se_planta)


def turnos_sucesivos(player, banca, player_se_planta, banca_se_planta):
    if player_se_planta and banca_se_planta:
        evaluar_resultado(player, banca)
        return

    if player_se_planta:
        turno_banca(banca, banca_se_planta, player, player_se_planta)
        return
      
    question = pregunta_usuario()
    if question.upper() == 'S':
        player += dar_carta()
    if question.upper() == 'N':
        player_se_planta = True
    if question and question.upper() != 'N' and question.upper() != 'S':
        print(f'Por favor escribe S o N, y nada más')
        turnos_sucesivos(player, banca, player_se_planta, banca_se_planta)
    turno_banca(banca, banca_se_planta, player, player_se_planta)
    


crear_baraja()
player, banca = reparte_primera_ronda()
turnos_sucesivos(player, banca, False, False)
evaluar_resultado(player, banca)