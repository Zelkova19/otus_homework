import pytest

from src.Circle import Circle


@pytest.mark.parametrize("radius_r", [2, 4, 7, 10])
def test_create_circle_area(radius_r):
    crl = Circle(radius_r)
    area_crl = crl.area
    extended_crl = int(3.14 * radius_r ** 2)
    assert area_crl == extended_crl


@pytest.mark.parametrize("radius_r", [2, 4, 7, 10])
def test_create_circle_perimeter(radius_r):
    crl = Circle(radius_r)
    perimeter_crl = crl.perimeter
    extended_crl = int(2 * 3.14 * radius_r)
    assert perimeter_crl == extended_crl


def test_class_definition_circle(class_definition_circle):
    status = isinstance(class_definition_circle, Circle)
    assert status


def test_add_area_circle(class_definition_circle, class_definition_triangle):
    area_circle = class_definition_circle.area
    area_triangle = class_definition_triangle.area
    expected_sum_area = area_circle + area_triangle
    sum_area = class_definition_circle.add_area(class_definition_triangle)
    assert sum_area == expected_sum_area
