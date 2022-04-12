import pytest
from src.triangle import Triangle


def test_triangle_name(default_triangle):
    name = default_triangle.name
    assert name == "triangle"


def test_negative_triangle_creation():
    """Check creating triangle with sum of two sides < third side"""
    with pytest.raises(Exception):
        Triangle(a=30, b=30, c=70)


def test_negative2_triangle_creation():
    """Check creating triangle with sum of two sides = third side"""
    with pytest.raises(Exception):
        Triangle(a=40, b=20, c=20)


def test_negative3_triangle_creation():
    """Check creating triangle with non sides"""
    with pytest.raises(Exception):
        Triangle(a=0, b=0, c=0)


def test_perimeter_calculated(default_triangle):
    perimeter = default_triangle.perimeter
    assert perimeter == 12


def test_area_calculated(default_triangle):
    area = default_triangle.area
    assert area == 6


def test_sum_calculated_area(default_triangle, default_square):
    summation = default_triangle.add_area(default_square)
    assert summation == 26


def test_non_sum_calculated_area(default_triangle):
    """Area of circle can't added other classes"""

    class Sign:
        pass

    with pytest.raises(Exception):
        default_triangle.add_area(Sign())
