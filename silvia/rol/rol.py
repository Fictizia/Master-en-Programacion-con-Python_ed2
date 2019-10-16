import json

from random import randint

DATA_PATH = './silvia/rol/players.json'


def tirar_dado():
    tirada = randint(0, 100)
    return tirada


def usuarios_vivos(PATH):

    players_dict = dict()

    with open(PATH, 'r') as json_file:
        # Transformo el json en un diccionario
        players_dict = json.load(json_file)

    def sort_list(e):
        # e, son los elementos de ordered_players
        return players_dict[e]['orden']

    ordered_players = list()

    for key in players_dict:
        if players_dict[key]['vida'] > 0:
            ordered_players.append(key)

    # Al método sort, hay que pasarle una función propia(sort_list) para decir con qué criterio ordena
    ordered_players.sort(key=sort_list)

    return ordered_players


def update_life(PATH, player, action, amount):

    players_dict = dict()

    with open(PATH, 'r') as json_file:
        players_dict = json.load(json_file)

    if action == 'add':
        players_dict[player]['vida'] += amount
    else:
        players_dict[player]['vida'] -= amount

    with open(PATH, 'w') as json_file:
        json.dump(players_dict, json_file)


# Obtener listado de jugadores

players_list = usuarios_vivos(DATA_PATH)

# Hacer bucle while listado jugadores > 1 se ejecute

while len(players_list) > 1:

    for player in players_list:  # Recorre listado jugadores
        score = tirar_dado()  # Cada jugador lanza el dado y actualiza los puntos de vida
        if score < 50:
            update_life(DATA_PATH, player, 'minus', 1)
        else:
            update_life(DATA_PATH, player, 'add', 1)

    players_list = usuarios_vivos(DATA_PATH)  # Actualiza listado de jugadores

print(f'El ganador es {players_list[0]}')
