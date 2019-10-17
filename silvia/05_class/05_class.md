# RESUMEN DÍA 4 (11/10/2019)

## MÓDULOS

Un módulo es un archivo de Python que se puede utilizar para añadir a proyectos.

Si tenemos un proyecto y queremos usar un módulo, tenemmos que importarlo de la siguiente manera:

```
from ubicación import nombre_del_módulo
```

Un módulo puede contener funciones y variables de todo tipo (diccionarios, objejos, etc) y es posible importar únicamente una de esas funciones o variables:

```
from ubicación import nombre_de_la_función(o_variable)
```

Para importar los módulos que vienen en Python por defecto:

```
import nombre_del_modulo
```

Se pueden importar también funcionalidades concretas de un módulo:

```
from random import randint

print(randint(0, 10))
```

Generalmente, para indicar la ubicación de los módulos se usan rutas absolutas, al ser más completas. Los directorios se separan por . en lugar de por /:

```
from .constants.vending import items
```

En este caso, items es un diccionario. Para acceder a los elementos de ese diccionario, se haría como si ese diccionario estuviese en el mismo archivo:

```
print(items['coca-cola']['price'])
```

**REPASAR PYTHONPATH - Consultar**

## FICHEROS

Desde Python, se puede trabajar con ficheros.

Para escribir en un fichero:

```
with open('./example.csv', 'w') as file:
    file.writelines('greet, hello world')
```

En este ejemplo, se crea (si no existe) el archivo example.csv y lo guarda en la variable file. 'w' indica que se sobreescriba el fichero. Si se una 'rw', primero lo lee y luego lo sobreescribe. Si no se indica nada, entiende que es 'w'. Al finalizar, se cierra el archivo.

## RECURSOS

### Módulos

- [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/ "Python Modules and Packages – An Introduction")
- [Absolute vs Relative Imports in Python](https://realpython.com/absolute-vs-relative-python-imports/ "Absolute vs Relative Imports in Python")

### Ficheros

- [Reading and Writing Files in Python (Guide)](https://realpython.com/read-write-files-python/ "Reading and Writing Files in Python (Guide)")
- [Working With Files in Python](https://realpython.com/working-with-files-in-python/ "Working With Files in Python")
- [Working With JSON Data in Python](https://realpython.com/python-json/ "Working With JSON Data in Python")
