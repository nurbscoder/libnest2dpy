#include <pybind11/pybind11.h>

#define CG_RELEASE pybind11::call_guard<pybind11::gil_scoped_release>()
