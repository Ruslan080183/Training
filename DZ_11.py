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
        def __init__(self, x=[5, 4, 3]):
            self.x = x

        def building(self):
            if sum(self.x) - max(self.x) > max(self.x):
                return print("Building a triangle is possible")
            else:
                return print("Building a triangle is not possible")













