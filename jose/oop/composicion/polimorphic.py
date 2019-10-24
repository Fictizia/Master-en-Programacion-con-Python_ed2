
from random import randint

from jose.oop.composicion.humano import Humano
from jose.oop.composicion.mago import Mago
from jose.oop.composicion.dementor import Dementor

alberto = Humano(1.8, True, 'blanca')
harry = Mago(alberto)
dementor = Dementor()

randomize_object = [alberto, harry, dementor]
for _ in range(1, 10):
    index = randint(0,2)
    winner = randomize_object[index]
    winner.alardear()