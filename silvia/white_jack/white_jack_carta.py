import random

import maze

suits = ['tréboles', 'corazones', 'picas', 'diamantes']
values = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

suit = random.choice(suits)
value = random.choice(values)

card = maze.english_deck[suit][value]

print(f'Tu carta es el {value} de {suit}')
print(card)

DATA_PATH = './silvia/white_jack/maze.py'

with open(DATA_PATH, 'w'):
    english_deck.pop(card)
