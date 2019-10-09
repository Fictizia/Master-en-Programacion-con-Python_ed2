
texto_sin_X = ' '

texto = '''En un lugar de la Mancha de cuyo nombre no puedo acordarme
vivia un hidalgo que no me acuerdo si tenia una talla XL'''

for caracter in texto: 
    
    if caracter == 'X':
        break
    else:
        texto_sin_X = texto_sin_X+caracter

print(texto_sin_X)

