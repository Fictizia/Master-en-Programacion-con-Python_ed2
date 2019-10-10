name = 'jose'
frind_list = ['Alberto', 'Silvia', 'Gonzalo']

my_dict = {'name': name,
           'age': 30,
           'friends': frind_list,
            }

print(my_dict)
my_key = 'name'
print(f'Me llamo {my_dict[my_key]}')

other_dict = my_dict
other_dict['age'] = 35

print(id(other_dict))
print(id(my_dict))

handsome = my_dict.get('handsome', False)

if not handsome:
    my_dict.update({'handsome': True})

print(my_dict)

