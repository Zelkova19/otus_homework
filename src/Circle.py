from src.Figure import Figure


class Circle(Figure):
    def __init__(self, r):
        self.r = r
        self.__area = int(3.14 * r ** 2)
        self.__perimeter = int(2 * 3.14 * r)
        super().__init__("Круг", self.__area, self.__perimeter)
