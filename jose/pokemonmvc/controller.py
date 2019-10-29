from jose.pokemonmvc.model import Pokemon

class PokemonController(object):
    def __init__(self, random):
        self.random = random
    
    def random_pokemon(self):
        pokemons = self.generate_pokemons(10)
        return self.random.choice(pokemons)
    
    def _generate_random_values(self):
        attack = self.random.randint(1, 10)
        defense = self.random.randint(0, 10)
        stamina = self.random.randint(5, 10)
        return attack, defense, stamina

    def generate_pokemons(self, how_many):
        pokemons = []
        for _ in range(0,how_many):
            attack, defense, stamina = self._generate_random_values()
            pokemon = Pokemon(attack, defense, stamina, self.random)
            pokemons.append(pokemon)
        return pokemons
