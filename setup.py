# setup cython code
import sys

try:
    from setuptools import setup, find_packages
except:
    raise RuntimeError("Cannot import setuptools \n" "python -m pip install setuptools")
    sys.exit(1)


import os
import codecs

package_root = os.path.abspath(os.path.dirname(__file__))

version = "0.01"

setup(
    name="geoinr",
    description="Open source 3D geological resource modelling",
    long_description=codecs.open("README.md", "r", "utf-8").read(),
    author="Lachlan Grose",
    author_email="lachlan.grose@monash.edu",
    license=("MIT"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "License :: Free for non-commercial use",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Graphics :: 3D Modeling",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    version=version,
    packages=find_packages(),
    keywords=[
        "earth sciences",
        "geology",
        "3-D modelling",
        "structural geology",
        "uncertainty",
    ],
)
