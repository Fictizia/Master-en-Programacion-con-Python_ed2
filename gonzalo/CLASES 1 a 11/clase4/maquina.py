limite_unidades_articulo= False
error_num_articulo      = True

num_veces_compra_articulo_1 = 0
num_veces_compra_articulo_2 = 0
num_veces_compra_articulo_3 = 0
num_veces_compra_articulo_4 = 0
num_veces_compra_articulo_5 = 0
num_veces_compra_articulo_6 = 0
num_veces_compra_articulo_7 = 0
num_veces_compra_articulo_8 = 0
num_veces_compra_articulo_9 = 0
num_veces_compra_articulo_10 = 0
num_veces_compra_articulo_11 = 0
num_veces_compra_articulo_12 = 0


print(" ##########  MÁQUINA   EXPENDEDORA  #############")
print(" # -------------------------------------------- #")
print(" ##########  OPCIONES de ARTÍCULOS  #############")
print(" # -------------------------------------------- #")
print(" # --> 1  : Cerveza SIN alcohol ------------ 1€ #")
print(" # --> 2  : Cerveza CON alcohol ------------ 1€ #")
print(" # --> 3  : Almendras ---------------------- 2€ #")
print(" # --> 4  : Sanguis vegetal ---------------- 3€ #")
print(" # --> 5  : Sanguis de atún ---------------- 3€ #")
print(" # --> 6  : Sanguis de chorizo ------------- 3€ #")
print(" # --> 7  : Sanguis de queso --------------- 2€ #")
print(" # --> 8  : Sanguis de salchichón ---------- 2€ #")
print(" # --> 9  : Sanguis ensaladilla rusa ------- 4€ #")
print(" # --> 10 : Sanguis ensaladilla yanki ------ 4€ #")
print(" # --> 11 : Cacahuetes --------------------- 3€ #")
print(" # --> 12 : Chuches variados   ------------- 3€ #")
print(" # -------------------------------------------- #")
print(" # A continuación:                              #")
print(" #  * PRIMERO escriba su crédito                #")
print(" #  * DESPUÉS elija el NÚMERO del artículo      #")
print(" #    que desea                                 #")
print(" # -------------------------------------------- #")
print(" # Puede seguir pidiendo artículos hasta que:   #")
print(" #  - se le acabe el crédito                    #")
print(" #  - escriba la palabra 'STOP' ó 'stop'        #")
print(" # -------------------------------------------- #")
print(" # Cada opción tiene diez unidades del artículo #")
print(" # Si se acaban puede elegir otro artículo      #")
print(" ################################################")

credito = input('ESCRIBE el crédito que tienes  $>>: ')

credito_num = int(credito)

