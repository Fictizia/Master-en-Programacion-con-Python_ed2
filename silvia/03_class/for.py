pair_numbers = list()
for number in range(0, 10, 2):
    pair_numbers.append(number)
print(pair_numbers)

text = '''En un lugar de la Mancha de cuyo nombre no puedo acordarme
vivía un hidalgo que no me acuerdo si tenía una talla XL'''

new_text = ''

index = 0

for char in text:
    if char == 'x' or char == 'X':
        break
    index += 1

# Otra solución:
index = text.rindex('X')

print(text[0:index])

# Método split:
text1 = 'banana, pear, melon, watermelon'
my_list = text1.split(', ')

print(my_list)

shopping_list = ['mouse', 'keyboard', 'monitor', 'operating system', 'windows']

for item in shopping_list:
    print(item)

numbers = [2, 8, 7, 5, 0, 9, 22, 99]
double_numbers = list()

for number in numbers: # Para cada número dentro de la lista números
    double = number * 2
    double_numbers.append(double)
    
print(double_numbers)
    

# for number in range(0, 101, 2): # Si pones (100), va de 0 a 99. El step permite decir de cuanto en cuanto salta el número
#    print(number)