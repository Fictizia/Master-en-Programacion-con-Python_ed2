class Pokemon(object):
    def __init__(self, attack, defense, stamina, random):
        self.attack = attack
        self.defense = defense
        self.stamina = stamina
        self.random = random

    def attack_to(self, enemy):
        final_attack = self.attack + self.random.randint(0,5)
        final_defense = enemy.defense + self.random.randint(0,5)
        result = final_attack - final_defense
        if result > 0:
            enemy.stamina -= result
    
    def __repr__(self):
        return f' ataque: {self.attack} \n defensa: {self.defense} \n vida: {self.stamina}'