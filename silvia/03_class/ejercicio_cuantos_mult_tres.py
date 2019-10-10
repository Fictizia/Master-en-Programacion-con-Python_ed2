counter = 1
acumulador = 0

while counter <= 100:
    if counter % 3 == 0:
        acumulador += 1
    counter += 1

print(f'Del 1 al 100 hay {acumulador} múltiplos de 3')

# Scope de las varibles