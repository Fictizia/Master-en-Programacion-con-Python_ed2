# Tiene 12 huecos
# Cada producto tiene un valor
# Tiene que restar del saldo el valor de lo que quiere
# Tiene que pedir cosas hasta que agote el crédito
# De cada producto sólo hay 10 cosas

items = {'coca-cola': {
    'price': 1,
    'quantity': 10,
},
    'manzana': {
    'price': 2,
    'quantity': 10,
},
    'fanta de naranja': {
    'price': 1,
    'quantity': 10,
},
    'agua': {
    'price': 0.70,
    'quantity': 10,
},
    'patatas': {
    'price': 1.50,
    'quantity': 10,
},
    'sandwich': {
    'price': 3,
    'quantity': 10,
},
    'chocolate': {
    'price': 2.5,
    'quantity': 10,
},
    'galleta': {
    'price': 1.25,
    'quantity': 10,
},
    'café':  {
    'price': 0.50,
    'quantity': 10,
},
    'ensalada': {
    'price': 3.50,
    'quantity': 10,
},
}

total_items = 0
for item in items:
    total_items += items[item]['quantity']
# print(total_items)

credit = int(input('¿Cuánto crédito tienes?: '))

while total_items > 0:
    choice = input('¿Qué quieres tomar?: ')

    price = items[choice]['price']
    quantity = items[choice]['quantity']

    if credit >= price and quantity > 0:
        print(
            f'Precio: {price} euros. Aquí tienes tu {choice}. \nTe quedan {round(credit - price, 2)} euros.')
        credit -= price
    elif quantity == 0:
        print(f'No hay stock de {choice}. Elige otro artículo.')
    elif credit < price:
        print(f'No tienes crédito.')
        break
    items[choice]['quantity'] -= 1
    total_items -= 1
