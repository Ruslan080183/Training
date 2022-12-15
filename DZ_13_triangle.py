from math import sqrt
def perimeter_triangle(a, b, c: float) -> float:
    perimeter_triangle_calculation = a + b + c
    return F"{perimeter_triangle_calculation} cm"

def square_triangle(a, b, c: float) -> float:
    p = a + b + c / 2
    square_triangle_calculation = round(sqrt(p * (p-a) * (p- b) * (p-c)), 2)
    return F"{square_triangle_calculation} cm"











