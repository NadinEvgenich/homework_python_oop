from src.figure import Figure


class Square(Figure):
    def __init__(self, h):
        self.name = "square"
        self.__h = h

    @property
    def perimeter(self):
        return self.__h * 4

    @property
    def area(self):
        return self.__h * 2
