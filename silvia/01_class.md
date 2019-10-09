# RESUMEN DÍA 1 (4/10/2019)

## COMANDOS UNIX IMPORTANTES

- `<mkdir workspace>`: crea un nuevo directorio, en este caso llamado workspace.
- `<ls>`: lista el contenido de un directorio.
- `<cd workspace>`: cambia de directorio. En este caso nos lleva al directorio workspace.
- `<pwd>`: indica el directorio actual.
- `<rm -rf directorio>`:
  - rm: borra directorio.
  - -rf: borra recursivamente todos los subdirectorios y archivos que cuelgan del directorio a borrar.

## GIT

Es un sistema de control de versiones.

GitHub es un alojamiento de repositorios de Git.

### Flujo de trabajo

Estando logados en GitHub, hacemos un Fork del repositorio original. En este caso, hacemos un Fork del repositorio https://github.com/Fictizia/Master-en-Programacion-con-Python_ed2.git. De este modo, se crea una copia de ese repositorio en nuestra cuenta de GitHub.

Cuando ya tenemos este repositorio en GitHub, lo clonamos desde nuestra cuenta a nuestro equipo con el comando
`<git clone https://github.com/sarnaizgarcia/Master-en-Programacion-con-Python_ed2.git>`

En Visual Studio Code, una vez que hemos hecho los cambios, pinchamos en el icono del condensador que nos mostrará el listado de cambios realizados para añadir los que se necesite al Stagging Area con el botón en el que aparece un +. Una vez seleccionados los cambios que se quieren añadir, para hacer el commit se pincha en el icono de verificación (√) y se indican en el mensaje las modificaciones que se han hecho.

Para subir los cambios hechos en local a nuestro repositorio en GitHub se utiliza el icono de sincronización que está en la parte inferior de la pantalla.

De este modo, quedan registrados los cambios en nuestros repositorio local y en el que se encuentra en nuestra cuenta de GitHub.

Para que los cambios que hemos hecho en ese repositorio se suban al repositorio de origen (del que se ha hecho el Fork), hemos de hacer una Pull Request, que es un commit que debe aprobar el “propietario” del repositorio original.

Puede pasar que desde que hemos hecho el Fork del repositorio original, se hayan hecho cambios en este y nuestro Fork se encuentre desactualizado. Para actualizarlo, pinchamos en Pull Request, New Pull Request, botón de comparar y en la opción “Try switching the base”. En caso de que estemos desactualizados, se solicitará una nueva Pull Request del repositorio original de Fictizia a nuestro Fork.

Para cambiar en Git el usuario que queremos que aparezca usamos el comando: `<git config --local user.name ‘nombre’>`

Para cambiar el email: `<git config --local user.email ‘email’>`

## PYTHON

Lenguaje interpretado, no se compila.

Tipado dinámico fuerte. Sólo se puede operar con operandos que sean del mismo tipo.

### Tipos de datos

- **Básicos**:

  - strings o cadenas de texto. Se escriben entre comillas dobles (") o simples (').
  - números:
    - enteros.
    - decimales o floats, positivos o negativos.
  - booleanos:
    - True.
    - False.

Ejemplos:

- type('hola') class 'str'.
- type(1) class 'int'.
- type(1.5) class 'float'.
- type(True) class 'bool'.
- type([1, 2]) class 'list'.

* **Complejos**:

  - listas (arrays). Se escriben entre corchetes ([]).
  - tuplas:
    - similares a las listas, pero son inmutables.
    - se escriben entre paréntesis ().

* **Variables**:

  Se escriben en minúscula y en snake case (con \_ entre palabras). Las constantes se escriben en mayúscula.

  No se tiene que declarar la variable. Simplemente nombrarla para asignarle el valor.

Ejemplos:

* a = 12
* cadena_uno = 'hola'
* cadena_dos = 'mundo'
* cadena_uno + cadena_dos = 'hola mundo'


## RECURSOS

### Git

[Forking Projects](https://guides.github.com/activities/forking/ "Forking Projects")

### Markdown

- [StackEdit](stackedit.io "StackEdit")
- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/ "Mastering Markdown")

### Python

- [PEP8 (Guía de estilo en Python)](https://www.python.org/dev/peps/pep-0008/ "PEP8")
- [The Zen of Python](https://www.python.org/dev/peps/pep-0020/ "The Zen of Python")
