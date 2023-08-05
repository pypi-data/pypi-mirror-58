#!/usr/bin/env python

from parser import *

print frequency('45.0')
print frequency('5daHz')
print frequency('5EHz')
print wavelength('5007')

print csv_int_list('*')
print csv_int_list('1')
print csv_int_list('10~12,1,2,5~8')
print csv_baseline_list('1-2,1-3,1-5~7,2~3-4~5')

