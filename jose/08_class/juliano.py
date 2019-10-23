# supuesto caso, año NO bisiesto, información "curada"
# el mes se pasa como un nº entero 1, enero, 2 febrero etc...

month = int(input('Introduce el mes en formato numérico >'))
if month > 12:
    print('EL MES TIENE QUE ESTAR ENTRE 1 Y 12')
    
        

months = [31,28,31,30,31,30,31,31,30,31,30,31]


# if is_leap():
#     months[1] = 29

# previous_months = months[:month-1]

# print(sum(previous_months)+day)