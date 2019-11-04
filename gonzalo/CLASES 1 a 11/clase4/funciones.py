
def greetings(person, print_me):
    if print_me:
        name = person['name']
        age = person['age']
        print(f'hola {name} tienes {age} años')
    else:
        print('lalalala')

#greetings('pepi')
#greetings('juli')

greetings({'name':'jose', 'age': 36}, 'N')

