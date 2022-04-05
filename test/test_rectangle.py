import pytest

from src.Rectangle import Rectangle


@pytest.mark.parametrize("side_a,side_b", [(2, 3),
                                           (4, 5),
                                           (7, 10)])
def test_create_rectangle_area(side_a, side_b):
    rtl = Rectangle(side_a, side_b)
    area_rtl = rtl.area
    extended_rtl = side_a * side_b
    assert area_rtl == extended_rtl


@pytest.mark.parametrize("side_a,side_b", [(2, 3),
                                           (4, 5),
                                           (7, 10)])
def test_create_rectangle_perimeter(side_a, side_b):
    rtl = Rectangle(side_a, side_b)
    area_rtl = rtl.perimeter
    extended_rtl = side_a * 2 + side_b * 2
    assert area_rtl == extended_rtl


def test_class_definition_rectangle(class_definition_rectangle):
    status = isinstance(class_definition_rectangle, Rectangle)
    assert status


def test_add_area_rectangle(class_definition_rectangle, class_definition_square):
    area_square = class_definition_square.area
    area_rectangle = class_definition_rectangle.area
    expected_sum_area = area_square + area_rectangle
    sum_area = class_definition_rectangle.add_area(class_definition_square)
    assert sum_area == expected_sum_area
