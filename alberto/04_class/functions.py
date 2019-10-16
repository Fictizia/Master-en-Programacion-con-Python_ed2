
def greetings(person, print_me):
if print_me:
    name = person['name']
    age = person['age']
    print(f'hola {name} tienes {person}años')
else:
    print('error')

greetings({'name':'Jose', 'age':36}, 'N')
