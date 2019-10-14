# pythonpath is the root of the project
import json

DATA_PATH = './silvia/constants/clase.json'
my_data = dict()

with open(DATA_PATH, 'r') as json_file:
    my_data = json.load(json_file)

with open(DATA_PATH, 'w') as writable_json:
    my_data.update({'Python': 'Mola'})
    new_data = json.dumps(my_data)
    json_file.write(new_data)



# from .constants.vending import items

# print(items['coca-cola']['price'])