# crear lista con los números del 1 al 100
# iterar uno a uno por los números
# si el número es múltiplo de 3, imprimir 'FIZZ'
# si el número es múltiplo de 5, imprimir 'BUZZ'
# si el número es múltipli de 3 y además de 5, imprimir 'FIZZBUZZ'
# si no es nada imprimir número

import random

# fizz_buzz_list = list()

# def create_list():
#     for num in range (1, 101):
#         fizz_buzz_list.append(num)
    
#     return fizz_buzz_list

# create_list()

fizz_buzz_list = [num for num in range(1, 101)]

def division(num):
        if num % 3 == 0 and num % 5 == 0: # if num % 15 == 0
            return 'FIZZBUZZ'
        if num % 3 == 0:
            return 'FIZZ'
        if num % 5 == 0:
            return 'BUZZ'
        return num

def fizzbuzz(fizz_buzz_list):
    for num in fizz_buzz_list:
        print(division(num))

fizzbuzz(fizz_buzz_list)

