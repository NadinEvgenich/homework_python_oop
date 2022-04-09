import pytest
from src.circle import Circle
from src.triangle import Triangle
from src.rectangle import Rectangle
from src.square import Square


@pytest.fixture
def default_circle():
    circle = Circle(3)
    yield circle
    del circle


@pytest.fixture
def default_triangle():
    triangle = Triangle(3, 4, 5)
    yield triangle
    del triangle


@pytest.fixture
def default_rectangle():
    rectangle = Rectangle(11, 20)
    yield rectangle
    del rectangle


@pytest.fixture
def default_square():
    square = Square(10)
    yield square
    del square
