#include <pybind11/pybind11.h>

#include <libnest2d/libnest2d.hpp>

namespace py = pybind11;

namespace libnest2dpy {
using namespace libnest2d;
void bind_double(py::module& m) {
  py::class_<Double>(m, "Double")
      .def(py::init<>(), py::call_guard<py::gil_scoped_release>())
      .def(py::init<double>(), py::arg("val"),
           py::call_guard<py::gil_scoped_release>())
      .def("__float__",
           [](const Double& self) { return static_cast<double>(self); });
}
}  // namespace libnest2dpy