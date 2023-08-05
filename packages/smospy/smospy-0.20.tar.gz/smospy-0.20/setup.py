#from distutils.core import setup,Extension
from setuptools import setup,Extension
import numpy
from Cython.Build import cythonize
import os
from os import path
import subprocess
from codecs import open  # To use a consistent encoding

root_dir = os.path.dirname(os.path.abspath(__file__))
c_path = path.join(root_dir,"smospy/c_functions")




# Get the long description from the relevant file
with open(path.join(root_dir, 'README'), encoding='utf-8') as f:
    long_description = f.read()

extensions = [Extension(
        name = "smospy.signal_c_lib",                                                           #name of the .so file
        sources = ["smospy/c_functions/03_signal_c.pyx","smospy/c_functions/01_signal_c.cpp"],  #cython file
        include_dirs = [numpy.get_include(),path.join(root_dir,c_path)],
        libraries = ['armadillo'],                                                              #-l option for compiler
        language = "c++",                                   #c++ flag
        extra_compile_args=['-std=c++11'],                  #force c++11
        )]

setup(
    name='smospy',
    version='0.20',
    description='strong motion seismic data analysis module for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitext.gfz-potsdam.de/alejaege/smospy',
    author='Alexander Jaeger',
    author_email='Alexander@jaeger-erfurt.de',
    license='MIT',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Cython',
        'Programming Language :: C++',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
        
    ],
    keywords=[
        'seismology, waveform analysis,geophysics,'
        ' geophysical inversion'],
    python_requires='>=3',
    #install_requires=['numpy','matplotlib','pygdal','pyshp','pandas','h5py','scipy','Cython'],
    
    packages = ['smospy'],
    
    include_package_data=True,
    package_data={
        'smospy/c_functions':
             ['01_signal_c.cpp',
             '02_signal_c.h',
             '03_signal_c.pyx',
             '04_setup.py',
             ],
    },
    ext_modules = cythonize(extensions),
    entry_points={
       'console_scripts': [
           'J_Cord_to_tiff = smospy.J_Cord_to_tiff:main',
       ],
    }
)
