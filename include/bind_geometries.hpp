#ifndef _BIND_GEOMETRIES_HPP_
#define _BIND_GEOMETRIES_HPP_
#include <pybind11/pybind11.h>

namespace libnest2dpy {
void bind_geometries(pybind11::module &m);
}  // namespace libnest2dpy

#endif /* _BIND_GEOMETRIES_HPP_ */