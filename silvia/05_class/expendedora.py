def target_has_money():
    pass

def choose_product():
    pass

def product_exists():
    pass

def target_has_enough_money_for(product):
    pass

def exit_program():
    pass

def start():
    if not target_has_money(): # Check. Está en negativo porque si no se cumple, te saca del programa.
        exit_program()
    product = choose_product()
    if not product_exists():
        exit_program()
    if not target_has_enough_money_for(product):
        exit_program()
    return_product(product)
    if target_has_money and there_are_products():
        start() # Recursividad. Una función que se llama a sí misma. Hay un número máximo de recursividad.
