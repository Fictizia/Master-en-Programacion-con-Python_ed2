class Item(object):
    def __init__(self, nombre, precio, cantidad=10):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def __repr__(self):
        return f'{self.nombre} cuesta {self.precio} y quedan {self.cantidad}'

pera = Item('Pera', 1)
manzana = Item('manzana',1)
platano = Item('platano', 1.2)
coca_cola = Item('coca cola', 2)
fanta = Item('fanta', 2)
sandwich = Item('sandwich',5)
