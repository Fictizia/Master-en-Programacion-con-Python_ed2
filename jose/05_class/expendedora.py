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
    if target_has_no_money():
        exit_program()
    product = choose_product()
    if product_not_exists(product):
        exit_program()
    if not target_has_enough_money_for(product):
        exit_program()
    return_product(product)
    if target_has_money() and there_are_products():
        start()

