from typing import ClassVar, Iterable, Iterator

from typing import overload


class Degrees:

    @overload
    def __init__(self, val: float = ...) -> None:
        ...

    @overload
    def __init__(self, rads) -> None:
        ...

    def __float__(self) -> float:
        ...


class IntPoint:
    __hash__: ClassVar[None] = ...
    x: int
    y: int

    def __init__(self, x: int = ..., y: int = ...) -> None:
        ...

    def __eq__(self, arg0: IntPoint) -> bool:
        ...

    def __ne__(self, arg0: IntPoint) -> bool:
        ...


class Path:
    __hash__: ClassVar[None] = ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, arg0: Path) -> None:
        ...

    @overload
    def __init__(self, arg0: Iterable) -> None:
        ...

    def append(self, x: IntPoint) -> None:
        ...

    def clear(self) -> None:
        ...

    def count(self, x: IntPoint) -> int:
        ...

    @overload
    def extend(self, L: Path) -> None:
        ...

    @overload
    def extend(self, L: Iterable) -> None:
        ...

    def insert(self, i: int, x: IntPoint) -> None:
        ...

    @overload
    def pop(self) -> IntPoint:
        ...

    @overload
    def pop(self, i: int) -> IntPoint:
        ...

    def remove(self, x: IntPoint) -> None:
        ...

    def __bool__(self) -> bool:
        ...

    def __contains__(self, x: IntPoint) -> bool:
        ...

    @overload
    def __delitem__(self, arg0: int) -> None:
        ...

    @overload
    def __delitem__(self, arg0: slice) -> None:
        ...

    def __eq__(self, arg0: Path) -> bool:
        ...

    @overload
    def __getitem__(self, s: slice) -> Path:
        ...

    @overload
    def __getitem__(self, arg0: int) -> IntPoint:
        ...

    def __iter__(self) -> Iterator:
        ...

    def __len__(self) -> int:
        ...

    def __ne__(self, arg0: Path) -> bool:
        ...

    @overload
    def __setitem__(self, arg0: int, arg1: IntPoint) -> None:
        ...

    @overload
    def __setitem__(self, arg0: slice, arg1: Path) -> None:
        ...


class PathList:
    __hash__: ClassVar[None] = ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, arg0: PathList) -> None:
        ...

    @overload
    def __init__(self, arg0: Iterable) -> None:
        ...

    def append(self, x: Path) -> None:
        ...

    def clear(self) -> None:
        ...

    def count(self, x: Path) -> int:
        ...

    @overload
    def extend(self, L: PathList) -> None:
        ...

    @overload
    def extend(self, L: Iterable) -> None:
        ...

    def insert(self, i: int, x: Path) -> None:
        ...

    @overload
    def pop(self) -> Path:
        ...

    @overload
    def pop(self, i: int) -> Path:
        ...

    def remove(self, x: Path) -> None:
        ...

    def __bool__(self) -> bool:
        ...

    def __contains__(self, x: Path) -> bool:
        ...

    @overload
    def __delitem__(self, arg0: int) -> None:
        ...

    @overload
    def __delitem__(self, arg0: slice) -> None:
        ...

    def __eq__(self, arg0: PathList) -> bool:
        ...

    @overload
    def __getitem__(self, s: slice) -> PathList:
        ...

    @overload
    def __getitem__(self, arg0: int) -> Path:
        ...

    def __iter__(self) -> Iterator:
        ...

    def __len__(self) -> int:
        ...

    def __ne__(self, arg0: PathList) -> bool:
        ...

    @overload
    def __setitem__(self, arg0: int, arg1: Path) -> None:
        ...

    @overload
    def __setitem__(self, arg0: slice, arg1: PathList) -> None:
        ...


class Polygon:
    contour: Path
    holes: PathList

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, cont: Path, holes: PathList) -> None:
        ...

    @overload
    def __init__(self, cont: Path) -> None:
        ...


class Radians:

    @overload
    def __init__(self, degs: Degrees) -> None:
        ...

    @overload
    def __init__(self, val: float = ...) -> None:
        ...

    def __float__(self) -> float:
        ...
