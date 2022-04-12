import pytest


def test_circle_name(default_circle):
    name = default_circle.name
    assert name == "circle"


def test_perimeter_calculated(default_circle):
    perimeter = default_circle.perimeter
    assert perimeter == 18


def test_area_calculated(default_circle):
    area = default_circle.area
    assert area == 28


def test_sum_calculated_area(default_circle, default_triangle):
    summation = default_circle.add_area(default_triangle)
    assert summation == 34


def test_non_sum_calculated_area(default_circle):
    """Area of circle can't added other classes"""

    class Number:
        pass

    with pytest.raises(Exception):
        default_circle.add_area(Number())
