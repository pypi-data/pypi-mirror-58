# -*- coding: utf-8 -*

"""
Module that stores various useful constants in one convenient location.
The constants defined in this file are:

c
    the speed of light in m/s

kB
    Boltzmann's constant in Jy m^2 / K

deg2rad
    the conversion factor for degrees to radians

tpi
    :math:`2 \\pi \\sqrt{-1}`
"""

import math

__version__ = '0.2'
__revision__ = '$Rev: 2567 $'
__all__ = ['c', 'kB', 'deg2rad', 'tpi', '__version__', '__revision__', '__all__']


import warnings
warnings.warn("lsl.common.constants will be removed in LSL version 1.3.0", DeprecationWarning)


c = 2.9979245800e8			# speed of light in m/s
kB = 1380.6488				# Boltzmann's constant in Jy m^2 / K
deg2rad = math.pi / 180.0	# degrees to radians conversion
tpi = 2j*math.pi			# two pi i
