# pythonpath is the root of the project
import json

DATA_PATH = './jose/constants/clase.json'
my_data = dict()

with open('./jose/constants/clase.json', 'r') as json_file:
    my_data = json.load(json_file)
    
with open(DATA_PATH, 'w') as writable_json:   
    my_data.update({'Python':'Mola'})
    new_data = json.dumps(my_data)
    writable_json.write(new_data)




