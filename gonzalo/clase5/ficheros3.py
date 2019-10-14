import json

data = dict()

#with open('./jose/constants/clase.json', 'r') as json_file:

with open('clase.json', 'r') as json_file:
    data = json.load(json_file) 

while open('clase.json', 'w'):
    my_data.update({'piton':'mola'})
    new_data = json.dumps(my_data)
    json_file.write(my_data)

print(my_data)

