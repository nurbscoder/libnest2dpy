cmake_minimum_required(VERSION 3.4)
project(libnest2dpy LANGUAGES CXX)

add_subdirectory(third_party/libnest2d)
add_subdirectory(third_party/pybind11)

pybind11_add_module(_libnest2dpy src/libnest2dpy.cpp)
target_link_libraries(_libnest2dpy PUBLIC libnest2d)