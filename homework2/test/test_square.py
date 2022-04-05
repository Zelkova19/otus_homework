import pytest

from homework2.src.Square import Square


@pytest.mark.parametrize("side", [2, 4, 7, 10])
def test_create_square_area(side):
    sqr = Square(side)
    area_sqr = sqr.area
    extended_area = side ** 2
    assert area_sqr == extended_area


@pytest.mark.parametrize("side", [2, 4, 7, 10])
def test_create_square_perimeter(side):
    sqr = Square(side)
    perimeter_sqr = sqr.perimeter
    extended_perimeter = side * 4
    assert perimeter_sqr == extended_perimeter


def test_class_definition_square(class_definition_square):
    status = isinstance(class_definition_square, Square)
    assert status


def test_add_area_square(class_definition_square, class_definition_circle):
    area_square = class_definition_square.area
    area_circle = class_definition_circle.area
    expected_sum_area = area_square + area_circle
    sum_area = class_definition_square.add_area(class_definition_circle)
    assert sum_area == expected_sum_area
