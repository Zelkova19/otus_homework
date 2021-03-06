import pytest

from homework2.src.Triangle import Triangle
from homework2.src.Circle import Circle
from homework2.src.Square import Square
from homework2.src.Rectangle import Rectangle


@pytest.fixture()
def class_definition_circle():
    crl = Circle(10)
    yield crl
    del crl


@pytest.fixture()
def class_definition_square():
    sqr = Square(10)
    yield sqr
    del sqr


@pytest.fixture()
def class_definition_rectangle():
    rtl = Rectangle(10, 12)
    yield rtl
    del rtl


@pytest.fixture()
def class_definition_triangle():
    tgl = Triangle(10, 11, 12)
    yield tgl
    del tgl
