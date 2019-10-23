import json
from random import randint

DATA_PATH = './silvia/rol/players.json'


def throw_dice():
    """
    Aquí debería haber una descripción de la función
    """
    score_dice = randint(0, 100)
    return score_dice


def alive_players(PATH):

    players_dict = dict()

    with open(PATH, 'r') as json_file:
        # Transformo el json en un diccionario
        players_dict = json.load(json_file)

    def sort_list(e):
        # e, son los elementos de ordered_players
        return players_dict[e]['turn']

    ordered_players = list()

    for key in players_dict:
        if players_dict[key]['life'] > 0:
            ordered_players.append(key)

    # Al método sort, hay que pasarle una función propia(sort_list) para decir con qué criterio turna
    ordered_players.sort(key=sort_list)

    return ordered_players


def update_life(PATH, player, action, amount):

    players_dict = dict()

    with open(PATH, 'r') as json_file:
        players_dict = json.load(json_file)

    if action == 'add':
        players_dict[player]['life'] += amount
    else:
        players_dict[player]['life'] -= amount

    with open(PATH, 'w') as json_file:
        json.dump(players_dict, json_file)


# Obtener listado de jugadores

players_list = alive_players(DATA_PATH)

# Hacer bucle while listado jugadores > 1 se ejecute

while len(players_list) > 1:

    for player in players_list:  # Recorre listado jugadores
        score = throw_dice()  # Cada jugador lanza el dado y actualiza los puntos de vida
        if score < 50:
            update_life(DATA_PATH, player, 'minus', 1)
        else:
            update_life(DATA_PATH, player, 'add', 1)

    players_list = alive_players(DATA_PATH)  # Actualiza listado de jugadores

print(f'El ganador es {players_list[0]}')
