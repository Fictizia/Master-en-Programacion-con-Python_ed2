class CocheController(object):
    def __init__(self, coche_primero, coche_segundo, coche_tercero, coche_cuarto):
        self.coche_primero = coche_primero
        self.coche_segundo = coche_segundo
        self.coche_tercero = coche_tercero
        self.coche_cuarto  = coche_cuarto

    def choose(self, coche_elegido):
        return coche_elegido

#        if coche_elegido == 1:
            #self.coche_primero.imprime_coche_uno()
#            return self.coche_primero
#        elif coche_elegido == 2:
#            return self.coche_segundo
#        elif coche_elegido == 3:
#            return self.coche_tercero
#        elif coche_elegido == 4:
#            return self.coche_cuarto
