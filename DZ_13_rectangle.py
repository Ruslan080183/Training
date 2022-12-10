def perimeter_restangle(a, b: float) -> float:
    global perimeter_restangle_calculation
    perimeter_restangle_calculation = (a + b) * 2
    return F"{perimeter_restangle_calculation} cm"
perimeter_restangle(2.4,5.6)

def square_restangle(a, b: float) -> float:
    global square_restangle_calculation
    square_restangle_calculation = round((a * b),2)
    return F"{square_restangle_calculation} cm"
square_restangle(2.4,5.6)


