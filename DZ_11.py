class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def building(self):
        a1 = [self.a, self.b, self.c]
        if sum(a1) - max(a1) > max(a1):
            return print("Building a triangle is possible")
        else:
            return print("Building a triangle is not possible")

class Triangle1:
        def __init__(self, sides_triangle):
            self.sides_triangle = sides_triangle

        def building(self):
            a = self.sides_triangle[0]
            b = self.sides_triangle[1]
            c = self.sides_triangle[2]
            if sum(self.sides_triangle) - max(self.sides_triangle) > max(self.sides_triangle):
                return print("Building a triangle is possible")
            else:
                return print("Building a triangle is not possible")













