# number = 1
# three_multiples = list()


# while number <= 100:
#     if number % 3 == 0 and number % 2 == 0:
#         three_multiples.append(number)
#     number += 1
#     if len(three_multiples) == 10:
#         break

# print(three_multiples)
# print(len(three_multiples))
# multiplicando = 1
# multiplicador = 1
# while multiplicando <= 5:
#     while multiplicador <= 10:
#         print(f' {multiplicando} x {multiplicador} = {multiplicador * multiplicador}')
#         multiplicador += 1      
#     print('--------------')
#     multiplicando += 1
#     multiplicador = 1


#     for number in range(1,101,2):
#         print(number)


#     pair_numbers = list ()
#     for number in range(0,10,2):
#             pair_numbers.append(number)
#     print(pair_numbers)


# text = '''En un lugar de la mancha de cuyo no quiero acordarme
# vivia un hidalgo que no me acuerdo si tenía una talla XL'''

# no_x_in_text = ''

# for char in text:
#     if char == 'x' or char == 'X':
#         break
#     no_x_in_text += char

# print(no_x_in_text)

# index = 0 
# for char in text:
#     if char == 'x' or char == 'X':
#         break
#     index += 1
# print(text[0:index])

# shopping_list = ['mouse', 'keyboard', 'monitor', 'operating system', 'windows']
# for item in shopping_list:
#     print(item)

# number_two = list()
# shopping_list = [2, 5, 5, 6, 6, 8]
# for number in shopping_list:
#     number_two = number * 2
#     number_two.append(number)
# print(number_two)

# number = input('Dime un número entero $>:')
# number = int(number)

#if number <= 1:
    #if number == 2:
    #print('El número tiene que ser mayor que 1 para poder ser primo')

comprobar = True
while comprobar:
    n = int(input('Introduce un número'))
    if n > 0:
        comprobar = False
        i = 2 
        while i < n:
            c = 2
            primo = True
            while primo and c < i:
                if i % c == 0:
                    primo = False
                else:
                    c += 1
                i += 1
        if True:
            print(i, "Es primo")
    
    else:
        print ("No es correcto, vuelve a intentarlo.")