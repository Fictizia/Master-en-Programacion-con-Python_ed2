from silvia.white_jack.maze import give_card, english_deck

# print(english_deck)
# card = give_card(english_deck)

# print(card)
# print('ED', english_deck)


def continue_game(english_deck, player_points, bank_points, player_game=True, bank_game=True):
    """
    Parámetro 1: english_deck. Parámetro 2: player_points. Parámetro 3: bank_points
    Hay un input con el que el jugador indica si quiere recibir otra carta y le dice el número de puntos que tiene
    Si el jugador tiene más de 21 puntos, pierde
    La banca recibe carta siempre que tenga menos de 15 puntos. Si se pasa de 21, pierde
    Después de cada turno, evalúa el resultado
    return None
    """

    if player_game:
        question = input('¿Quieres carta? (sí o no): ')
        if 'S' in question.upper() and player_game:
            player_card_value = give_card(english_deck)
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
            bank_card_value = give_card(english_deck)
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


player_points = give_card(english_deck)  # Contador de puntos del jugador
bank_points = give_card(english_deck)  # Contador de puntos de la banca
print(f'Tienes {player_points} puntos')
continue_game(english_deck, player_points, bank_points)
