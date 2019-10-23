# supuesto caso, año NO bisiesto, información "curada"
# el mes se pasa como un nº entero, 1: enero, 2: febrero, etc.

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    if year % 4 == 0:
        return True
    return False


def check_valid_year(year):
    if year < 1582 or year > 2020:
        print('Introduce un año entre 1582 y 2020 > ')
        raise Exception


def check_valid_month(month):
    if month > 12:
        print('EL MES TIENE QUE ESTAR ENTRE 1 Y 12')
        raise Exception  # deja de ejecutar el programa


def check_valid_day(day, month, months):
    last_day = months[month-1]
    if day < 1 or day > last_day:
        print(f'Introduce un día entre 1 y {last_day}')
        raise Exception


def main():
    try:
        year = int(input('Introduce el año > '))
        check_valid_year(year)

        month = int(input('Introduce el mes en formato numérico > '))
        check_valid_month(month)

        day = int(input('Introduce el día > '))
        check_valid_day(day, month, months)

        if is_leap(year):
            months[1] = 29

        previus_months = months[:month - 1]  # empieza a contar desde 0

        print(sum(previus_months) + day)
    except:
        print('Recuerda que el programa solo acepta números enteros ')
        main()


main()
