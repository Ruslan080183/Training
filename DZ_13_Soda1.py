class Soda:
    def __init__(self, additive_to_water: str=None):
        self.additive_to_water = additive_to_water

    def show_my_drink(self) -> str:
        if self.additive_to_water == None:
            return print("Regular sparkling water")
        else:
            return print(F"Сarbonated water with taste {self.additive_to_water}")
