class Human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_older_than(my_age, other_age):
        if my_age > other_age:
            print('que viejo soy')
    
    @classmethod
    def show_the_age(cls):
        cls.is_older_than(8,1)

    def dinamic(self):
        self.show_the_age()


human = Human('random', 90)
human.dinamic()



