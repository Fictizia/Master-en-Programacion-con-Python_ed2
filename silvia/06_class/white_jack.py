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
suit = list(range(1, 10))

for ten in range(4):
    suit.append(10)

maze = suit * 4

# Se inicializan los contadores de puntos del jugador y la banca
player_points = 0
bank_points = 0

# Se define una función que reparta una carta y la retire de la baraja


def give_a_card(maze):
    """
    parametro: maze

    elige un elemento de la lista maze (una carta de la baraja)
    retira ese elemento para que no se vuelva a repartir

    devuelve un entero
    """
    card = random.choice(maze)
    maze.remove(card)

    return card

# Se hace el primer reparto


player_points = give_a_card(maze)
print(f'Tienes {player_points} puntos.')

bank_points = give_a_card(maze)

# Flujo de juego

player_game, bank_game = True, True

while player_game == True or bank_game == True:
    if player_game == True:
        question = input('¿Quieres carta? (sí o no): ')
        if question == 'sí':
            player_card_value = give_a_card(maze)
            print(f'Carta jugador {player_card_value}')
            player_points += player_card_value
            print(f'Tienes {player_points} puntos.')
        else:
            player_game = False

    if player_points >= 21:
        break

    if bank_points < 15:
        bank_card_value = give_a_card(maze)
        print(f'Recibe carta la banca')
        bank_points += bank_card_value
#       print(f'Total BANCA {bank_points}')
    else:
        bank_game = False

    if bank_points >= 21:
        break


# Resultado

if (bank_points > 21) or (player_points <= 21 and player_points > bank_points):
    print(
        f'Has ganado. Tienes {player_points} puntos y la banca {bank_points} puntos')
else:
    print(
        f'Gana la banca. Tiene {bank_points} puntos y tú tienes {player_points} puntos')
