def calcular(number):
    operator = input()
    second_num = input()
    result = f'{number} {operator} {second_num}'
    print(eval(result))
    calcular(result)

first_num = input()
calcular(first_num)

