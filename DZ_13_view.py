from DZ_13_triangle import perimeter_triangle, square_triangle
from DZ_13_rectangle import perimeter_restangle, square_restangle
from DZ_13_circle import perimeter_circle, square_circle
def output_of_results() -> dict:
    output_of_results_dict ={"Triangle": {"Square triangle": square_triangle(), "Perimeter triangle": perimeter_triangle()},
                             "Restangle": {"Square restangle": square_restangle(), "Perimeter restangle": perimeter_restangle()},
                             "Circle": {"Square circle ": square_circle(), "Perimeter circle ": perimeter_circle()}}
    return print(output_of_results_dict)
