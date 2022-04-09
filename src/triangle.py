from src.figure import Figure
import math


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.name = "triangle"
        self.__a = a
        self.__b = b
        self.__c = c
        if a >= b + c or b >= a + c or c >= a + b:
            raise ValueError("Triangle not created!")

    @property
    def perimeter(self):
        return self.__a + self.__b + self.__c

    @property
    def area(self):
        return math.sqrt(self.perimeter / 2 * (self.perimeter / 2 - self.__a) * (self.perimeter / 2 - self.__b) * (
                self.perimeter / 2 - self.__c))
