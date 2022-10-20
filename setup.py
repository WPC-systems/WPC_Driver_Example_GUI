##  setup.py
##  - Build wheel file & make distribution
##
##  Copyright (c) 2022 WPC Systems Ltd.
##  All rights reserved.

## Python
import sys
import setuptools as sut

## WPC
sys.path.append('wpcsys/')
import pywpc

class BinaryDistribution(sut.dist.Distribution):
    """Distribution which always forces a binary package with platform name"""
    def has_ext_modules(x):
        return True

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    install_requires = fh.readlines()
    install_requires = [str_.rstrip(' \n') for str_ in install_requires]

sut.setup(
    name="wpcsys",
    version=pywpc.__version__,
    description='WPC Python driver APIs, the easiest way to Control & Data Acquisition (DAQ)',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author="chunglee_people, Chieh-An Lin",
    author_email="wu@wpc.com.tw",
    url="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release",

    packages=['wpcsys'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    distclass=BinaryDistribution,
    license='MIT',
    keywords='wpc, daq, driver, usb, ethernet, wifi, data acquisition',

    include_package_data=True,
    install_requires=install_requires,
    python_requires='>=3.8',
)
