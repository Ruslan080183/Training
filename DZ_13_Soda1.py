class Soda:
    def __init__(self, additive_to_water):
        self.additive_to_water = additive_to_water

    def show_my_drink(self) -> str:
        list_additive_to_carbonated_water = ["Coca - cola", "Sprite", "Fanta", "Cherry"]
        if self.additive_to_water in list_additive_to_carbonated_water:
              return print(F"Сarbonated water with taste {self.additive_to_water}")
        else:
              return print("Regular sparkling water")