class Paco:
    def __init__(self, estatura, belleza, fuerza):
        self.estatura = estatura
        self.belleza = belleza
        self.fuerza = fuerza

    def cargar(self, el_que, el_donde):
        if self.fuerza > 10:
            print(f'cargando {el_que} en el {el_donde}')
            self.fuerza -= 1
        else:
            print('no tengo fuerza suficiente')

paquito = Paco('bajo', 'feo', 12)
paquito.cargar('latex', 'cargador')
paquito.cargar('latex', 'cargador')
paquito.cargar('latex', 'cargador')