#include "bind_double.hpp"

#include <pybind11/pybind11.h>

#include <libnest2d/libnest2d.hpp>

#include "common.hpp"

namespace py = pybind11;

namespace libnest2dpy {
using namespace libnest2d;
void bind_double(py::module& m) {
  py::class_<Double>(m, "Double")
      .def(py::init<>(), CG_RELEASE)
      .def(py::init<double>(), py::arg("val"), CG_RELEASE)
      .def(
          "__float__",
          [](const Double& self) { return static_cast<double>(self); },
          CG_RELEASE);
}
}  // namespace libnest2dpy