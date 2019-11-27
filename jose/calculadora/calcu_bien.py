def calcula(numero):
    operador = input()
    segundo_num = int(input())

    if operador == '+':
        segundo_num = numero + segundo_num
    elif operador == '-':
        segundo_num = numero - segundo_num
    elif operador == '*':
        segundo_num = numero * segundo_num
    elif operador == '/':
        segundo_num = numero / segundo_num
    print(segundo_num)
    calcula(segundo_num)



primer_numero = int(input())
calcula(primer_numero)

