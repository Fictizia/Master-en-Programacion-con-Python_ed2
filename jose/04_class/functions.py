def greetings(person, print_me):
    if print_me:
        name = person['name']
        age = person['age']
        print(f'Hola {name} tienes {age} años')
    else:
        print('hakuna matata')

greetings({'name':'Jose', 'age': 36}, 'N')
