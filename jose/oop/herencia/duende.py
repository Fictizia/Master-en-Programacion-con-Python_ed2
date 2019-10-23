class Duende(object):
    def __init__(self, color, veces_alardeado=0, otro_algo=True):
        self.color = color
        self.veces_alardeado = veces_alardeado
        self.otro_algo = otro_algo

    
    def alardear(self):
        if self.veces_alardeado < 3:
            print('Soy un duende y no me gusta alardear mas de 3 veces')
        self.veces_alardeado += 1