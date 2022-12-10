from math import sqrt
def perimeter_triangle(a, b, c: float) -> float:
    global perimeter_triangle_calculation
    perimeter_triangle_calculation = a + b + c
    return F"{perimeter_triangle_calculation} cm"
perimeter_triangle(2.4,5.6,7.8)


def square_triangle(a, b, c: float) -> float:
    p = a + b + c / 2
    global square_triangle_calculation
    square_triangle_calculation = round(sqrt(p * (p-a) * (p- b) * (p-c)), 2)
    return F"{square_triangle_calculation} cm"
square_triangle(2.4,5.6,7.8)










