# -*- coding: utf-8 -*

"""LWA Software Library
Provided packages:
  * lsl.common
  * lsl.reader
  * lsl.writer
  * lsl.correlator
  * lsl.statistics
  * lsl.sim
  * lsl.imaging
  * lsl.misc

Provided modules:
  * lsl.astro
  * lsl.catalog
  * lsl.skymap
  * lsl.transform

See the individual package descriptions for more information.
"""

import os
import sys
import subprocess
from lsl import version
from lsl.common import paths

__version__ = '0.7'
__revision__ = '$Rev: 2383 $'
__author__ = "Jayce Dowell"


def test():
    """
    Internal test fixture
    """
    
    eggPath = os.path.split(paths.module)[0]
    testPath = os.path.join(eggPath, 'tests', 'test_lsl.py')
    subprocess.check_call([sys.executable, testPath, '-v'])

