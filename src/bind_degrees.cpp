#include "bind_degrees.hpp"

#include <pybind11/pybind11.h>

#include <libnest2d/libnest2d.hpp>

#include "common.hpp"

namespace py = pybind11;

namespace libnest2dpy {
using namespace libnest2d;
void bind_degrees(py::module &m) {
  py::class_<Degrees, Double>(m, "Degrees").def(py::init<>(), CG_RELEASE);
}
}  // namespace libnest2dpy