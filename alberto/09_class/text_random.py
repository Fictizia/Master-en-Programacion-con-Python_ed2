#Randomnizar frases
#Podemos crear un documento que sea el diccionarario, una vez que lo hemos creado podemos llamarlo desde
#otro archivo con el import y que este documento solo sea una linea donde se le este llamando, del estilo frases = [frases_tipo_uno,frases_tipo_dos etc... ]
#en base a los diferentes tipos de preguntas que tengamos.


import random
from frases import frases



def texto_random(bloques_frases):
    with open('frases_2.txt', 'a+') as f:
        for _ in range(bloques_frases):        
                for bloques in range(6):
                    frase = frases[random.randint (0, 33)]
                    print('Frase:', bloques + 1, ':', frase)
                    f.write(str('Frase:' + str(bloques) + frase +'\n' '/*************'))
            
    

bloques_frases = int(input('¿Cuantos bloques de frases quieres (numero entero)? > '))
texto_random(bloques_frases)

