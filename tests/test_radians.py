import math
import pytest as pyt
from libnest2dpy import Radians, Degrees

def test_degrees_to_radians() -> None:
    deg = Degrees(180)
    rad = Radians(deg)
    assert float(rad) == pyt.approx(math.pi)
