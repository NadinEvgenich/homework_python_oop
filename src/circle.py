from src.figure import Figure
import math


class Circle(Figure):
    def __init__(self, r):
        self.name = "circle"
        self.__r = r

    @property
    def perimeter(self):
        return int(self.__r * math.pi * 2)

    @property
    def area(self):
        return int(math.pi * (self.__r ** 2))
