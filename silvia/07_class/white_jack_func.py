# Un jugador y la banca
# La banca reparte una carta a cada uno y luego pregunta si quieres más
# Dos opciones: pedir carta o plantarte
# Aunque uno se plante, el otro se puede plantar
# Cuando los dos se han plantado, gana el que más se acerque a 21 sin pasarse
# Si uno se pasa primero, pierde
# Valor de las cartas: figuras: 10 puntos; as: 1 punto; resto: lo que marque la carta
# No se puede repartir la misma carta más de una vez

import random

# Se crea la baraja


def create_maze():
    """
    Crea una baraja a partir de una lista del 1 al 10 y le añade 3 cartas de valor 10, equivalentes a las figuras J, Q, K

    Multiplica esa lista por 4, una por palo

    Devuelve una lista con los valores de cada carta de los 4 palos
    """
    suit = list(range(1, 10))  # Cartas en un palo

    for _ in range(4):
        suit.append(10)

    deck = suit * 4  # La baraja son las figuras de los cuatro palos
    return deck


# Se define una función que reparta una carta y la retire de la baraja

def give_a_card(maze):
    """
    Parámetro: maze

    Elige un elemento de la lista maze (una carta de la baraja)

    Retira ese elemento para que no se vuelva a repartir

    Devuelve un entero
    """
    card = random.choice(maze)
    maze.remove(card)

    return card

# Juego después del primer reparto


def continue_game(english_deck, player_points, bank_points, player_game=True, bank_game=True):
    """
    Parámetros: english_deck, player_points, bank_points

    Hay un input con el que el jugador indica si quiere recibir otra carta y le dice el número de puntos que tiene

    Si el jugador tiene más de 21 puntos, pierde

    La banca recibe carta siempre que tenga menos de 15 puntos. Si se pasa de 21, pierde

    Después de cada turno, evalúa el resultado

    return None
    """

    if player_game:
        question = input('¿Quieres carta? (sí o no): ')
        if 'S' in question.upper() and player_game:
            player_card_value = give_a_card(english_deck)
            print(f'Carta jugador {player_card_value}')
            player_points += player_card_value
            print(f'Tienes {player_points} puntos')
        else:
            player_game = False

    if player_points >= 21:
        print('Te has pasado de 21')
        evaluate_result(player_points, bank_points)
        return

    if bank_game:

        if bank_points < 15 and bank_game:
            bank_card_value = give_a_card(english_deck)
            print(f'La banca recibe carta')
            bank_points += bank_card_value
            print(f'Total BANCA {bank_points}')
        else:
            bank_game = False
            print('La banca se planta')

    if bank_points >= 21 or not (player_game or bank_game):
        evaluate_result(player_points, bank_points)
        return

    continue_game(english_deck, player_points,
                  bank_points, player_game, bank_game)

# Función que evalúa el resultado


def evaluate_result(player_points, bank_points):
    if (bank_points > 21) or (player_points <= 21 and player_points > bank_points):
        print(
            f'Has ganado. Tienes {player_points} puntos y la banca {bank_points} puntos')
    else:
        print(
            f'Gana la banca. Tiene {bank_points} puntos y tú tienes {player_points} puntos')


english_deck = create_maze()
player_points = give_a_card(english_deck)  # Contador de puntos del jugador
bank_points = give_a_card(english_deck)  # Contador de puntos de la banca
print(f'Tienes {player_points} puntos')
continue_game(english_deck, player_points, bank_points)
