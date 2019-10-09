# BASICS STRINGS

name = 'Jose'
age = 36
print(f'hola {name} tienes {age} años, y sé que {name} realmente no es tu nombre')

print('hola {nombre} tienes {edad} años, y sé que {nombre} realmente no es tu nombre'.format(nombre = name, edad = age))

print('hola ' * 5)

texto_largo = 'En un lugar de La Mancha, de cuyo nombre no puedo acordarme'
print(texto_largo[:24])

# BASIC NUMBERS

entero = 1
decimales = 2.1
otro_decimal = 2.0

print(entero + entero) # 2
print(entero + decimales) # 3.1
print(entero + otro_decimal) # 3
print(round(entero + otro_decimal))

# BASIC VARIABLES

a = 1
b = a
a = 2
print(b) # b = 1

c = 'hola'
d = c
c = ' Mundo'
print(d) # hola

