#include "bind_degrees.hpp"

#include <pybind11/pybind11.h>

#include <libnest2d/libnest2d.hpp>

#include "libnest2dpy.hpp"

namespace py = pybind11;

namespace libnest2dpy {
using namespace libnest2d;
void bind_degrees(py::module& m) {
  py::class_<Degrees>(m, "Degrees")
      .def(py::init<double>(), py::arg("val") = double{}, CG_RELEASE)
      .def(py::init<Radians>(), py::arg("rads"), CG_RELEASE)
      .def(
          "__float__",
          [](const Degrees& self) { return static_cast<double>(self); },
          CG_RELEASE);
}
}  // namespace libnest2dpy