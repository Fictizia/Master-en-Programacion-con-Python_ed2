## Trabajando con ficheros (e import)
**Uso de WITH**

Con with no es necesario:
 * abrir fichero
 * hacer tratamiento
 * cerrar fichero
 With abre el fichero y lo cierra cuando se sale de su ámbito (los ':')
 
with open("fichero.txt", "r") as fichero:
    for linea in fichero:
        print(linea)
 
 =====
 ***Ejemplo de escribir líneas***
 import csv
with  open('./saludos.csv', 'w') as  fich_saludo:
	fich_saludo.***writelines***('hola estoy aquí')

with  open('./saludos.csv', 'r') as csv_fich:
	formato_csv = csv.reader(csv_fich, delimiter  =  ',')
	for reg in formato_csv:
		print(reg)

**Con diccionarios:**
import csv

with  open('./ejemplo2.csv', 'a') as  file:
	file.writelines('hola, mundo')

my_class =  dict()

with  open('./ejemplo2.csv', 'r') as csv_file:
	formato_csv = csv.reader(csv_file, delimiter  =  ',')
	for row in formato_csv:
		my_class.update({row[0]: row[1]})
		print(my_class)

*He visto que se pueden ejecutar instrucciones del sistema operativo: mkdir, rmdir, etc; importando las librerías correspondientes*

import csv
***import os*** *<-- importamos ésta*

with  open('datos.csv', 'w') as fich_datos:
	fich_datos.writelines('hola soy yo')

with  open('datos.csv', 'r') as fich_csv:
	formato_csv = csv.reader(fich_csv, delimiter  =  ',')
	for reg in formato_csv:
		print(reg)
		
***os.rename***('datos.csv', 'midato.csv')  *<-- renombrar fichero*

