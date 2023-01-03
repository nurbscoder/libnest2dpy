#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(_libnest2dpy, m)
{
    m.doc() = "Internal module of python wrapper for 2D irregular bin packaging and nesting library";
}