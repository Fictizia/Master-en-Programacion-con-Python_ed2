# def greetings(name): # Declaración de la función
#    print(f'Hola, {name}')

# greetings('Silvia') # Llamada a la función

def greetings(person, print_me):
    if print_me:
        name = person['name']
        age = person['age']
        print(f'Hola {name} tienes {age} años')
    else:
        print('Hakina Matata')

greetings({'name': 'Jose', 'age': 36}, 'N') # Recibe como parámetro un diccionario