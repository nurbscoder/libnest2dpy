import pytest as pyt
from libnest2dpy import Degrees, Radians

def test_degrees_value() -> None:
    deg = Degrees(180)
    assert float(deg) == pyt.approx(180)

def test_radians_to_degrees() -> None:
    deg = Degrees(180)
    rad = Radians(deg)
    assert float(deg) == pyt.approx(float(Degrees(rad)))