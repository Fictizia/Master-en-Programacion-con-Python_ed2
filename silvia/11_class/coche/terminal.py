from view import CarView
from controller import CarController
from model import Car

number = input('Give me a number from 0 to 1: ')

first_car = Car('Seat', 'Ibiza', 'Rojo')
second_car = Car('Fiat', '600', 'Blanco')
car_controller = CarController(first_car, second_car)
car_view = CarView(car_controller)
car = car_view.show_car(number)
print(car)
