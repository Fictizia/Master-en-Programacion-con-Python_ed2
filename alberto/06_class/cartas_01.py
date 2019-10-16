# Crear un usuario y una banca
# puedes pedir una carta mas o plantarte
# la banca tambien puede coger cartas y tiene el mismo cometido que es llegar a 21 y puede plantarse
# el que mas se aproxime a 21 gana sin pasarse gana

#crear baraja
#se reparte las dos primeras cartas a cada usuario
# una vez que se ha repartido tiene que existir la posiblidad de pedir una mas
# una vez que se haya pedido una mas tenemos que ver si el resultado es mayor que 21
# si no es mayor que 21 debemos dejar la posiblidad de dar una carta mas
# tenemos que tener en cuenta que a partir de la segunda carta se puede plantar (stop)

# figuras{
#     figura_j = {'nombre': 'j', 'valor': 10}
#     figura_q = {'nombre': 'q', 'valor': 10}
#     figura_k = {'nombre': 'k', 'valor': 10}
#     figura_a = {'nombre': 'a', 'valor': 1}
#     figura_dos = {'nombre': '2', 'valor': 2}
#     figura_tres = {'nombre': '3', 'valor': 3}
#     figura_cuatro = {'nombre': '4', 'valor': 4}
#     figura_cinco = {'nombre': '5', 'valor': 5}
#     figura_seis = {'nombre': '6', 'valor': 6}
#     figura_siete = {'nombre': '7', 'valor': 7}
#     figura_ocho = {'nombre': '8', 'valor': 8}
#     figura_nueve = {'nombre': '9', 'valor': 9}
#     figura_nueve = {'nombre': '9', 'valor': 10}
# }

import random

# elementos = list(range(1,10))
# for ten in range(4):
#     elementos.append(10)
# baraja = elementos + elementos + elementos + elementos
# print (baraja)

# usuario = 0
# banca = 0
elementos = list(range(1,10))
for ten in range (4):
    elementos.append(10)
baraja = elementos + elementos + elementos + elementos
print(baraja)


def primera_mano():
    carta_usuario = random.choice(baraja)
    carta_banca = random.choice(baraja)
    print(carta_usuario)
    # print(carta_banca)
    return carta_usuario, carta_banca


def quiere_otra_otra():
    respuesta = input('¿Quieres otra? ')
    if respuesta.upper() in 'NO':
        return False
    return True

def reparte_una_carta(carta_usuario, mano_banca):
    carta_usuario = random.choice(baraja)
    carta_banca = random.choice(baraja)
    print(carta_usuario)
    # print(carta_banca)
    return carta_usuario, carta_banca
# carta_banca, carta_usuario = quieres_una_mas()
carta_usuario, carta_banca = primera_mano()
if quiere_otra_otra():
    puntuacion_usuario, puntuacion_banca = reparte_una_carta(carta_usuario, carta_banca)
    if puntuacion_usuario == 21 or puntuacion_banca == 21:
        print('Has ganado ' + puntuacion_banca)
        print('Has ganado' + puntuacion_usuario)
    else:
        puntuacion_usuario > 21
        print(quiere_otra_otra())
    