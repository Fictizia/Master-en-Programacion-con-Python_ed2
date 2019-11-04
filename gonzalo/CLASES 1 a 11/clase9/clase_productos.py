class Producto:

    def __init__(self, nombre, precio, cantidad=10):
        self.nombre   = nombre
        self.precio   = precio
        self.cantidad = cantidad

    def __repr__(self):
        return f' ** =>: {self.nombre.upper()}   vale {self.precio}€     y hay {self.cantidad} unidades'


# ----------------------


print("                                         ")
print(" ======== MÁQUINA EXPENDEDORA ========== ")
print("                                         ")


pera = Producto('pera', 1)

cacahuetes = Producto('cacahuetes', 2)

chuches = Producto('chuches', 3)

cerveza = Producto('cerveza', 1.80)

cafe = Producto('cafe', 1.45)

consome = Producto('consome', 2.30)

fanta = Producto('fanta', 1.20)

sandwich = Producto('sandwich', 2.35)

