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

  py::bind_vector<std::vector<std::vector<IntPoint>>>(m, "PathList");

  py::class_<Polygon>(m, "Polygon")
      .def(py::init<>(), CG_RELEASE)
      .def(py::init<const Path&, const Paths&>(), py::arg("cont"),
           py::arg("holes"), py::keep_alive<1, 2>(), py::keep_alive<1, 3>(),
           CG_RELEASE)
      .def(py::init<const Path&>(), py::arg("cont"), CG_RELEASE)
      .def_readwrite("contour", &Polygon::Contour)
      .def_readwrite("holes", &Polygon::Holes);
}
}  // namespace libnest2dpy