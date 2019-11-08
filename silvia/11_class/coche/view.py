class CarView(object):
    def __init__(self, car_controller):
        self.car_controller = car_controller

    def show_car(self, number):
        return self.car_controller.show_car(number)

