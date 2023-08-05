# -*- coding: utf-8 -*-

# Python3 compatiability
from __future__ import print_function

"""
Modules to take TBW/TBN time series data and write it to a FITS file composed 
of binary tables.  The format of TSFITS files is:

**PRIMARY HDU**

Keywords:
 * OBJECT - object being observed in this data set, e.g., 'zenith'
 * TELESCOP - telescope used for the observations, e.g., 'LWA-1'
 * OBSMODE - observation mode used for the data.  Options are TBW or TBN.
 * NSTANDS - number of stands found in the file
 * TBWBITS *optional* - how many bits are used by the TBW data (4 or 12)
 * FILTER *optional* - TBN filter code used to acquire the data
 * GAIN *optional* - TBN gain setting used to acquire the data
 * FREQ *optional* - central frequency in Hz for the TBN observations

**TIME SERIES HDU**

Binary table that stores the actual observations.  There is one TIME SERIES 
extension per stand (TBW/TBN) or beam/tuning pair (DRX) in the data.

Keywords:
 * EXTNAME - extension name of 'TIME SERIES'
 * EXTVER - extension version equal to the order in which the data was 
            added to the FITS file
 * STAND - stand number associated with this data
 * DATE-OBS - date of observation for the first sample of the first data 
              row

Data:
 * DATA - column storing the observations.  For TBW data this consists of 
          400 (12-bit) or 1200 (4-bit) elements per row stored as 16-bit 
          integers.  For TBN data this consists of 512 elements per row 
          stored as 32-bit complex numbers.  For DRX data this consists of 
          4096 elements per row stored as 32-bit complex numbers.
 * POL - column storing the polarization associated with the DATA column.  
         'x' polarization is stored as 0 and 'y' polarization is stored as 1.  
         The values is stored as a 16-bit integer.
 * TIME - number of samples at f_S (196 MSamples/s) since DATE-OBS for the
          first sample in the row.  This is stored as a 64-bit integer.
"""

import os
import time
import numpy
import pyfits
from datetime import datetime, timedelta, tzinfo

from lsl.common import dp as dp_common

__version__ = '0.5'
__revision__ = '$Rev: 2667 $'
__all__ = ['UTC', 'TSFITS', 'TBW', 'TBN', '__version__', '__revision__', '__all__']


import warnings
warnings.warn("lsl.writer.tsfits will be removed in LSL version 1.3.0", DeprecationWarning)


