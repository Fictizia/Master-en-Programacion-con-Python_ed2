# RESUMEN DÍA 4 (11/10/2019)

## COMPLEJIDAD CICLOMÁTICA

Se produce cuando hay muchas estructuras anidadas.

## ENTORNO VIRTUAL

El virtualenv es un programa que permite crear entornos virtuales en Python. Con ello, se pueden utilizar de forma aislada diferentes versiones de una misma herramienta sin tener que instalarlo directamente en local.

Para crearlo:

```
python3 -m venv ./directorio
```

## FUNCIONES

Una función es un bloque de código que funciona cuando es llamada y a la que se le puede pasar un parámetro.

Ejemplo:

```
def greetings(name):
    print(f'Hola, {name}')

# greetings('Silvia')
```

Resultado:

```
Hola, Silvia
```

Ejemplo en que recibe como parámetro un diccionario:

```
def greetings(person, print_me):
    if print_me:
        name = person['name']
        age = person['age']
        print(f'Hola {name} tienes {age} años')
    else:
        print('Hakuna Matata')

greetings({'name': 'Jose', 'age': 36}, 'N')
```

Resultado:

```
Hola Jose tienes 36 años
```

## ITERAR SOBRE DICCIONARIOS

Existen varias formas de acceder a los elementos de un diccionario para iterar sobre ellos:

```
people_in_class = {'profe': 'Jose',
                'primer_alumno': 'Alberto',
                'segundo_alumno': 'Silvia',
                'tercer_alumno': 'Gonzalo'}

print(people_in_class.items())
```

Resultado:

```
dict_items([('profe', 'Jose'), ('primer_alumno', 'Alberto'), ('segundo_alumno', 'Silvia'), ('tercer_alumno', 'Gonzalo')])
```

Para acceder a los elementos e iterar sobre ellos:

```
for clave, valor in people_in_class.items():
print(clave)
print(valor)
```

Resultado:

```
profe
Jose
primer_alumno
Alberto
segundo_alumno
Silvia
tercer_alumno
Gonzalo
```

Otra forma de hacerlo:

```
for clave in people_in_class:
    print(clave)
    print(people_in_class[clave])
```

Resultado:

```
profe
Jose
primer_alumno
Alberto
segundo_alumno
Silvia
tercer_alumno
Gonzalo
```
