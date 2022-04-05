from homework2.src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        if not self.__existence_check(a, b, c):
            raise AttributeError("Это не треугольник")
        super().__init__('Треугольник', self.__area, self.__perimeter)

    def __existence_check(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            self.a = a
            self.b = b
            self.c = c
            self.p = (self.a + self.b + self.c) / 2
            self.__area = int((self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)) ** 0.5)
            self.__perimeter = int(self.a + self.b + self.c)
            return True
        return False
