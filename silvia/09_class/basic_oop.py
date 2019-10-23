class Paco:
    def __init__(self, estatura, belleza, fuerza): # contrato con python. es lo primero que quieres que pase al definir la función
        self.estatura = estatura
        self.belleza = belleza
        self.fuerza = fuerza
    
    def cargar(self, el_que, el_donde):
        if self.fuerza > 10:
            print(f'cargando {el_que} en el {el_donde}')
            self.fuerza -= 1
        else:
            print('no tengo fuerza')

paquito = Paco('bajo', 'feo', 12)
paquito.cargar('látex','cargador')
paquito.cargar('látex','cargador')
paquito.cargar('látex','cargador')