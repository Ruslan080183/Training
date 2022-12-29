class Snow:
    def __init__(self, number_of_snowflakes: int):
        self.number_of_snowflakes = number_of_snowflakes
    def __add__(self, other):
        self.number_of_snowflakes += other
    def __sub__(self, other):
        self.number_of_snowflakes -= other
    def __mul__(self, other):
        self.number_of_snowflakes *= other
    def __truediv__(self, other):
        self.number_of_snowflakes /= other
    def get_makeSnow(self, number_of_row: int):
        rows_count = self.number_of_snowflakes // number_of_row
        last_snowflakes = self.number_of_snowflakes - rows_count * number_of_row
        for _ in range(rows_count):
            print("*" * number_of_row)
        print(last_snowflakes * "*")
