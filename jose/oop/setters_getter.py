class Gato():
    def __init__(self, color, raza):
        self.color = color
        self.raza = raza
    
    def get_raza(self):
        return self.raza
    
    def get_color(self):
        return self.color

    def setter_hambre(self, valor):
        self.hambre = valor


luna = Gato('marron','vagabunda')
print(luna.get_color())
print(luna.get_raza())

luna.setter_hambre(True)
print(luna.hambre)