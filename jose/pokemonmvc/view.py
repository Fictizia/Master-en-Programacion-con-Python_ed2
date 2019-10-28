import random
from jose.pokemonmvc.controller import PokemonController

# TODO, REFACTORIZAR AL CONTROLADOR
# TODO, CREAR UNA CLASE ARBRITRO QUE AYUDE A GESTIONAR TODO ESTO

pokemon_controller = PokemonController(random)

def choose_one_pokemon(pokemons):
    print('elige un pokemon de la lista')
    for index, pokemon in enumerate(pokemons):
        print(f'{index} .- {pokemon}')
    pokemon_index = int(input(' > '))
    return pokemons[pokemon_index]

def fight(machine_pokemon, person_pokemon):
    while machine_pokemon.stamina > 0 and person_pokemon.stamina > 0:
        machine_pokemon.attack_to(person_pokemon)
        person_pokemon.attack_to(machine_pokemon)

def winner(machine_pokemon, person_pokemon):
    if machine_pokemon.stamina > person_pokemon.stamina:
        return machine_pokemon
    return person_pokemon
    
def main():
    machine_pokemon = pokemon_controller.random_pokemon()
    print(machine_pokemon)
    person_pokemons = pokemon_controller.generate_pokemons(5)
    person_pokemon = choose_one_pokemon(person_pokemons)
    print(f'has elegido {person_pokemon}')
    fight(machine_pokemon, person_pokemon)
    print('and the winner is :')
    print(winner(machine_pokemon, person_pokemon))


main()