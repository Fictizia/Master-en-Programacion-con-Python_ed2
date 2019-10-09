# RESUMEN DÍA 2 (7/10/2019)

## TIPOS DE DATOS BÁSICOS

### **Strings o cadenas de texto**

Se pueden concatenar dos cadenas con el operador +:

```
print('Hola' + ' mundo')
```

Resultado:

```
Hola mundo
```

Existen otras formas de concatenar cadenas, con las que también se pueden concatenar datos de tipos diferentes:

```
name = 'Silvia'
age = '38'

print(f'hola {name} tienes {age} años, y sé que {name} realmente no es tu nombre')

print('hola {nombre} tienes {edad} años, y sé que {nombre} realmente no es tu nombre'.format(nombre = name, edad = age))

print('hola {} tienes {} años, y sé que {} realmente no es tu nombre'.format(name, age, name))

print('hola {0} tienes {1} años, y sé que {0} realmente no es tu nombre'.format(name, age))
```

En todos esos casos el resutado es el mismo:

```
hola Silvia tienes 38 años, y sé que Silvia realmente no es tu nombre
```

También se puede utilizar el operador \*:

```
print('hola ' * 5)
```

Resultado:

```
hola hola hola hola hola
```

Es posible acceder a una parte de una cadena:

```
texto_largo = 'En un lugar de La Mancha, de cuyo nombre no puedo acordarme'

print(texto_largo[:24])

print(texto_largo[26:])
```

Resultado:

```
En un lugar de La Mancha

de cuyo nombre no puedo acordarme
```

### **Números**

Los número pueden ser enteros (int) o decimales (float).

Al operar con números enteros, el resultado es un entero. Si uno de los operandos es decimal, el resultado será decimal:

```
entero = 1
decimales = 2.1
otro_decimal = 2.0

print(entero + entero)
print(entero + decimales)
print(entero + otro_decimal)
```

Resultado:

```
2
3.1
3.0
```

Se puede redondear un decimal al entero más cercano con la función round:

```
print(round(entero + otro_decimal))
```

Resultado:

```
3
```

### **Variables**

Las variables en Python son nombres que hacen referencia o apuntan a un valor.

Python es un lenguaje de tipado dinámico, por lo que una variable puede tomar valores de distinto tipo:

```
a = 1
b = 2
a = 'Juan'
print(a)
```

Resultado:

```
Juan
```

Cuando se asigna un valor a una variable, Python crea ese valor y nos podemos referir a él por el nombre de la variable. Sin embargo, la información está contenida en el propio valor, no en el nombre de la variable

Al crear una variable y asignarle un valor, ese valor ocupa un espacio en memoria. Por ejemplo:

```
c = 'hola'
d = c
c = ' Mundo'
print(d)
```

Resultado:

```
hola
```

En este caso, se ha creado el valor 'hola' y se le ha asignado la variable c. Al igualar d a c, ambas apuntan al mismo lugar en la memoria.

Al crear el nuevo valor ' Mundo' y asignarle la variable c, d sigue apuntando a 'hola' y ese será su valor, aunque d inicialmente fuera igual a c.

La función id() nos da el identificador de un valor. Este identificador es único para cada valor y permite ver si dos variables apuntan al mismo.

## TIPOS DE DATOS COMPLEJOS

### **Listas**

Son colecciones de elementos ordenados y mutables que se escriben entre corchetes []. Se pueden duplicar elementos:

```
fruits = ['banana', 'pear', 'apple']
```

Se puede acceder a los elementos de una lista mediante un índice:

```
print(fruits[0])
print(fruits[1])
print(fruits[2])
```

Resultado:

```
banana
pear
apple
```

Para añadir un nuevo elemento a una lista, se usa el método append():

```
fruits.append('pineapple')
print(fruits[3])
print(fruits)
```

Resultado:

```
pineapple
['banana', 'pear', 'apple', 'pineapple']
```

Al contrario que con los números o las cadenas de texto, las listas son objetos mutables, por lo que se pueden modificar sin cambiar el lugar que ocupan en memoria:

```
summer_fruits = ['melon', 'watermelon']
more_fruits = summer_fruits
print(more_fruits)
more_fruits[1] = 'pear'
print(more_fruits)
print(summer_fruits)
```

Resultado:

```
['melon', 'watermelon']
['melon', 'pear']
['melon', 'pear']
```

```
id(more_fruits)
140636847439176

id(summer_fruits)
140636847439176
```

Se puede saber la longitud de una lista con el método len():

```
a = [1, 2, 3]
a_length = len(a)
print(a_length)
```

Resultado:

```
3
```

Partiendo del ejemplo anterior, si añadimos un nuevo elemento a la lista a, el valor de a_length seguirá siendo 3, porque al asignarle el valor de la longitud de la lista a, en realidad le estamos dando como valor un número entero. De este modo, aunque la lista a varíe en su longitud, a_length seguirá valiendo 3:

```
a.append(4)
print(a_length)
print(len(a))
```

Resultado:

```
3
4
```

También se pueden formar listas de listas:

```
b = ['a', 'b', 'c']
c = [a, b]
print(c)
print(len(c))
```

Resultado:

```
[[1, 2, 3, 4], ['a', 'b', 'c']]
2
```

Para acceder a los elementos de las listas de listas se utilizan también índices:

```
first_list = c[0]
print(first_list[2])
```

Resultado:

```
3
```

