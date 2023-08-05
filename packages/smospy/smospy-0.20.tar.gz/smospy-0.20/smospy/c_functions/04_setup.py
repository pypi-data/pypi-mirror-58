# Cython compile instructions
# Use 
# python3 04_setup.py build_ext --inplace
# to compile

from distutils.core import setup,Extension
from Cython.Build import cythonize
import os
from os import path

setup(
  name = "signal_c_lib",
  ext_modules = cythonize(Extension(        #
        name="signal_c_lib",                     #name of the .so file
        sources=["03_signal_c.pyx","01_signal_c.cpp"],        #cython file
        
        libraries = ['armadillo'],          #-l option for compiler
        language="c++",                     #c++ flag
        )
  ))
