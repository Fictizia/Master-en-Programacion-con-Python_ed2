
cont = 0
tot = 0

resul = list()

while cont <= 100:
    cont += 1        
    if cont%3 == 0 and cont%2 == 0:  # pares y multiplos de 3
        resul.append(cont)
    tot += 1

if len(tot) == 10:
    break

print(resul)

    

