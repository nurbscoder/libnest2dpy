import pytest as pyt
from libnest2dpy import Degrees, Double

def test_degrees_is_derived_from_double() -> None:
    deg = Degrees()
    assert isinstance(deg, Double)
