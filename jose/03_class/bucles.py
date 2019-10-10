# DO WHILE

number = 1
three_multiples = list()

while number <= 100:    
    if number % 3 == 0 and number % 2 == 0:
        three_multiples.append(number)
    number += 1
    if len(three_multiples) == 10:
        break

print(three_multiples)
print(len(three_multiples))

