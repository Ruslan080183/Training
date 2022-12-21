from car import Car
class Opel(Car):
    COUNTER = 0
    def __init__(self, car_name: str, car_mileage: int, car_year: int, car_price: int, car_model: str):
        self.car_name = car_name
        self.car_mileage = car_mileage
        self.car_year = car_year
        self.car_price = car_price
        self.car_model = car_model
        Opel.COUNTER += 1

    def country_of_car_production():
        print("This car brand Opel")


