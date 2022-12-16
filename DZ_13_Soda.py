class Soda:
    def show_my_drink() -> str:
        list_additive_to_carbonated_water = ["Coca - cola", "Sprite", "Fanta", "Cherry"]
        additive_to_water = input("Enter the supplement:")
        if additive_to_water in list_additive_to_carbonated_water:
            return print(F"Сarbonated water with taste {additive_to_water}")
        else:
            return print("Regular sparkling water")



