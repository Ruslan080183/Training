class Car:
    COUNTER = 0
    def __init__(self, car_name: str, car_mileage: int,car_year: int, car_price: int):
        self.car_name = car_name
        self.car_mileage = car_mileage
        self.car_year = car_year
        self.car_price = car_price
        Car.COUNTER += 1

    def __str__(self):
        return print(F" {self.car_name} {self.car_year} release , mileage - {self.car_mileage} km, "
                     F"price - {self.car_price} rubles")

    def __eq__(self, other):
        if self.car_year != other.car_year and self.car_name != other.car_name:
            return print(F"Cars {self.car_name} and {other.car_name} differ by year of manufacture and brand")
        elif self.car_year == other.car_year and self.car_name == other.car_name:
            return print(F"Cars {self.car_name} and {other.car_name} have the same year of manufacture and brand "
                         F"of manufacturer")
        elif self.car_year == other.car_year and self.car_name != other.car_name:
            return print(F"Cars {self.car_name} and {other.car_name} have the same year of manufacture, but differ "
                         F"in the make of the manufacturer")
        elif self.car_year != other.car_year and self.car_name == other.car_name:
            return print(F"Cars {self.car_name} and {other.car_name} of the same brand of manufacturer, but differ "
                         F"in the year of manufacture")

    def get_price_currency(self):
        currency = round(self.car_price / float(input("Enter the dollar to Belarusian ruble exchange rate: ")), 2)
        return print(F"The cost of a {self.car_name} in Belarusian rubles is {self.car_price},in dollars - {currency}")
    @classmethod
    def get_car_counter(cls):
        return cls.COUNTER
    @staticmethod
    def country_of_car_production(car_brand: str = None) -> str:
        producing_countries = {"Germany": ["Opel", "BMW", "Volkswagen"],
                            "France": ["Peugeot", "Citroen", "Renault"],
                            "Japan": ["Nissan", "Toyota", "Mazda"]}
        car_brand = input("Enter brand of car:")
        for i in producing_countries:
            for k in producing_countries[i]:
                if car_brand == k:
                    return print(F"Country of manufacture of the car brand {car_brand} {i}")
                else:
                    return print(F"The country of the manufacturer of the car {car_brand} is not in the list")
    @property
    def get_mileage_cars(self):
       return self.car_mileage
    @get_mileage_cars.setter
    def get_mileage_cars(self, c):
        if c > 500000:
            print("Mileage limit!!!")
            self.car_mileage = c
    @get_mileage_cars.deleter
    def get_mileage_cars(self):
         print("Delete!!!")
         del self.car_mileage







