#ifndef _BIND_DEGREES_HPP_
#define _BIND_DEGREES_HPP_

#include <pybind11/pybind11.h>

namespace libnest2dpy {
void bind_degrees(pybind11::module &m);
}  // namespace libnest2dpy

#endif /* _BIND_DEGREES_HPP_ */