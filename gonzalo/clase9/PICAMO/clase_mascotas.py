class Mascotas:

    def __init__(self, nombre, ataque, defensa, vida):
        self.nombre   = nombre
        self.ataque   = ataque
        self.defensa  = defensa
        self.vida     = vida

    def __repr__(self):
        return f' ** =>: {self.nombre.upper()}   vale {self.precio}€     y hay {self.cantidad} unidades'

# -------------------------------------------------------
# OJO:
# -------------------------------------------------------
mascota1 = Mascotas('Rusky', 10, 10, 10)   # los numeros los generaré aleatoriamente

mascota2 = Mascotas('Lusky', 10, 10, 10)  # los numeros los generaré aleatoriamente

mascota3 = Mascotas('Tuski', 10, 10, 10)   # los numeros los generaré aleatoriamente

mascota4 = Mascotas('Pusky', 10, 10, 10)   # los numeros los generaré aleatoriamente

mascota5 = Mascotas('Ansky', 10, 10, 10)   # los numeros los generaré aleatoriamente
#
# -------------------------------------------------------
