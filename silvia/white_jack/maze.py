import random

score = {'As': 1,
         '2': 2,
         '3': 3,
         '4': 4,
         '5': 5,
         '6': 6,
         '7': 7,
         '8': 8,
         '9': 9,
         '10': 10,
         'J': 10,
         'Q': 10,
         'K': 10,
         }

english_deck = {
    'tréboles': score,
    'corazones': score,
    'picas': score,
    'diamantes': score
}


def give_card(english_deck):
    suits = ['tréboles', 'corazones', 'picas', 'diamantes']
    values = ['As', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', 'J', 'Q', 'K']

    suit = random.choice(suits)
    value = random.choice(values)

    card = english_deck[suit][value]
    del english_deck[suit][value]
    print(f'Tu carta es el {value} de {suit}. Tienes {card} puntos')
    return card
