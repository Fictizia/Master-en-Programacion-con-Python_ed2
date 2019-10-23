name = 'jose'
friend_list = ['Alberto', 'Silvia', 'Gonzalo']

my_dict = {'name': name,
            'age': 30,
            'friends': friend_list,
            }

print(my_dict)
my_key = 'name'
print(f'Me llamo {my_dict[my_key]}')

other_dict = my_dict
other_dict['age'] = 35

print(id(other_dict)) # -> Tienen el mismo hash. Apuntan al mismo lugar de la memoria
print(id(my_dict)) # -> Tienen el mismo hash. Apuntan al mismo lugar de la memoria

handsome = my_dict.get('handsome', False) # False, porque no existe esta clave

if not handsome:
    my_dict.update({'handsome': True})# lo mismo que my_dict['handsome'] = True. La primera forma es más correcta

print(my_dict)