import pytest


def test_rectangle_name(default_rectangle):
    name = default_rectangle.name
    assert name == "rectangle"


def test_perimeter_calculated(default_rectangle):
    perimeter = default_rectangle.perimeter
    assert perimeter == 62


def test_area_calculated(default_rectangle):
    area = default_rectangle.area
    assert area == 220


def test_sum_calculated_area(default_rectangle, default_circle):
    summation = default_rectangle.add_area(default_circle)
    assert summation == 248


def test_non_sum_calculated_area(default_rectangle):
    """Area of circle can't added other classes"""

    class Word:
        pass

    with pytest.raises(Exception):
        default_rectangle.add_area(Word())
