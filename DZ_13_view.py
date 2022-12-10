from DZ_13_triangle import perimeter_triangle_calculation, square_triangle_calculation
from DZ_13_rectangle import perimeter_restangle_calculation, square_restangle_calculation
from DZ_13_circle import perimeter_circle_calculation, square_circle_calculation
def output_of_results() -> dict:
    output_of_results_dict ={"Triangle": {"Square triangle": square_triangle_calculation, "Perimeter triangle": perimeter_triangle_calculation},
                             "Restangle": {"Square restangle": square_restangle_calculation, "Perimeter restangle": perimeter_restangle_calculation},
                             "Circle": {"Square circle ": square_circle_calculation, "Perimeter circle ": perimeter_circle_calculation}}
    return print(output_of_results_dict)
output_of_results()