import pytest as pyt
from libnest2dpy import IntPoint, Path, PathList


def test_int_point_initializer() -> None:
    int_point = IntPoint(3, 9)
    assert int_point.x == 3
    assert int_point.y == 9


def test_path_initialization() -> None:
    path = Path([IntPoint(5, 3), IntPoint(4, 7), IntPoint(99, 3)])
    assert path[1] == IntPoint(4, 7)


def test_path_list_initialization() -> None:
    path1 = Path([IntPoint(4, 3), IntPoint(7, 8)])
    path2 = Path([IntPoint(9, 9), IntPoint(77, 989), IntPoint(777, 666)])
    path_list = PathList([path1, path2])
    assert path_list[0][1] == IntPoint(7, 8)
