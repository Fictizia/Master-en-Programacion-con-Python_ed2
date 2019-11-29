import requests
from flask import jsonify

print('obtengo indice')
indice = requests.get('https://swapi.co/api/')
indice = indice.json()

print('obtengo people')
people_url = indice['people'] # indice.get('people') but for not mess with get http method
people = requests.get(people_url)
people = people.json()


insert_info = jsonify({'user':'jose'}) # json format
headers_info = jsonify({'loque':'me pidan'})
result = requests.post('swapi.com/whatever',insert_info, headers=headers_info)

print(people)