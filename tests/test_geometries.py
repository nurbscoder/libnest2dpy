from libnest2dpy import IntPoint, Path, PathList, Polygon
import pytest as pyt


@pyt.fixture
def path1() -> Path:
    yield Path([IntPoint(4, 3), IntPoint(7, 8)])


@pyt.fixture
def path2() -> Path:
    yield Path([IntPoint(9, 9), IntPoint(77, 989), IntPoint(777, 666)])


@pyt.fixture
def path_list(path1: Path, path2: Path) -> PathList:
    yield PathList([path1, path2])


@pyt.fixture
def empty_polygon() -> Polygon:
    yield Polygon()


@pyt.fixture
def polygon_with_holes(path2: Path, path_list: PathList) -> Polygon:
    yield Polygon(path2, path_list)


@pyt.fixture
def polygon_without_holes(path1: Path) -> Polygon:
    yield Polygon(path1)


def test_int_point_initializer() -> None:
    int_point = IntPoint(3, 9)
    assert int_point.x == 3
    assert int_point.y == 9


def test_path_initialization(path1: Path) -> None:
    assert path1[1] == IntPoint(7, 8)


def test_path_list_initialization(path_list: PathList) -> None:
    assert path_list[0][1] == IntPoint(7, 8)


def test_default_polygon_has_empty_contour(empty_polygon: Polygon) -> None:
    assert len(empty_polygon.contour) == 0


def test_default_polygon_has_empty_holes(empty_polygon: Polygon) -> None:
    assert len(empty_polygon.holes) == 0


def test_polygon_contour(empty_polygon: Polygon, path1: Path) -> None:
    empty_polygon.contour = path1
    assert empty_polygon.contour == path1


def test_polygon_holes(empty_polygon: Polygon, path_list: PathList) -> None:
    empty_polygon.holes = path_list
    assert empty_polygon.holes == path_list


def test_polygon_with_holes(polygon_with_holes: Polygon, path2: Path,
                            path_list: PathList) -> None:
    assert polygon_with_holes.contour == path2
    assert polygon_with_holes.holes == path_list

def test_polygon_without_holes(polygon_without_holes: Polygon, path1: Path) -> None:
    assert polygon_without_holes.contour == path1
    assert len(polygon_without_holes.holes) == 0