class UTC(tzinfo):
    """
    tzinfo object for UTC time.
    """

    def utcoffset(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return timedelta(0)


class TSFITS(object):
    """
    Class that holds TSFITS data until it is ready to be written to disk.
    """

    def __init__(self, filename, mode, UseQueue=True, verbose=False, memmap=None, clobber=False):
        """
        Initialize a TSFITS object using a filename and an observation mode 
        (TBW or TBN).  Optionally, TSFITS can be told to overwrite the file if it 
        already exists using the 'Overwrite' keyword.
        
        .. versionchanged:: 1.1.2
            Added the 'memmap' to control if the file is memory mapped.
            Changed 'Overwrite' to 'clobber' for consistency with other writers.
        """

        assert(mode in ['TBW', 'TBN'])

        self.filename = filename
        self.mode = mode
        self.hdulist = None
        self.UseQueue = UseQueue
        self.queue = {}
        self.queueLimit = 10000
        self.site = 'LWA'
        self.firstSamples = {}
        self.verbose = verbose

        if os.path.exists(filename):
            if clobber:
                os.unlink(filename)
            else:
                raise IOError("File '%s' already exists" % filename)
        self.standCount = 0
        primary = pyfits.PrimaryHDU()
        primary.header['OBJECT'] = 'zenith'
        primary.header['TELESCOP'] = self.site
        primary.header['OBSMODE'] = self.mode
        primary.header['NSTAND'] = self.standCount
        
        primary.header['COMMENT'] = " FITS (Flexible Image Transport System) format is defined in 'Astronomy and Astrophysics', volume 376, page 359; bibcode: 2001A&A...376..359H"
        
        hdulist = pyfits.HDUList([primary])
        hdulist.writeto(filename)
        
        self.hdulist = pyfits.open(self.filename, mode="update", memmap=memmap)

    def info(self):
        """
        Short-cut to the pyfits.info() function on an opened FITS file.
        """

        self.hdulist.info()

    def flush(self):
        """
        Short-cut to the pyfits.flush() function on an opened FITS file.
        """

        self.hdulist.flush()

    def close(self):
        """
        Empty the data queue (if it exists) and write all changes to disk 
        using flush.
        """

        if self.UseQueue:
            self.__emptyQueue()
        self.flush()

    def setSite(self, site):
        """
        Set the TELESCOP keyword in the primary HDU using an lsl.common.stations
        object.
        """

        self.site = site.name

        self.hdulist[0].header['TELESCOP'] = self.site

        self.flush()

    def __findExtension(self, stand):
        """
        Private function to find out which extension stores the stand in 
        question.  None is returned is that stand is not in the TSFITS file.
        """

        extension = None

        i = 1
        for hdu in self.hdulist[1:]:
            if int(hdu.header['stand']) == int(stand):
                extension = i
                break
            i = i + 1

        return extension

    def __makeAppendTable(self, extension, AddRows=1):
        """
        Private function to make a temporary table for appending data.
        """

        nrows = self.hdulist[extension].data.shape[0]
        tempHDU = pyfits.new_table(self.hdulist[extension].columns, nrows=nrows+AddRows)
        tempHDU.header = self.hdulist[extension].header.copy()
    
        return tempHDU

    def __applyAppendTable(self, extension, tempHDU):
        """
        Private function to replace the given extension with the temporary
        table.
        """

        self.hdulist[extension] = tempHDU
        self.flush()

    def __addDataSingle(self, frame):
        """
        Private function to add a single data entry to a TSFITS file.  This 
        method is not particular fast since the existing file needs to be copied
        to append data to the end of a particular extension.
        """

        if self.mode == 'TBW':
            stand = frame.parseID()
        else:
            try:
                stand, pol = frame.parseID()
            except ValueError:
                stand, tune, pol = frame.parseID()
                stand = stand*10 + tune
        extension = self.__findExtension(stand)

        if extension is None:
            if self.verbose:
                print("Stand '%i' not found, creating new binary table extension" % stand)
            self.standCount = self.standCount + 1

            if self.mode == 'TBW':
                # Data
                c1 = pyfits.Column(name='data', format='%iI' % frame.data.xy.shape[1], array=frame.data.xy.astype(numpy.int16))
                # Polarization
                c2 = pyfits.Column(name='pol', format='1I', array=numpy.array([0, 1], dtype=numpy.int16))
                # Time
                c3 = pyfits.Column(name='time', format='1K', array=numpy.array([0, 0]))
            else:
                # Data
                data = frame.data.iq.astype(numpy.csingle)
                data.shape = (1,)+data.shape
                c1 = pyfits.Column(name='data', format='%iC' % data.shape[1], array=data)
                # Polarization
                c2 = pyfits.Column(name='pol', format='1I', array=numpy.array([0], dtype=numpy.int16))
                # Time
                c3 = pyfits.Column(name='time', format='1K', array=numpy.array([0]))

            # Define the collection of columns
            colDefs = pyfits.ColDefs([c1, c2, c3])

            # Get the time of the first sample and convert it to a datetime
            self.firstSamples[stand] = long(frame.data.timeTag / dp_common.fS)
            firstSample = datetime.utcfromtimestamp(self.firstSamples[stand])

            tsfits = pyfits.new_table(colDefs)
            tsfits.header.set('EXTNAME', 'TIME SERIES', after='TFIELDS')
            tsfits.header.set('EXTVER', self.standCount, after='EXTNAME')
            tsfits.header.set('STAND', stand, after='EXTVER')
            tsfits.header['DATE-OBS'] = firstSample.isoformat()

            self.hdulist.append(tsfits)
            self.hdulist[0].header['NSTAND'] = self.standCount
            self.flush()
            
            self.hdulist[-1].data.field('pol')[0] = numpy.array([0], dtype=numpy.int16)
            self.hdulist[-1].data.field('time')[0] = frame.data.timeTag / dp_common.fS - self.firstSamples[stand]
            if self.mode == 'TBW':
                self.hdulist[-1].data.field('pol')[1] = numpy.array([1], dtype=numpy.int16)
                self.hdulist[-1].data.field('time')[1] = frame.data.timeTag / dp_common.fS - self.firstSamples[stand]
        else:
            # Make sure that we have a first sample time to reference to if 
            # we are adding on to the end of a file
            if stand not in self.firstSamples.keys():
                firstSample = datetime.strptime(self.hdulist[extension].header['DATE-OBS'], "%Y-%m-%dT%H:%M:%S")
                self.firstSamples[stand] = long(time.mktime(firstSample.timetuple()))

            nrows = self.hdulist[extension].data.shape[0]
            if self.mode == 'TBW':
                tempHDU = self.__makeAppendTable(extension, AddRows=2)
                tempHDU.data.field('data')[nrows] = numpy.squeeze(frame.data.xy.astype(numpy.int16)[0,:])
                tempHDU.data.field('pol')[nrows] = numpy.array([0], dtype=numpy.int16)
                tempHDU.data.field('time')[nrows] = frame.data.timeTag / dp_common.fS - self.firstSamples[stand]
                tempHDU.data.field('data')[nrows+1] = numpy.squeeze(frame.data.xy.astype(numpy.int16)[1,:])
                tempHDU.data.field('pol')[nrows+1] = numpy.array([1], dtype=numpy.int16)
                tempHDU.data.field('time')[nrows+1] = frame.data.timeTag / dp_common.fS - self.firstSamples[stand]
            else:
                tempHDU = self.__makeAppendTable(extension, AddRows=1)
                data = frame.data.iq.astype(numpy.csingle)
                data.shape = (1,)+data.shape
                tempHDU.data.field('data')[nrows:] = data
                tempHDU.data.field('pol')[nrows:] = numpy.array([pol], dtype=numpy.int16)
                tempHDU.data.field('time')[nrows:] = numpy.array([frame.data.timeTag]) / dp_common.fS - self.firstSamples[stand]

            self.__applyAppendTable(extension, tempHDU)

        self.flush()

    def __addDataQueue(self, frame):
        """
        Private function similar to __addDataSignle, but it saves the data to 
        memory (self.queue) to be written once the queue fills up.
        """

        if self.mode == 'TBW':
            stand = frame.parseID()
        else:
            try:
                stand, pol = frame.parseID()
            except ValueError:
                stand, tune, pol = frame.parseID()
                stand = stand*10 + tune
        if stand not in self.queue.keys():
            self.queue[stand] = []
        self.queue[stand].append(frame)

        if len(self.queue[stand]) >= self.queueLimit:
            start = 0
            extension = self.__findExtension(stand)

            if extension is None:
                start = 1
                frame = self.queue[stand][0]
                
                if self.verbose:
                    print("Stand '%i' not found, creating new binary table extension" % stand)
                self.standCount = self.standCount + 1

                if self.mode == 'TBW':
                    # Data
                    c1 = pyfits.Column(name='data', format='%iI' % frame.data.xy.shape[1], array=frame.data.xy.astype(numpy.int16))
                    # Polarization
                    c2 = pyfits.Column(name='pol', format='1I', array=numpy.array([0, 1], dtype=numpy.int16))
                    # Time
                    c3 = pyfits.Column(name='time', format='1K', array=numpy.array([0, 0]))
                else:
                    # Data
                    data = frame.data.iq.astype(numpy.csingle)
                    data.shape = (1,)+data.shape
                    c1 = pyfits.Column(name='data', format='%iC' % data.shape[1], array=data)
                    # Polarization
                    c2 = pyfits.Column(name='pol', format='1I', array=numpy.array([0], dtype=numpy.int16))
                    # Time
                    c3 = pyfits.Column(name='time', format='1K', array=numpy.array([0]))

                # Define the collection of columns
                colDefs = pyfits.ColDefs([c1, c2, c3])

                # Get the time of the first sample and convert it to a datetime
                self.firstSamples[stand] = long(frame.data.timeTag / dp_common.fS)
                firstSample = datetime.utcfromtimestamp(self.firstSamples[stand])

                tsfits = pyfits.new_table(colDefs)
                tsfits.header.set('EXTNAME', 'TIME SERIES', after='TFIELDS')
                tsfits.header.set('EXTVER', self.standCount, after='EXTNAME')
                tsfits.header.set('STAND', stand, after='EXTVER')
                tsfits.header['DATE-OBS'] = firstSample.isoformat('T')

                self.hdulist.append(tsfits)
                self.hdulist[0].header['NSTAND'] = self.standCount
                self.flush()
                
                self.hdulist[-1].data.field('pol')[0] = numpy.array([0], dtype=numpy.int16)
                self.hdulist[-1].data.field('time')[0] = frame.data.timeTag / dp_common.fS - self.firstSamples[stand]
                if self.mode == 'TBW':
                    self.hdulist[-1].data.field('time')[1] = frame.data.timeTag / dp_common.fS - self.firstSamples[stand]
                    self.hdulist[-1].data.field('pol')[1] = numpy.array([1], dtype=numpy.int16)

                self.flush()
                extension = self.__findExtension(stand)

            # Make sure that we have a first sample time to reference to if 
            # we are adding on to the end of a file
            if stand not in self.firstSamples.keys():
                firstSample = datetime.strptime(self.hdulist[extension].header['DATE-OBS'], "%Y-%m-%dT%H:%M:%S")
                self.firstSamples[stand] = long(time.mktime(firstSample.timetuple()))

            nrows = self.hdulist[extension].data.shape[0]
            if self.mode == 'TBW':
                tempHDU = self.__makeAppendTable(extension, AddRows=2*(self.queueLimit-start))
                for count,frame in zip(range(len(self.queue[stand][start:])), self.queue[stand][start:]):
                    tempHDU.data.field('data')[nrows+2*count] = numpy.squeeze(frame.data.xy.astype(numpy.int16)[0,:])
                    tempHDU.data.field('pol')[nrows+2*count] = numpy.array([0], dtype=numpy.int16)
                    tempHDU.data.field('time')[nrows+2*count] = frame.data.timeTag / dp_common.fS - self.firstSamples[stand]
                    tempHDU.data.field('data')[nrows+2*count+1] = numpy.squeeze(frame.data.xy.astype(numpy.int16)[1,:])
                    tempHDU.data.field('pol')[nrows+2*count+1] = numpy.array([1], dtype=numpy.int16)
                    tempHDU.data.field('time')[nrows+2*count+1] = frame.data.timeTag / dp_common.fS - self.firstSamples[stand]
            else:
                tempHDU = self.__makeAppendTable(extension, AddRows=(self.queueLimit-start))
                for count,frame in zip(range(len(self.queue[stand][start:])), self.queue[stand][start:]):
                    try:
                        stand, pol = frame.parseID()
                    except ValueError:
                        stand, tune, pol = frame.parseID()
                        stand = stand*10 + tune
                        
                    data = frame.data.iq.astype(numpy.csingle)
                    data.shape = (1,) + data.shape
                    tempHDU.data.field('data')[nrows+count] = data
                    tempHDU.data.field('pol')[nrows+count] = numpy.array([pol], dtype=numpy.int16)
                    tempHDU.data.field('time')[nrows+count] = frame.data.timeTag / dp_common.fS - self.firstSamples[stand]

            self.__applyAppendTable(extension, tempHDU)
            del(self.queue[stand])

    def __emptyQueue(self):
        """
        Private function to empty a empty the self.queue dictionary on demand
        if it exists.
        """

        for stand in self.queue.keys():
            if len(self.queue[stand]) == 0:
                continue
            queueSize = len(self.queue[stand])
            start = 0
            extension = self.__findExtension(stand)

            if extension is None:
                start = 1
                frame = self.queue[stand][0]
                
                if self.verbose:
                    print("Stand '%i' not found, creating new binary table extension" % stand)
                self.standCount = self.standCount + 1

                if self.mode == 'TBW':
                    # Data
                    c1 = pyfits.Column(name='data', format='%iI' % frame.data.xy.shape[1], array=frame.data.xy.astype(numpy.int16))
                    # Polarization
                    c2 = pyfits.Column(name='pol', format='1I', array=numpy.array([0, 1], dtype=numpy.int16))
                    # Time
                    c3 = pyfits.Column(name='time', format='1K', array=numpy.array([0, 0]))
                else:
                    # Data
                    data = frame.data.iq.astype(numpy.csingle)
                    data.shape = (1,)+data.shape
                    c1 = pyfits.Column(name='data', format='%iC' % data.shape[1], array=data)
                    # Polarization
                    c2 = pyfits.Column(name='pol', format='1I', array=numpy.array([0], dtype=numpy.int16))
                    # Time
                    c3 = pyfits.Column(name='time', format='1K', array=numpy.array([0]))

                # Define the collection of columns
                colDefs = pyfits.ColDefs([c1, c2, c3])

                # Get the time of the first sample and convert it to a datetime
                self.firstSamples[stand] = long(frame.data.timeTag / dp_common.fS)
                firstSample = datetime.utcfromtimestamp(self.firstSamples[stand])

                tsfits = pyfits.new_table(colDefs)
                tsfits.header.set('EXTNAME', 'TIME SERIES', after='TFIELDS')
                tsfits.header.set('EXTVER', self.standCount, after='EXTNAME')
                tsfits.header.set('STAND', stand, after='EXTVER')
                tsfits.header['DATE-OBS'] = firstSample.isoformat('T')

                self.hdulist.append(tsfits)
                self.hdulist[0].header['NSTAND'] = self.standCount
                self.flush()
                
                self.hdulist[-1].data.field('pol')[0] = numpy.array([0], dtype=numpy.int16)
                self.hdulist[-1].data.field('time')[0] = frame.data.timeTag / dp_common.fS - self.firstSamples[stand]
                if self.mode == 'TBW':
                    self.hdulist[-1].data.field('time')[1] = frame.data.timeTag / dp_common.fS - self.firstSamples[stand]
                    self.hdulist[-1].data.field('pol')[1] = numpy.array([1], dtype=numpy.int16)

                self.flush()
                extension = self.__findExtension(stand)

            # Make sure that we have a first sample time to reference to if 
            # we are adding on to the end of a file
            if stand not in self.firstSamples.keys():
                firstSample = datetime.strptime(self.hdulist[extension].header['DATE-OBS'], "%Y-%m-%dT%H:%M:%S")
                self.firstSamples[stand] = long(time.mktime(firstSample.timetuple()))

            nrows = self.hdulist[extension].data.shape[0]
            if self.mode == 'TBW':
                tempHDU = self.__makeAppendTable(extension, AddRows=2*(queueSize-start))
                for count,frame in zip(range(len(self.queue[stand][start:])), self.queue[stand][start:]):
                    tempHDU.data.field('data')[nrows+2*count] = numpy.squeeze(frame.data.xy.astype(numpy.int16)[0,:])
                    tempHDU.data.field('pol')[nrows+2*count] = numpy.array([0], dtype=numpy.int16)
                    tempHDU.data.field('time')[nrows+2*count] = frame.data.timeTag / dp_common.fS - self.firstSamples[stand]
                    tempHDU.data.field('data')[nrows+2*count+1] = numpy.squeeze(frame.data.xy.astype(numpy.int16)[1,:])
                    tempHDU.data.field('pol')[nrows+2*count+1] = numpy.array([1], dtype=numpy.int16)
                    tempHDU.data.field('time')[nrows+2*count+1] = frame.data.timeTag / dp_common.fS - self.firstSamples[stand]
            else:
                tempHDU = self.__makeAppendTable(extension, AddRows=(queueSize-start))
                for count,frame in zip(range(len(self.queue[stand][start:])), self.queue[stand][start:]):
                    try:
                        stand, pol = frame.parseID()
                    except ValueError:
                        stand, tune, pol = frame.parseID()
                        stand = stand*10 + tune
                        
                    data = frame.data.iq.astype(numpy.csingle)
                    data.shape = (1,) + data.shape
                    tempHDU.data.field('data')[nrows+count] = data
                    tempHDU.data.field('pol')[nrows+count] = numpy.array([pol], dtype=numpy.int16)
                    tempHDU.data.field('time')[nrows+count] = frame.data.timeTag / dp_common.fS - self.firstSamples[stand]

            self.__applyAppendTable(extension, tempHDU)
            del(self.queue[stand])

    def addStandData(self, frame):
        """
        Add a frame object to the TSFITS file.  This function takes care of 
        figuring out which extension the data goes to and how it should be formated.
        This function also updates the primary HDU with information about the data, 
        i.e., TBW data bits, TBN filter code, etc.
        """

        if self.mode == 'TBW':
            try:
                self.hdulist[0].header['TBWBITS']
            except:
                self.hdulist[0].header['TBWBITS'] = frame.getDataBits()
                self.flush()
        else:
            try:
                self.hdulist[0].header['FILTER']
            except:
                if frame.getFilterCode() is not None:
                    self.hdulist[0].header['FILTER'] = frame.getFilterCode()
                if getattr(frame.header, 'gain', None) is not None:
                    self.hdulist[0].header['GAIN'] = frame.header.gain
                if getattr(frame.header, 'tuningWord', None) is not None:
                    self.hdulist[0].header['FREQ'] = frame.getCentralFreq()
                self.flush()

        if self.UseQueue:
            self.__addDataQueue(frame)
        else:
            self.__addDataSingle(frame)

    def getStandData(self, stand):
        """
        Retrieve a dictionary of all data stored for a particular stand.  The 
        dictionary keys are:
         * *data* - numpy array of data
         * *pol* - numpy array of polarizations
         * *time* - numpy array of times in samples at f_S since DATE-OBS
        """

        extension = self.__findExtension(stand)
        
        if extension is None:
            output = {}
            for key in ['data', 'pol', 'time']:
                output[key] = None
        else:
            output = {}
            for key in ['data', 'pol', 'time']:
                output[key] = self.hdulist[extension].data.field(key)
        return output


class TBW(TSFITS):
    """
    Sub-class of TSFITS for dealing with TBW data in particular.
    """

    def __init__(self, filename, UseQueue=True, verbose=False, memmap=None, clobber=False):
        super(TBW, self).__init__(filename, 'TBW', UseQueue=UseQueue, verbose=verbose, memmap=memmap, clobber=clobber)
        

class TBN(TSFITS):
    """
    Sub-class of TSFITS for dealing with TBN data in particular.
    """

    def __init__(self, filename, UseQueue=True, verbose=False, memmap=None, clobber=False):
        super(TBN, self).__init__(filename, 'TBN', UseQueue=UseQueue, verbose=verbose, memmap=memmap, clobber=clobber)
