def escribir_anno():
    anno = input("ES año bisiesto? - Escribe el año: ")
    return int(anno)

def es_bisiesto(anno):
    if anno % 4 == 0:
        return True
    return False

def validar_anno(anno):
    if anno < 1582 or anno > 2020:
        raise Exception
            

def main():
     
    try:
        anno = escribir_anno()   
        # validar_anno(anno)
        if es_bisiesto(anno):
            print("Si es bisiesto")
        else:
            print("No es bisiesto")
    except ValueError:
        print('INTRODUCE EL VALOR NUMERICO SO MELON')
    
    except:
        print('Escribe un año entre 1582 y 2020')
        main()


main()