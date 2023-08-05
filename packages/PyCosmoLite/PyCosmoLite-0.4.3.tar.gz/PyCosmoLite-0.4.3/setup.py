#!/usr/bin/env python

import os
import sys

from setuptools import Distribution, Extension, find_packages, setup

required = ["numpy", "sympy<1.4", "scipy>=0.14.0", "recfast4py>=0.1.1", "hope>=0.7.2",
            "Cython", "dill", "matplotlib<3", "numba"]


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        # file might not exist when package is installed as dependency:
        return ""


class BinaryDistribution(Distribution):

    """as this setup.py does not declare c code to compile, 'setup.py bdist_wheel'
    would create source wheels, unless we implement this 'fake' class and use
    it as 'distclass=BinaryDistribution' below.
    """

    def has_ext_modules(self):
        return True


def create_ext_modules():
    """
    Build commands require preinstalled numpy to compile the c extensions. A
    global "import numpy" here would break tox and also if installed as a
    dependency from another python package. So we only require numpy for the
    cases where its header files are actually needed.
    """

    build_commands = ('build', 'build_ext', 'build_py',
                      'build_clib', 'build_scripts', 'bdist_wheel',
                      'bdist_rpm', 'bdist_wininst', 'bdist_msi', 'bdist_mpkg',
                      'build_sphinx', 'develop', 'install', 'install_lib',
                      'install_header')

    ext_modules = []
    if any(command in build_commands for command in sys.argv[1:]):
        try:
            import numpy
        except ImportError:
            raise Exception(
                "please install numpy, need numpy header files to compile c extensions")

        from Cython.Build import cythonize
        cythonize("PyCosmo/cython/halo_integral.pyx")
        files = ["const.c", "main.c", "halo_integral.c", "polevl.c", "sici.c", "sicif.c",
                 "polevlf.c", "logf.c", "sinf.c", "constf.c", "mtherr.c"]
        ext_modules = [Extension("PyCosmo.cython.halo_integral",
                                 sources=["PyCosmo/cython/" + file for file in files],
                                 include_dirs=[numpy.get_include()])]
    return ext_modules


if "bdist_wheel" in sys.argv:

    package_data = {'PyCosmo': ['BoltzmannSolver/_cache/*/*.so',
                                'BoltzmannSolver/_traces/*.json',
                                'CosmologyCore.ipynb',
                                ],
                    }

else:
    package_data = {'PyCosmo': ['BoltzmannSolver/_traces/*.json',
                                'CosmologyCore.ipynb',
                               ],
                    }


setup(
    name="PyCosmoLite",
    version="0.4.3",   # no need to update version in other places of PyCosmo
    author="Adam Amara",
    author_email="adam.amara@phys.ethz.ch",
    url="http://cosmo-docs.phys.ethz.ch/PyCosmo",
    license="MIT License",
    packages=find_packages(exclude=["examples", "tests.param_files", "tests"]),
    description="A multi-purpose cosmology calculation tool",
    long_description=read("README.rst"),
    install_requires=required,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: C",
        "Topic :: Scientific/Engineering :: Astronomy",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points='''
        [console_scripts]
        trace-generator=PyCosmo.BoltzmannSolver.generator.trace_generator:main
        compute-fields=PyCosmo.compute_fields:main
        check-pycosmo-config-file=PyCosmo:check_config_file
    ''',
    distclass=BinaryDistribution,
    package_data=package_data,
    ext_modules=create_ext_modules(),
)
