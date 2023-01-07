from __future__ import annotations

import os
import pathlib
import platform
import subprocess
import sys
import sysconfig
from distutils.command.build_ext import build_ext
from packaging.version import Version
from typing import Any
import re

from setuptools import Extension

CFG = "Release"


class CMakeExtension(Extension):
    name: str

    def __init__(self, name: str, sourcedir: str = "") -> None:
        super().__init__(name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class ExtensionBuilder(build_ext):
    def run(self) -> None:
        self.validate_cmake()
        super().run()

    def build_extension(self, ext: Extension) -> None:
        if isinstance(ext, CMakeExtension):
            self.build_cmake_extension(ext)
        else:
            super().build_extension(ext)

    def validate_cmake(self) -> None:
        cmake_extensions = [
            x for x in self.extensions if isinstance(x, CMakeExtension)]
        if len(cmake_extensions) > 0:
            try:
                out = subprocess.check_output(["cmake", "--version"])
            except OSError:
                raise RuntimeError(
                    "CMake must be installed to build the following extensions: "
                    + ", ".join(e.name for e in cmake_extensions)
                )
            cmake_version = Version(
                re.search(r"version\s*([\d.]+)", out.decode()).group(1))  # type: ignore
            if cmake_version < Version("3.4.0"):
                raise RuntimeError("CMake >= 3.4.0 is required")

    def build_cmake_extension(self, ext: CMakeExtension) -> None:
        cmake_args = ["-DPYTHON_EXECUTABLE=" + sys.executable]

        build_folder = (pathlib.Path(__file__).parent / "build").resolve()

        build_args = ["--config", CFG]

        if platform.system() == "Windows":
            if sys.maxsize > 2 ** 32:
                cmake_args += ["-A", "x64"]
            build_args += ["--", "/m"]
        else:
            cmake_args += ["-DCMAKE_BUILD_TYPE=" + CFG]
            build_args += ["--", "-j4"]
        cmake_args += ["-DPYTHON_INCLUDE_DIR={}".format(
            sysconfig.get_path("include"))]
        cmake_args += ["-DRP_ENABLE_DOWNLOADING=ON"]
        cmake_args += ["-DLIBNEST2D_HEADER_ONLY=OFF"]
        cmake_args += ["-DCMAKE_EXPORT_COMPILE_COMMANDS=ON"]

        env = os.environ.copy()
        env["CXXFLAGS"] = '{} -DVERSION_INFO=\\"{}\\"'.format(
            env.get("CXXFLAGS", ""), self.distribution.get_version())
        if not os.path.exists(build_folder):
            os.makedirs(build_folder)
        subprocess.check_call(["cmake", ext.sourcedir] +
                              cmake_args, cwd=build_folder, env=env)
        subprocess.check_call(["cmake", "--build", "."] +
                              build_args, cwd=build_folder)


def build(setup_kwargs: dict[str, Any]) -> None:
    cmake_modules = [CMakeExtension("_libnest2dpy", sourcedir=str(
        pathlib.Path(__file__).parent.resolve()))]

    setup_kwargs.update(
        {
            "ext_modules": cmake_modules,
            "cmdclass": dict(build_ext=ExtensionBuilder),
            "zip_safe": False,
        }
    )
