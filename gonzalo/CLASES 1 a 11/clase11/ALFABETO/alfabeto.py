import string

def mitexto(texto):
    texto = upper(texto)

    alfabeto = string.ascii_letters
    alfabeto_mayusculas = alfabeto[26:]

    for l in texto:
        letra_del_texto = texto[l]
        posicion_en_alfabeto = alfabeto_mayusculas.index(letra_del_texto) + 1
        print(f'Posición en el alfabeto: {i}')

#        for i in alfabeto_mayusculas:
#            letra_del_alfabeto = alfabeto_mayusculas[i]
#            if letra_del_texto == letra_del_alfabeto:
        
        
