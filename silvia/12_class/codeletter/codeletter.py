# crear una función que espera como parámetro un texto
# el texto vendrá de un archivo de texto
# pasar el texto a mayúsculas
# pasar cada caracter a la posición que ocupa en el diccionario

import string

ALPHABET = string.ascii_uppercase

def position(letter):
    try:
        letter_position = ALPHABET.index(letter) + 1
    except ValueError:
        return 0
    return letter_position

with open('./silvia/12_class/codeletter/mytext.txt', 'r') as file:
    text = file.read()
    shift_text = text.upper()
    final_text = [position(letter) for letter in shift_text] # esto nos dará una lista
    print(final_text)
    # for letter in shift_text:
    #     print(position(letter))
