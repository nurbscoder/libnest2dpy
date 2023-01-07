#include <pybind11/pybind11.h>

#include <libnest2d/libnest2d.hpp>

namespace py = pybind11;

namespace libnest2dpy {
using namespace libnest2d;
void bind_degrees(py::module &m) { py::class_<Degrees, Double>(m, "Degrees"); }
}  // namespace libnest2dpy