def input_year():
    year = int(input('ES año bisiesto? - Escribe el año: '))
    return year

def is_leap(year):
    if year % 4 == 0:
        return True
    return False # Evita que tenga que validar el else; sólo valida el if.

year = input_year()
if is_leap(year):
    print(f'{year} es bisiesto')
else:
    print(f'{year} no es bisisesto')