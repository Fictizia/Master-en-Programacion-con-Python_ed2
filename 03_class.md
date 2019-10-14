# RESUMEN DÍA 3 (9/10/2019)

## OPERADORES LÓGICOS AND Y OR

El operador **and** devuelve True si ambas afirmaciones son ciertas.

El operador **or** devuelve True si una de las afirmaciones es cierta.

En Python se utiliza la indentación (4 espacios) para agrupar código en un bloque.

Ejemplos:

```
if True:
    print('I`m in')
else:
    print('I`m out now')

if True and True and True:
    print('I`m True')

if True and False:
    print('I`m True again')
else:
    print('I\'m False')

if True or False:
    print('I`m True again')

if False or False:
    print('if False or False')
```

Resultado:

```
I`m in
I`m True
I'm False
I`m True again
```

## CONDICIONALES - IF STATEMENTS

Los if statements tienen la siguiente estructura básica:

```
if condition:
    statement # lo que pasa si se cumple la condición
```

Si hay varias condiciones que pueden tener diferentes statements, la estructura es la siguiente:

```
if condition1:
    statement1 # lo que pasa si se cumple la condición 1
elif condition2:
    statement2 # lo que pasa si se cumple la condición 2
else:
    statement3
```

Se puede usar también la estructura:

```
if not condition:
    statement # lo que pasa si se cumple la condición
```

Es buena práctica usar el **if** en positivo. Cuanto menos **not** usemos, mejor.

Ejemplos:

```
a = 1
b = 2
c = 1

my_condition = a < b
print(my_condition)
if my_condition:
    print('a es menor que b')

if a < b:
    print('un if de toda la vida')
else:
    print('b es menor que a')

if a < b and b > c:
    print('a es menor que b y b es mayor que c')

if (a > b) or (c < b and c == a):
    print('lol, como te complicas')
```

Resultado:

```
True
a es menor que b
un if de toda la vida
a es menor que b y b es mayor que c
lol, como te complicas
```

## BUCLES

### WHILE

El bucle while ejecuta un conjunto de statements mientras se cumpla una condición.

Ejemplo:

```
counter = 1
counter += 1 # counter = counter + 1

while counter > 0:
    print(f'Im bigger than 0 and Im {counter}')
    counter += 1
```

Como resultado da un bucle infinito que comienza con:

```
Im bigger than 0 and Im 2
```

### FOR

Un bucle for se usa para iterar sobre iterables, como listas, sets o tuplas. También sobre diccionarios.

Con la funcion range(), se itera sobre los valores comprendidos en ese rango.

Ejemplo:

```
pair_numbers = list()
for number in range(0, 10, 2):
    pair_numbers.append(number)

print(pair_numbers)
```

En este caso, el bucle itera entre los números 0 y 9, de dos en dos, dando como resultado:

```
[0, 2, 4, 6, 8]
```

También se puede iterar sobre un texto:

```
text = '''En un lugar de la Mancha de cuyo nombre no puedo acordarme
vivía un hidalgo que no me acuerdo si tenía una talla XL'''

index = 0

for char in text:
    if char == 'x' or char == 'X':
        break
    index += 1

print(text[0:index])
```

Resultado:

```
En un lugar de la Mancha de cuyo nombre no puedo acordarme
vivía un hidalgo que no me acuerdo si tenía una talla
```

Otra forma de hacer lo mismo es con el método rindex():

```
index = text.rindex('X')

print(text[0:index])
```

Resultado:

```
En un lugar de la Mancha de cuyo nombre no puedo acordarme
vivía un hidalgo que no me acuerdo si tenía una talla
```

En Python existen numerosos métodos que se pueden usar en las cadenas de caracteres. Entre ellos, está en método split(), que parte una cadena de caracteres por donde se le indique y devuelve una lista:

```
text1 = 'banana, pear, melon, watermelon'
my_list = text1.split(', ')

print(my_list)
```

Resultado:

```
['banana', 'pear', 'melon', 'watermelon']
```

También se puede iterar sobre listas:

```
shopping_list = ['mouse', 'keyboard', 'monitor', 'operating system', 'windows']

for item in shopping_list:
    print(item)
```

Resultado:

```
mouse
keyboard
monitor
operating system
windows
```

Otro ejemplo:

```
numbers = [2, 8, 7, 5, 0, 9, 22, 99]
double_numbers = list()

for number in numbers:
    double = number * 2
    double_numbers.append(double)

print(double_numbers)
```

Resultado:

```
[4, 16, 14, 10, 0, 18, 44, 198]
```

## INPUT

input() es una función que permite al usuario introducir un dato. Ese dato que introduce el usuario, está en un formato con el que Python no puede trabajar, así que hay que transformarlo:

```
number = input('Dime un número entero para calcular si es primo  $>: ') # lo que se mete va en formato raw
number = int(number)
```

Resultado:

```
Dime un número entero para calcular si es primo  $>:
```