while True:
    numero_articulo = input('ESCRIBE el número del artículo  $>>: ')

    if numero_articulo == 'STOP' or  numero_articulo == 'stop':
        break
    if credito_num == 0:
        print(" Se ha quedado sin crédito - Hasta luego ")
        break

    credito_antes_compra = credito_num

    if  numero_articulo == '1':
        precio_articulo_elegido = 1
        num_veces_compra_articulo_1 = num_veces_compra_articulo_1 + 1
    elif numero_articulo == '2':
        precio_articulo_elegido = 1
        num_veces_compra_articulo_2 = num_veces_compra_articulo_2 + 1        
    elif numero_articulo == '3':
        precio_articulo_elegido = 2
        num_veces_compra_articulo_3 = num_veces_compra_articulo_3 + 1        
    elif numero_articulo == '4':
        precio_articulo_elegido = 3
        num_veces_compra_articulo_4 = num_veces_compra_articulo_4 + 1        
    elif numero_articulo == '5':
        precio_articulo_elegido = 3
        num_veces_compra_articulo_5 = num_veces_compra_articulo_5 + 1        
    elif numero_articulo == '6':
        precio_articulo_elegido = 3
        num_veces_compra_articulo_6 = num_veces_compra_articulo_6 + 1        
    elif numero_articulo == '7':
        precio_articulo_elegido = 2
        num_veces_compra_articulo_7 = num_veces_compra_articulo_7 + 1        
    elif numero_articulo == '8':
        precio_articulo_elegido = 2
        num_veces_compra_articulo_8 = num_veces_compra_articulo_8 + 1        
    elif numero_articulo == '9':
        precio_articulo_elegido = 4
        num_veces_compra_articulo_9 = num_veces_compra_articulo_9 + 1        
    elif numero_articulo == '10':
        precio_articulo_elegido = 4
        num_veces_compra_articulo_10 = num_veces_compra_articulo_10 + 1        
    elif numero_articulo == '11':
        precio_articulo_elegido = 3
        num_veces_compra_articulo_11 = num_veces_compra_articulo_11 + 1        
    elif numero_articulo == '12':
        precio_articulo_elegido = 3
        num_veces_compra_articulo_12 = num_veces_compra_articulo_12 + 1
    else:
        error_num_articulo = True
        print(" Elija un número del 1 al 12 ")


    credito_num = credito_num - precio_articulo_elegido
    if credito_num < 0 and error_num_articulo == False:
        credito_num = credito_antes_compra
        print(" No le queda crédito suficiente para adquirir ese artículo ")
    

    if      numero_articulo == '1' and num_veces_compra_articulo_1 > 10:
        limite_unidades_articulo_1 = True
        credito_num = credito_antes_compra
        print(" Ya ha agotado las 10 unidades del artículo 1 - Elija otro o escriba 'STOP'/'stop' para finalizar")
    elif    numero_articulo == '2' and num_veces_compra_articulo_2 > 10:
        limite_unidades_articulo_2 = True
        credito_num = credito_antes_compra
        print(" Ya ha agotado las 10 unidades del artículo 2 - Elija otro o escriba 'STOP'/'stop' para finalizar")
    elif    numero_articulo == '3' and num_veces_compra_articulo_3 > 10:
        limite_unidades_articulo_3 = True
        credito_num = credito_antes_compra
        print(" Ya ha agotado las 10 unidades del artículo 3 - Elija otro o escriba 'STOP'/'stop' para finalizar")        
    elif    numero_articulo == '4' and num_veces_compra_articulo_4 > 10:
        limite_unidades_articulo_4 = True
        credito_num = credito_antes_compra
        print(" Ya ha agotado las 10 unidades del artículo 4 - Elija otro o escriba 'STOP'/'stop' para finalizar")        
    elif    numero_articulo == '5' and num_veces_compra_articulo_5 > 10:
        limite_unidades_articulo_5 = True
        credito_num = credito_antes_compra
        print(" Ya ha agotado las 10 unidades del artículo 5 - Elija otro o escriba 'STOP'/'stop' para finalizar")        
    elif    numero_articulo == '6' and num_veces_compra_articulo_6 > 10:
        limite_unidades_articulo_6 = True
        credito_num = credito_antes_compra
        print(" Ya ha agotado las 10 unidades del artículo 6 - Elija otro o escriba 'STOP'/'stop' para finalizar")        
    elif    numero_articulo == '7' and num_veces_compra_articulo_7 > 10:
        limite_unidades_articulo_7 = True
        credito_num = credito_antes_compra
        print(" Ya ha agotado las 10 unidades del artículo 7 - Elija otro o escriba 'STOP'/'stop' para finalizar")
    elif    numero_articulo == '8' and num_veces_compra_articulo_8 > 10:
        limite_unidades_articulo_8 = True
        credito_num = credito_antes_compra
        print(" Ya ha agotado las 10 unidades del artículo 8 - Elija otro o escriba 'STOP'/'stop' para finalizar")        
    elif    numero_articulo == '9' and num_veces_compra_articulo_9 > 10:
        limite_unidades_articulo_9 = True
        credito_num = credito_antes_compra
        print(" Ya ha agotado las 10 unidades del artículo 9 - Elija otro o escriba 'STOP'/'stop' para finalizar")        
    elif    numero_articulo == '10' and num_veces_compra_articulo_10 > 10:
        limite_unidades_articulo_10 = True
        credito_num = credito_antes_compra
        print(" Ya ha agotado las 10 unidades del artículo 10 - Elija otro o escriba 'STOP'/'stop' para finalizar")        
    elif    numero_articulo == '11' and num_veces_compra_articulo_11 > 10:
        limite_unidades_articulo_11 = True
        credito_num = credito_antes_compra
        print(" Ya ha agotado las 10 unidades del artículo 11 - Elija otro o escriba 'STOP'/'stop' para finalizar")        
    elif    numero_articulo == '12' and num_veces_compra_articulo_12 > 10:
        limite_unidades_articulo_12 = True
        credito_num = credito_antes_compra
        print(" Ya ha agotado las 10 unidades del artículo 12 - Elija otro o escriba 'STOP'/'stop' para finalizar")        


    print(" Crédito restante: ", credito_num)
