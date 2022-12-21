class Snow:

    def __init__(self, number_of_snowflakes: int):
        self.number_of_snowflakes = number_of_snowflakes
    def get_stacking_snowflakes(self):
        n = int(input("Enter number:"))
        stacking_snowflakes = ("*" * self.number_of_snowflakes) + ("*" * n)
        return stacking_snowflakes
    def get_subtraction_of_snowflakes(self):
        n2 = int(input("Enter number:"))
        subtraction_of_snowflakes = "*" * (self.number_of_snowflakes - n2)
        return subtraction_of_snowflakes
    def get_snowflake_multiplication(self):
        n3 = int(input("Enter number:"))
        snowflake_multiplication = ("*" * self.number_of_snowflakes) * n3
        return snowflake_multiplication
    def get_division_of_snowflakes(self):
        n4 = int(input("Enter number:"))
        division_of_snowflakes = ("*" * (self.number_of_snowflakes // n4))
        return division_of_snowflakes

    def get_makeSnow(self, number_of_row: int):
        self.number_of_row = number_of_row
        c = "\n"
        a = "*" * self.number_of_snowflakes
        return print(F"{(a[0:self.number_of_row] + c )  * (self.number_of_snowflakes // self.number_of_row)}")

