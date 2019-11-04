import json

my_data = dict()

#with open('./jose/constants/clase.json', 'r') as json_file:
with open('clase.json', 'r') as json_file:
    my_data = json.loads(json_file) 

print(my_data)
