#include "bind_geometries.hpp"

#include <pybind11/operators.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl_bind.h>

#include <libnest2d/libnest2d.hpp>

#include "libnest2dpy.hpp"

namespace py = pybind11;

namespace libnest2dpy {
using namespace libnest2d;
using namespace ClipperLib;
void bind_geometries(py::module& m) {
  py::class_<IntPoint>(m, "IntPoint")
      .def(py::init<cInt, cInt>(), py::arg("x") = 0, py::arg("y") = 0,
           CG_RELEASE)
      .def_readwrite("x", &IntPoint::X)
      .def_readwrite("y", &IntPoint::Y)
      .def(py::self == py::self, CG_RELEASE)
      .def(py::self != py::self, CG_RELEASE);
  py::bind_vector<std::vector<IntPoint>>(m, "Path");
}
}  // namespace libnest2dpy