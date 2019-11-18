class Human():
    def __init__(self, brain, hair, license):
        self.brain = brain
        self.hair = hair
        self.license = license
         
    @property    
    def head(self):
        return self.brain and self.hair

    def can_shoot(self, func):
        if self.license:
            func()

    @can_shoot
    def shoot(self):
        print('BOOM BOOM')


jose = Human(True, True, False)
print(jose.hair)
print(jose.head)
jose.shoot()
