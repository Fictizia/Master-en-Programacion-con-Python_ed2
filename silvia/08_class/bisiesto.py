def input_year():
    year = int(input('ES año bisiesto? - Escribe el año: '))
    return year

def is_leap(year):
    if year % 4 == 0:
        return True
    return False # Evita que tenga que validar el else; sólo valida el if.

def validate_year(year):
    if year < 1582 or year > 2020:
        print('Escribe un año entre 1582 y 2020')
        return False
    return True

def main():
    year = input_year()
    if validate_year(year):
        if is_leap(year):
            print(f'{year} es bisiesto')
        else:
            print(f'{year} no es bisisesto')
    else:
        main()

main()