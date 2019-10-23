def escribir_anno():
    anno = int(input("Escribe el año de cuatro cifras, desde 1582 a 2020: "))
    return anno

def validar_anno(anno):
    if not(anno <= 2020 and anno >= 1582):
        raise Exception

def es_bisiesto(anno):
    if anno % 4 == 0:
        return True
    return False

def escribir_mes():
    mes = int(input("Escribe el mes: "))
    return mes

def validar_mes(mes):
    if mes > 12 or mes < 1:
        raise Exception

def escribir_dia():
    dia = int(input("Escribe el día: "))
    return dia

def validar_dia(bisiesto, dia, mes):
    meses = [31,28,31,30,31,30,31,31,30,31,30,31]
    if bisiesto == True:
       meses[1] = 29

    dias_mes_introducido = int(meses[mes-1])
    if dia > dias_mes_introducido:
        raise Exception

    return dias_mes_introducido

def calcular_dia_juliano(dia, mes, bisiesto):
    meses = [31,28,31,30,31,30,31,31,30,31,30,31]
    if bisiesto == True:
       meses[1] = 29

    meses_anteriores = meses[:mes-1]

    suma_dias_hasta_la_fecha =  sum(meses_anteriores) + dia

    return suma_dias_hasta_la_fecha


# -------------------------------------------------------

def main():

    # ==== AÑO
    try:
        anno = escribir_anno()
        tratar_anno = False
    except:
        print('Escribe el año en formato numérico')
        main()
    try:
        validar_anno(anno)
    except:
        print('El año ha de estar entre 1582 y 2020')
        main()

    # ==== MES
    try:
        mes = escribir_mes()
    except:
        print('Escribe el mes en formato numérico')
        main()
    try:
        validar_mes(mes)
    except:
        print('El mes ha de estar entre 1 y 12')
        main()

    # ==== DÍA
    try:
        dia = escribir_dia()
    except:
        print('Escribe el día en formato numérico')
        main()
    try:
        dias_de_ese_mes = validar_dia(es_bisiesto(anno), dia, mes)
    except:
        print('No es un día de mes válido')
        main()



    # Fecha juliana
    dia_juliano = calcular_dia_juliano(dia, mes, es_bisiesto(anno))
    print(f'El dia juliano es: {dia_juliano}')

    return

# =============================================================================================

main()

