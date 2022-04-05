from homework2.src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.__area = a * b
        self.__perimeter = a * 2 + b * 2
        super().__init__("Прямоугольник", self.__area, self.__perimeter)
