import string

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'
print(ALPHABET)


def position(letter):
    try:
        letter_position = ALPHABET.index(letter) + 1
    except ValueError:
        return 0
    return letter_position

with open('./jose/katas/mytext.txt', 'r') as file:
    text = file.read()
    shift_text = text.upper()
    final_text = [position(letter) for letter in shift_text]
    print(final_text)


    