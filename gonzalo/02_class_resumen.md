## Resumen clase 2ª Python ##

-**Mi chuleta para trabajar en terminal Git Bash de Windows **-
En Terminal de Git Bash:

$ pwd
/c/Users/Gonzalo

***Hago directorio para clonar el proyecto de Fictizia***
$ mkdir FICTIZIA

***Hago directorio para clonar el proyecto de gonzapython***
$ mkdir GONZAPYTHON

***Hago "clone" de cada uno, copiando previamente la url, de la página de GitHub ***(no consigo pegar o insertar el pantallazo)******

$ cd GONZAPYTHON

$ pwd
/c/Users/Gonzalo/GONZAPYTHON
 
**=*Clone de gonzapython*=**
$ git clone https://github.com/***gonzapython***/Master-en-Programacion-con-Python_ed2.git
Cloning into 'Master-en-Programacion-con-Python_ed2'...
remote: Enumerating objects: 116, done.
remote: Counting objects: 100% (116/116), done.
remote: Compressing objects: 100% (80/80), done.
remote: Total 116 (delta 38), reused 70 (delta 17), pack-reused 0
Receiving objects: 100% (116/116), 20.24 KiB | 259.00 KiB/s, done.
Resolving deltas: 100% (38/38), done.


$ cd Master-en-Programacion-con-Python_ed2

$ pwd
/c/Users/Gonzalo/GONZAPYTHON/Master-en-Programacion-con-Python_ed2

$ cd Master-en-Programacion-con-Python_ed2

$ ls
01_class.md  alberto/  example.py  gonzalo/  README.md  silvia/

$ cd ..


$ cd ..

$ cd FICTIZIA

$ ls

 ***=*Clone de Fictizia*=***
$ git clone https://github.com/***Fictizia***/Master-en-Programacion-con-Python_ed2.git
Cloning into 'Master-en-Programacion-con-Python_ed2'...
remote: Enumerating objects: 115, done.
remote: Counting objects: 100% (115/115), done.
remote: Compressing objects: 100% (83/83), done.
remote: Total 115 (delta 36), reused 67 (delta 15), pack-reused 0
Receiving objects: 100% (115/115), 21.83 KiB | 272.00 KiB/s, done.
Resolving deltas: 100% (36/36), done.

$ ls
Master-en-Programacion-con-Python_ed2/

$ cd Master-en-Programacion-con-Python_ed2

$ ls
01_class.md  alberto/  gonzalo/  jose/  Master-en-Programacion-con-Python_ed2/  README.md  silvia/

 - ***Se van 'trayendo' los nuevos ficheros con git pull***

$ cd GONZAPYTHON

$ ls
Master-en-Programacion-con-Python_ed2/

$ cd Master-en-Programacion-con-Python_ed2

$ git pull
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 4 (delta 2), reused 4 (delta 2), pack-reused 0
Unpacking objects: 100% (4/4), done.
From https://github.com/gonzapython/Master-en-Programacion-con-Python_ed2
   af61b6d..4321f8e  master     -> origin/master
Updating af61b6d..4321f8e
Fast-forward
 ***gonzalo/02_class_resumen.md*** | 81 ++++++++++++++++++++++++++++++++++++++++++---
 1 file changed, 77 insertions(+), 4 deletions(-)

 - ***Y se van 'subiendo' con el editor Visual Studio Code.***

==========================================================

Luego, la clase (muy resumida) fue:

Empezamos trabajando con programas básicos en Python

 1. caracteres y números
 2. listas (arrays) y tuplas
 3. sets :  muy interesantes, ya que se pueden hacer intersecciones, uniones y otras operaciones entre sets con gran cantidad de datos. Pueden eliminarse datos repetidos en un muestreo de muchos datos, buscar los comunes a dos conjuntos (sets), etc. Lo veo muy útil para Big Data
 4. diccionarios clave-valor  