mi_lista = [number for number in range(1,11)]

# SIN ARGS

def uno_a_uno(una_lista):
    for number in una_lista:
        print(number)
    
# uno_a_uno(mi_lista)

# CON ARGS

def uno_a_uno_con_args(*args):
    for number in args:
        print(number)

# uno_a_uno_con_args(1,2,3,4,5,6)

def deprimir_usuario(data):
    nombre = data.get('nombre')
    estado = data.get('estado')
    agotado = data.get('agotado')

    print(f'El usuario {nombre} se encuentra en {estado} y está agotado: {agotado}')


usuario = {'nombre':'Alberto', 'estado':'Black Friday', 'agotado':True}
# deprimir_usuario(usuario)

def deprimir_usuario_con_kwargs(**kwargs):
    nombre = kwargs.get('nombre')
    estado = kwargs.get('estado')
    agotado = kwargs.get('agotado')

    print(f'El usuario {nombre} se encuentra en {estado} y está agotado: {agotado}')

deprimir_usuario_con_kwargs(nombre='Alberto', estado='Black Friday', agotado=True)