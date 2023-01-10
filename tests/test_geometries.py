import pytest as pyt
from libnest2dpy import IntPoint, Path


def test_int_point_initializer() -> None:
    int_point = IntPoint(3, 9)
    assert int_point.x == 3
    assert int_point.y == 9


def test_path_initialization() -> None:
    path = Path([IntPoint(5, 3), IntPoint(4, 7), IntPoint(99, 3)])
    assert path[1] == IntPoint(4, 7)
