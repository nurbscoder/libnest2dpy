cmake_minimum_required(VERSION 3.4)
project(libnest2dpy LANGUAGES CXX)

add_subdirectory(third_party/libnest2d)
add_subdirectory(third_party/pybind11)

pybind11_add_module(libnest2dpy src/libnest2dpy.cpp)

set_target_properties(
  libnest2dpy
  PROPERTIES OUTPUT_NAME "_libnest2dpy"
             LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/libnest2dpy
             LIBRARY_OUTPUT_DIRECTORY_RELEASE
             ${CMAKE_CURRENT_SOURCE_DIR}/libnest2dpy
             LIBRARY_OUTPUT_DIRECTORY_DEBUG
             ${CMAKE_CURRENT_SOURCE_DIR}/libnest2dpy
             SKIP_BUILD_RPATH FALSE
             BUILD_WITH_INSTALL_RPATH TRUE
             INSTALL_RPATH "\$ORIGIN"
             INSTALL_RPATH_USE_LINK_PATH FALSE)

if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
  target_link_options(libnest2dpy PUBLIC -Wl,--disable-new-dtags)
endif()

target_link_libraries(libnest2dpy PUBLIC libnest2d)
