class Car:
    _content = "Включение и глушение двигателя автомобиля"
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def first_launch(self):
        return f"Автомобиль заведен"
    def сar_engine_plug(self):
        return f"Автомобиль заглушен"
    def __str__(self):
        return f"Автомобиль {self.type} {self.year} года выпуска : цвет {self.color}"

auto_1 = Car(type="Фольксваген Поло", color="бордовый", year="2022")
print(auto_1)