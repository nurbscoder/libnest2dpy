#include "libnest2dpy.hpp"

#include <pybind11/pybind11.h>

#include "bind_degrees.hpp"
#include "bind_geometries.hpp"
#include "bind_radians.hpp"

namespace py = pybind11;

namespace libnest2dpy {

PYBIND11_MODULE(_libnest2dpy, m) {
  m.doc() =
      "Internal module of python wrapper for 2D irregular bin packaging and "
      "nesting library";

  bind_degrees(m);
  bind_radians(m);
  bind_geometries(m);
}
}  // namespace libnest2dpy