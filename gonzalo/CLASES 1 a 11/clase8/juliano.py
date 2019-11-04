
def escribir_anno():
    anno = int(input("Escribe el año de cuatro cifras desde 1582 a 2020: "))
    return anno

def validar_anno():
    if anno > 2020 or anno< 1582:
        raise Exception
    
def escribir_mes():
    mes = int(input("Escribe el mes: "))
    return mes

def validar_mes(mes):
    if mes <= 12 and mes>= 1:
        raise Exception

def escribir_dia():
    dia = int(input("Escribe el día: "))

def validar_dia():
    meses = [31,28,31,30,31,30,31,31,30,31,30,31]
    if meses[mes] != dia:
        raise Exception


def main():
    try:
        anno = escribir_anno()
    except:
        print("Escribe el año en formato numérico")

    validar_anno(anno)

    try:
        mes = escribir_mes()
    except:
        print("Escribe el mes en formato numérico")

    validar_mes(mes)


# ---------------

main()


anno = escribir_anno()
if not validar_anno(anno):
    escribir_anno()

es_bisiesto()

escribir_mes()
if not validar_mes(anno):
    escribir_mes

dia = escribir_dia()