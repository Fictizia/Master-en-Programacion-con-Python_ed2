
from random import randint

from jose.oop.humano import Humano
from jose.oop.mago import Mago
from jose.oop.dementor import Dementor

alberto = Humano(1.8, True, 'blanca')
harry = Mago(1.5, False, 'blanca')
dementor = Dementor(3, True, 'transparente')

randomize_object = [alberto, harry, dementor]
for _ in range(1, 10):
    index = randint(0,2)
    winner = randomize_object[index]
    winner.alardear()