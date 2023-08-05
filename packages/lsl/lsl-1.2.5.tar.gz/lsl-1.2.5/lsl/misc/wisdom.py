# -*- coding: utf-8 -*-

# Python3 compatiability
from __future__ import print_function

"""
Module for building and saving LSL-specific FFTW and PyFFTW wisdom.

.. versionadded:: 1.0.1
"""

import os
import numpy
import pickle
from datetime import datetime

from lsl.common.paths import data as dataPath
from lsl.common.busy import BusyIndicator
from lsl.misc import _wisdom


__version__ = "0.2"
__revision__ = "$Rev: 2454 $"
__all__ = ["make", "show", "__version__", "__revision__", "__all__"]


# Path to the LSL-specific FFTW wisdom file
_wisdomFilenameFFTW = os.path.join(dataPath, 'fftw_wisdom.txt')

# Path to the LSL-specific PyFFTW wisdom file
_wisdomFilenamePyFFTW = os.path.join(dataPath, 'pyfftw_wisdom.pkl')


def _makeFFTW():
    """
    Build a new set of LSL-specific FFTW wisdom.
    """
    
    bi = BusyIndicator(message="Building FFTW wisdom")
    bi.start()
    
    _wisdom.buildWisdom(_wisdomFilenameFFTW)
    
    bi.stop()
    
    return True


def _makePyFFTW():
    """
    Build a new set of LSL-specific PyFFTW wisdom.
    """
    
    MAXTRANSFORM = 262144
    
    try:
        import pyfftw
        
        bi = BusyIndicator(message="Building PyFFTW wisdom")
        bi.start()
        
        # Enable the PyFFTW cache
        if not pyfftw.interfaces.cache.is_enabled():
            pyfftw.interfaces.cache.enable()
            pyfftw.interfaces.cache.set_keepalive_time(60)
            
        fftFunction = lambda x: pyfftw.interfaces.numpy_fft.fft(x, planner_effort='FFTW_PATIENT')
        ifftFunction = lambda x: pyfftw.interfaces.numpy_fft.ifft(x, planner_effort='FFTW_PATIENT', overwrite_input=True)
        
        # Setup
        fftlen = 2
        while fftlen <= MAXTRANSFORM:
            data = numpy.ones(fftlen, dtype=numpy.complex64)
            fftFunction(data)
            ifftFunction(data)
            
            fftlen *= 2
            
        fftlen = 10
        while fftlen <= MAXTRANSFORM:
            data = numpy.ones(fftlen, dtype=numpy.complex64)
            fftFunction(data)
            ifftFunction(data)
            
            fftlen *= 10
            
        fh = open(_wisdomFilenamePyFFTW, 'wb')
        pickle.dump(pyfftw.export_wisdom(), fh)
        fh.close()
        
        bi.stop()
        
    except ImportError:
        print("PyFFTW is not installed, skipping")
        return False
        
    return True


def make(FFTW=True, PyFFTW=True):
    """
    Build a new set of LSL-specific FFTW and, optionally, PyFFTW wisdom.
    """
    
    # FFTW
    if FFTW:
        _makeFFTW()
        
    # PyFFTW
    if PyFFTW:
        _makePyFFTW()
        
    return True


def _showFFTW():
    """
    List information about the current LSL-specific FFTW wisdom.
    """
    
    if not os.path.exists(_wisdomFilenameFFTW):
        print("No LSL-specific FFTW wisdom file found, consider running make()")
        return False
        
    fh = open(_wisdomFilenameFFTW, 'r')
    lines = fh.readlines()
    fh.close()
    
    print("LSL FFTW Wisdom:")
    print(" Lines: %i" % len(lines))
    print(" Size: %i bytes" % os.path.getsize(_wisdomFilenameFFTW))
    print(" Last Modified: %s" % datetime.utcfromtimestamp(os.stat(_wisdomFilenameFFTW)[8]))
    
    return True


def _showPyFFTW():
    """
    List information about the current LSL-specific FFTW wisdom.
    """
    
    if not os.path.exists(_wisdomFilenamePyFFTW):
        print("No LSL-specific PyFFTW wisdom file found, consider running make()")
        return False
        
    try:
        import pyfftw
        
        fh = open(_wisdomFilenamePyFFTW, 'r')
        d,s,ld = pickle.load(fh)
        fh.close()
        
        d = d.split('\n')
        s = s.split('\n')
        ld = ld.split('\n')
        
        print("LSL PyFFTW Wisdom:")
        print(" Lines: %i (single) %i (double) %i (long double)" % (len(s), len(d), len(ld)))
        print(" Size: %i bytes" % os.path.getsize(_wisdomFilenamePyFFTW))
        print(" Last Modified: %s" % datetime.utcfromtimestamp(os.stat(_wisdomFilenamePyFFTW)[8]))
        
    except ImportError:
        print("PyFFTW is not installed, skipping")
        return False
    
    return True


def show(FFTW=True, PyFFTW=True):
    """
    List information about the current LSL-specific FFTW and PyFFTW wisdom.
    """
    
    # FFTW
    if FFTW:
        _showFFTW()
        
    # PyFFTW
    if PyFFTW:
        _showPyFFTW()
        
    return True
