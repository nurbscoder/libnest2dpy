#ifndef _LIB2DNESTPY_HPP_
#define _LIB2DNESTPY_HPP_

#include <pybind11/pybind11.h>

#include <libnest2d/libnest2d.hpp>
#include <vector>

PYBIND11_MAKE_OPAQUE(std::vector<ClipperLib::IntPoint>);

#define CG_RELEASE pybind11::call_guard<pybind11::gil_scoped_release>()

#endif /*_LIB2DNESTPY_HPP_*/