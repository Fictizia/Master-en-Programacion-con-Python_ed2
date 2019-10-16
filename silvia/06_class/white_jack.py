# Un jugador y la banca
# La banca reparte una carta a cada uno y luego pregunta si quieres más
# Dos opciones: pedir carta o plantarte
# Aunque uno se plante, el otro se puede plantar
# Cuando los dos se han plantado, gana el que más se acerque a 21 sin pasarse
# Si uno se pasa primero, pierde
# Valor de las cartas: figuras: 10 puntos; as: 1 punto; resto: lo que marque la carta
# No se puede repartir la misma carta más de una vez

import random

suit = list(range(1, 10))

for ten in range(4):
    suit.append(10)

maze = suit * 4

user = 0
bank = 0

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

user = give_a_card(maze)
print(f'Tienes {user} puntos')

bank = give_a_card(maze)

play = True

def user_turn(user):
    if ask_for_card == 'yes':
        points = give_a_card(maze)
        user += points
    else:
        if user <= 21 and user > bank:
            print(f'Tienes {user} puntos y la banca {bank} ¡¡Has ganado!!')
        play = False
    return user

def bank_turn(bank):
    if bank <= 15:
        points = give_a_card(maze)
        bank += points
    else:
        print('La banca se planta')
        play = False
    return bank

while play == True:
    ask_for_card = input('¿Quieres otra carta? (yes/no): ')
    user_turn()

    bank_turn()



            


    









    
    


 