Existen dos operandos que pueden dar lugar a confusión. Son el operando == y el operando _is_. El operando == evalúa que el valor de los elementos comparados sea igual, y el operando _is_ mira si esos elemntos se refieren a un valor que se encuentra en una misma dirección de memoria:

```
x = [1, 2]
y = [1, 2]
print(x == y)
print(x is y)
```

Resultado:

```
True
False
```

### **Tuplas**

Las tuplas se diferencian de las listas en que son inmutables y se escriben entre paréntesis ().

```
a = ('a', 'b')
b = (1, True, 'c')
print(a)
print(b)
print(len(a))
print(b[2])
```

Resultado:

```
('a', 'b')
(1, True, 'c')
2
c
```

Ejemplo de que no se pueden cambiar:

```
b[3] = 1.5
```

Resultado:

```
TypeError: 'tuple' object does not support item assignment
```

### **Sets**

Son colecciones de elementos sin ordenar, sin indexar y que no admiten duplicados. Se escriben entre llaves {}:

```
my_set = {1, 1, 2, 2, 4}
print(my_set)

first_url = 'www.google.com/first_url'
second_url = 'www.google.com/first_url'

my_urls = {first_url, second_url}

print(my_urls)
```

Resultado:

```
{1, 2, 4}
{'www.google.com/first_url'}
```

Para comprobar si un elemento se encuetra en una colección de elemntos en Python, se utiliza la palabra in:

```
first_list = [1, 2, 3]
a_tuple = (4, 2, 7, 7)

print(7 in a_tuple)
print(7 in first_list)
```

Resultado:

```
True
False
```

Con el método set() se pueden convertir listas o tuplas en sets:

```
first_set_from_list = set(first_list)
second_set_from_list = set(a_tuple)

print(first_set_from_list)
print(second_set_from_list)
```

Resultado:

```
{1, 2, 3}
{2, 4, 7}
```

Con los sets se pueden hacer diferentes operaciones:

- Intersección, devuelve un set que es la intersección de otros:

  ```
    print(first_set_from_list.intersection(second_set_from_list))
  ```

  Resultado:

  ```
    {2}
  ```

- Unión, devuelve un set que es la unión de otros:

  ```
    print(first_set_from_list.union(second_set_from_list))
  ```

  Resultado:

  ```
    {1, 2, 3, 4, 7}
  ```

- Diferencia, devuelve un set que es la diferencia entre dos sets:

  ```
    print(first_set_from_list.difference(second_set_from_list))

    print(first_set_from_list - second_set_from_list)
  ```

  Resultado:

  ```
    {1, 3}

    {1, 3}
  ```

- Averiguar si un set contiene otro set:

  ```
    print(first_set_from_list.issubset(second_set_from_list))
  ```

  Resultado:

  ```
    False
  ```

No es posible hacer sets que contengan otros sets:

```
my_lists = {first_set_from_list, second_set_from_list}
print(my_lists)
```

Resultado:

```
TypeError: unhashable type: 'list'
```

### **Diccionarios**

Son colecciones de elementos desordenados, mutables e indexados. Se escriben entre llaves y sus elementos tienen clave(key) y valor. Podemos acceder a los elementos del diccionario mediante escribiendo su clave entre corchetes []:

```
name = 'jose'
friend_list = ['Alberto', 'Silvia', 'Gonzalo']

my_dict = {'name': name,
            'age': 30,
            'friends': friend_list,
            }
print(my_dict)

my_key = 'name'
print(f'Me llamo {my_dict[my_key]}')
```

Resultado:

```
{'name': 'jose', 'age': 30, 'friends': ['Alberto', 'Silvia', 'Gonzalo']}

Me llamo jose
```

Al ser mutables, si asignamos a una variable un diccionario que ya existe, esta nueva variable apuntará a la misma dirección de memoria:

```
other_dict = my_dict
other_dict['age'] = 35

print(id(other_dict))
print(id(my_dict))
```

Resultado:

```
140638476776216
140638476776216
```

Otra forma de acceder a los elementos de un diccionario es mediante el método get(). Si la clave no existe, devolverá _None_ por defecto o se puede indicar que devuelva otra cosa. En el siguiente ejemplo se indica que devuelva False:

```
handsome = my_dict.get('handsome', False)

print(my_dict)
print(handsome)
```

Resultado:

```
{'name': 'jose', 'age': 35, 'friends': ['Alberto', 'Silvia', 'Gonzalo']}
False
```

Se pueden añadir elementos al diccionario de diferentes maneras:

- Con el método update(), preferiblemente:

```
if not handsome:
    my_dict.update({'handsome': True})

print(my_dict)
```

Resultado:

```
{'name': 'jose', 'age': 35, 'friends': ['Alberto', 'Silvia', 'Gonzalo'], 'handsome': True}
```

- ```
  my_dict['handsome'] = True
  ```

Resultado:

```
{'name': 'jose', 'age': 35, 'friends': ['Alberto', 'Silvia', 'Gonzalo'], 'handsome': True}
```

## RECURSOS

- [Python Variables](https://realpython.com/python-variables/ "Python Variables")

* [Tricky Python I : Memory Management for Mutable & Immutable Objects](https://medium.com/@tyastropheus/tricky-python-i-memory-management-for-mutable-immutable-objects-21507d1e5b95 "Tricky Python I : Memory Management for Mutable & Immutable Objects")
