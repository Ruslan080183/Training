from math import pi
def perimeter_circle(radius: float) -> float:
    global perimeter_circle_calculation
    perimeter_circle_calculation = round((2 * pi * radius), 2)
    return F"{perimeter_circle_calculation} cm"
perimeter_circle(3.16)




def square_circle(radius: float) -> float:
    global square_circle_calculation
    square_circle_calculation = round((pi * radius ** 2), 2)
    return F"{square_circle_calculation} cm"
square_circle(3.16)
