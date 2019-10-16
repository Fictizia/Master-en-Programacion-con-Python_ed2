#Necesitamos tener un stock de dinero
#Debemos tener un stock y ver que ocurre cuando lo agotas

# Ahora definimos el numero de productos que tenemos y el precio

def productos():

    producto_manzana = {'producto': 'Manzana', 'precio': 1, 'stock': 1, 'moneda': '€'}
    producto_platano = {'producto': 'Platano', 'precio': 1.25, 'stock': 2, 'moneda': '€'}
    producto_pera = {'producto': 'Pera', 'precio': 1.10, 'stock': 10, 'moneda': '€'}
    producto_patatas = {'producto': 'Patatas', 'precio': 1.5, 'stock': 10, 'moneda': '€'}
    producto_chocolatina = {'producto': 'Chocolatina', 'precio': 2, 'stock': 10, 'moneda': '€'}
    producto_coca_cola = {'producto': 'Coca-cola', 'precio': 5, 'stock': 10, 'moneda': '€'}
    
    items = [producto_manzana, producto_platano, producto_pera, producto_patatas, producto_chocolatina, producto_coca_cola]
    dinero_maquina = 0

    #Ver que productos hay disponibles y el stock + precio

    def mostrador(items):
        print ('Productos disponibles. \n***************')

        for item in items: #Recorremos el numero de productos. En este caso lo hemos llamado items
            if item.get('stock') == 0: #Aqui estamos comprobando si el producto tiene stock
                items.remove(item) # Si no tiene stock que lo elimine.
        for item in items:
            print(item.get('producto'), item.get('precio'), item.get('moneda'))
        print('***************\n')

    continuar_comrpando = True #Tenemos que permitir al sistema que siga comprando.
    dinero_maquina = int(input('Introduce tu dinero \n***************: '))
    while continuar_comrpando == True:
        if dinero_maquina > 0:
            print('Hola, elige el producto que desees. \n***************')
            mostrador(items)
            seleccionar_producto = input('¿Que producto deseas?: ')             
            for item in items:
                if seleccionar_producto == item.get('producto'):
                    print('Perfecto')
                    seleccionar_producto = item
                    precio = seleccionar_producto.get('precio')
                    if dinero_maquina - precio >0:                              
                        print('Has seleccionado  ' + seleccionar_producto.get('producto'))
                        seleccionar_producto['stock'] -= 1
                        #dinero = monedero - dinero_maquina
                        dinero_maquina -= precio
                        print('Te quedan ---> ' + str(dinero_maquina) + '€')
                        pregunta = input('¿Quieres comprar algo mas? (S/N): ')
                        if pregunta == 'N':
                            continuar_comrpando = False
                                
                            if dinero_maquina != 0:
                                print('Tu cambio ' + str(dinero_maquina) + '€' )
                                dinero_maquina = 0
                                print('Gracias por tu compra\n')
                                break
                            else:
                                print('Gracias por tu compra\n')
                                break    
                        else:
                            continue
                    else:
                        print('No se permite credito negativo')
                        break
        else:
            print('No tienes dinero')
            dinero_maquina = int(input('Introduce tu dinero \n***************: '))
            
productos()