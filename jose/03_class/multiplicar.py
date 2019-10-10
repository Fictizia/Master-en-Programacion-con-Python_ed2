multiplicando = 1 # llegar a 5
multiplicador = 1 # llegar a 10

while multiplicando <= 5:
    while multiplicador <= 10:
        print(f'{multiplicando} x {multiplicador} = {multiplicando * multiplicador}')
        multiplicador += 1
    print('------------')
    multiplicando += 1
    multiplicador = 1