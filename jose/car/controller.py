class CarController(object):
    def __init__(self, first_car, second_car):
        self.first_car = first_car
        self.second_car = second_car

    def show_car(self, number):
        number = int(number)
        if number < 0 or number > 1:
            raise NeedNumberOneOrTwo
        if number == 0:
            return self.first_car
        return self.second_car