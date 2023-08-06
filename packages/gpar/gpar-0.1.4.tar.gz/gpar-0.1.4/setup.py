# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from setuptools import find_packages, setup

requirements = ['numpy>=1.16',
                'torch',

                'plum-dispatch',
                'backends',
                'backends-matrix',
                'stheno',
                'varz']

setup(packages=find_packages(exclude=['docs']),
      python_requires='>=3.6',
      install_requires=requirements,
      include_package_data=True)
