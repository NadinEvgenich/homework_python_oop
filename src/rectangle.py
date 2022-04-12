from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, d, e):
        self.name = "rectangle"
        self.__d = d
        self.__e = e

    @property
    def perimeter(self):
        return (self.__d + self.__e) * 2

    @property
    def area(self):
        return self.__d * self.__e
