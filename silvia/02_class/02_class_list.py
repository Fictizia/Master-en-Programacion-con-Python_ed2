# LISTAS

fruits = ['banana', 'pear', 'apple']
print(fruits[0])
print(fruits[1])
print(fruits[2])
fruits.append('pineapple')
print(fruits[3])

summer_fruits = ['melon', 'watermelon']
more_fruits = summer_fruits
print(more_fruits)
more_fruits[1] = 'pear'
print(more_fruits)
print(summer_fruits)


a = [1, 2, 3]
a_length = len(a)
print(a_length)
a.append(4)
print(a_length)
print(len(a))
b = ['a', 'b', 'c']
c = [a, b]
print(c)
print(len(c))

first_list = c[0]
print(first_list[2])

x = [1, 2]
y = [1, 2]
print(x == y) # True
print(x is y) # False. El operando is, al tratar con variables complejas, mira que sea la misma dirección de memoria. 