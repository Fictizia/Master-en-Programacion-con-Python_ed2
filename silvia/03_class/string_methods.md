# STRING METHODS

- **.capitalize()**: devuelve una copia de la cadena con el primer caracter en mayúscula y el resto en minúscula.

```
text = 'temiendo Dantés ser sorprendido en las grutas durante la noche, cogió su fusil y salió al aire libre.'

capitalized = text.capitalize()
print(texto_cap)

Temiendo dantés ser sorprendido en las grutas durante la noche, cogió su fusil y salió al aire libre.
```

- **.casefold()**: devuelve todo el texo en minúsculas.

```
text = 'temiendo Dantés ser sorprendido en las grutas durante la noche, cogió su fusil y salió al aire libre.'

casefolded = text.casefolded()
print(casefolded)

temiendo dantés ser sorprendido en las grutas durante la noche, cogió su fusil y salió al aire libre.
```

- **.center(width[, fillchar])**: centra un texto, que tendrá la longitud que le indiquemos:

  - width: longitud que queremos que tenga el texto.
  - fillchar (opcional): carácter con el que se rellenan los espacios en blanco.

```
text = 'cogió su fusil y salió al aire libre'

centered = text.center(30, '-')
print(centered)

------------cogió su fusil y salió al aire libre------------
```

- **.count(sub[, start[, end]])**: devuelve el número de veces que un valor concreto aparece en un texto:

  - sub: la cadena que queremos localizar.
  - start (opcional): entero que indica en qué posición queremos empezar a buscar. Por defecto es 0.
  - end (opcional): entero que indica en qué posición queremos finalizar la búsqueda. Por defecto es el final de la cadena.

```
text = 'temiendo Dantés ser sorprendido en las grutas durante la noche, cogió su fusil y salió al aire libre.'

counted = text.count('r', 17)
print(counted)

7 # veces que aparece 'r' a partir de la posición 17
```

- **str.encode(encoding="utf-8", errors="strict")**

* **.endswith(suffix[, start[, end]])**: devuelve True si el string finaliza con el valor especificado o False si no es así:
  - suffix: valor que queremos comprobar si finaliza la cadena.
  * start (opcional): entero que indica en qué posición queremos empezar a buscar.
  * end (opciona): entero que indica en qué posición queremos finalizar la búsqueda.

```
text = 'temiendo Dantés ser sorprendido en las grutas durante la noche, cogió su fusil y salió al aire libre.'

ended_with = text.endswith('r')
print(ended_with)

False

```

# RECURSOS

[String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods "String Methods")
