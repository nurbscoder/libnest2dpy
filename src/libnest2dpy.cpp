#include <pybind11/pybind11.h>


namespace py = pybind11;

PYBIND11_MODULE(libnest2dpy, m)
{
    m.doc() = "Python wrapper for 2D irregular bin packaging and nesting library";
}