from math import pi
def perimeter_circle(radius: float) -> float:
    perimeter_circle_calculation = round((2 * pi * radius), 2)
    return F"{perimeter_circle_calculation} cm"

def square_circle(radius: float) -> float:
    global square_circle_calculation
    square_circle_calculation = round((pi * (radius ** 2)), 2)
    return F"{square_circle_calculation} cm"

