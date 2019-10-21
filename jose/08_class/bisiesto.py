def escribir_anno():
    anno = input("ES año bisiesto? - Escribe el año: ")
    return int(anno)

def es_bisiesto(anno):
    if anno % 4 == 0:
        return True
    return False

anno = escribir_anno()
if es_bisiesto(anno):
    print("Si es bisiesto")
else:
    print("No es bisiesto")
