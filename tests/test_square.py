import pytest


def test_square_name(default_square):
    name = default_square.name
    assert name == "square"


def test_perimeter_calculated(default_square):
    perimeter = default_square.perimeter
    assert perimeter == 40


def test_area_calculated(default_square):
    area = default_square.area
    assert area == 20


def test_sum_calculated_area(default_square, default_rectangle):
    summation = default_square.add_area(default_rectangle)
    assert summation == 240


def test_non_sum_calculated_area(default_square):
    """Area of circle can't added other classes"""

    class NonFigure:
        pass

    with pytest.raises(Exception):
        default_square.add_area(NonFigure())
