# crear lista con numberos del 1 al 100
# iterar uno a uno por los numeros
# si el número es múltiplo de 3, print 'FIZZ' 
# si el número es múltiplo de 5, print 'BUZZ'
# si el número es múltiplo de 3 y además de 5, print 'FIZZBUZZ'
# SI NO ES NADA IMPRIMIR NUMERO

numbers_to_hundred = [number for number in range(1,101)]

def division(number):
    if number % 15 == 0 and number % 5 == 0:
        return 'FIZZBUZZ'
    if number % 3 == 0:
        return 'FIZZ'
    if number % 5 == 0:
        return 'BUZZ'
    return number

def fizzbuzz(numbers):
    for number in numbers:
        print(division(number))

fizzbuzz(numbers_to_hundred)