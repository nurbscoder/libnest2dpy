cmake_minimum_required(VERSION 3.4)
project(libnest2dpy LANGUAGES CXX)

add_subdirectory(third_party/libnest2d)
add_subdirectory(third_party/pybind11)

pybind11_add_module(libnest2dpy src/libnest2dpy.cpp)
target_link_libraries(libnest2dpy PUBLIC libnest2d)