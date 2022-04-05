import pytest

from homework2.src.Triangle import Triangle


@pytest.mark.parametrize("side_a,side_b,side_c", [(2, 4, 5),
                                                  (10, 10, 10),
                                                  (10, 11, 10)])
def test_create_triangle_area(side_a, side_b, side_c):
    tgl = Triangle(side_a, side_b, side_c)
    area_tgl = tgl.area
    semi_perimeter = (side_a + side_b + side_c) / 2
    extended_tgl = int((semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b)
                        * (semi_perimeter - side_c)) ** 0.5)
    assert area_tgl == extended_tgl


@pytest.mark.parametrize("side_a,side_b,side_c", [(2, 4, 5)])
def test_create_triangle_perimeter(side_a, side_b, side_c):
    tgl = Triangle(side_a, side_b, side_c)
    perimeter_tgl = tgl.perimeter
    extended_tgl = side_a + side_b + side_c
    assert perimeter_tgl == extended_tgl


def test_class_definition_triangle(class_definition_triangle):
    status = isinstance(class_definition_triangle, Triangle)
    assert status


def test_add_area_triangle(class_definition_triangle, class_definition_rectangle):
    area_triangle = class_definition_triangle.area
    area_rectangle = class_definition_rectangle.area
    expected_sum_area = area_triangle + area_rectangle
    sum_area = class_definition_triangle.add_area(class_definition_rectangle)
    assert sum_area == expected_sum_area


def test_create_not_a_triangle():
    with pytest.raises(AttributeError):
        Triangle(10, 11, 40)
