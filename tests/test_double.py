import pytest as pyt

from libnest2dpy import Double


def test_type_casting() -> None:
    double_value = Double(0.3)
    assert float(double_value) == pyt.approx(0.3)