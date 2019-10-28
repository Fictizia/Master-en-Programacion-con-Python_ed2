class CocheController(object):
    def __init__(self, coche):
        self.coche = coche
    
    def choose(self, number):
        if number == 1:
            self.coche.imprime_coche_uno()
        else:
            self.coche.imprime_coche_dos()        
    