# -*- coding: utf-8 -*-

"""
To upload to PyPI, PyPI test, or a local server:
python setup.py bdist_wheel upload -r <server_identifier>
"""

import setuptools
from distutils.core import setup, Extension
import numpy.distutils.misc_util

setuptools.setup(
    name="nionswift_segmentation",
    version="0.0.2",
    author="Ning wang",
    author_email="nwang@mpie.de",
    description="Description.",
    long_description=open("README.rst").read(),
    url="https://github.com/NingWang1990/segmentation_nionswift_plugin",
    ext_modules=[Extension("_stemdescriptor", ["nion/segmentation/_stemdescriptor.c", "nion/segmentation/calculate_descriptor.c"],
                   depends=['nion/segmentation/calculatedescriptor.h'],extra_compile_args=['-fopenmp'])],
    include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs(),
    packages=["nionswift_plugin.nion_segmentation","nion.segmentation"],
    license='GPLv3',
    include_package_data=True,
    python_requires='~=3.5',
    zip_safe=False,
)
