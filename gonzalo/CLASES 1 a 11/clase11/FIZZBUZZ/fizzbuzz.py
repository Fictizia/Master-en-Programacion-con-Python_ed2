def fizzbuzz():
    for numero in range(1, 101):

        if numero%3 == 0 and numero%5 !=0:
            return('FIZZ')
        elif numero%3 != 0 and numero%5 == 0:
            return('BUZZ')
        elif numero%3 == 0 and numero%5 ==0:
            return('FIZZBUZZ')
        elif numero%3 != 0 and numero%5 !=0:
            return(numero)

#
fizzbuzz()

print(resultado)
    