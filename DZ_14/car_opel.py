from car import Car

class Opel(Car):
    def __init__(self, car_name, car_mileage,car_year, car_price):
        Car.__init__(self, car_name, car_mileage,car_year, car_price)
    @staticmethod
    def country_of_car_production():
      print("This car brand Opel")



