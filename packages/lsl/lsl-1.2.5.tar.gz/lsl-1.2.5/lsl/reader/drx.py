# -*- coding: utf-8 -*-

"""
Python module to read in DRX data.  This module defines the following 
classes for storing the DRX data found in a file:

Frame
  object that contains all data associated with a particular DRX frame.  
  The primary constituents of each frame are:
    * FrameHeader - the DRX frame header object and
    * FrameData   - the DRX frame data object.
Combined, these two objects contain all of the information found in the 
original DRX frame.

ObservingBlock
object that stores a collection of Frames for all beams/tunings/
polarizations for a particular time.

The functions defined in this module fall into two class:
  1. convert a frame in a file to a Frame object and
  2. describe the format of the data in the file.

For reading in data, use the readFrame function.  It takes a python file-
handle as an input and returns a fully-filled Frame object.  The readBlock
function reads in a (user-defined) number of DRX frames and returns a 
ObservingBlock object.

For describing the format of data in the file, two function are provided:

getBeamCount
  read in the first few frames of an open file handle and return how many 
  beams are present in the file.

getFramesPerObs
  read in the first several frames to see how many frames (tunings/polarizations)
  are associated with each beam.

..versionchanged:: 1.2.0
    Dropped support for ObservingBlock since the lsl.reader.buffer modules does
    a better job.

.. versionchanged:: 0.4.0
    Switched over from pure Python readers to the new C-base Go Fast! readers.
"""

import copy
import numpy

from lsl.common import dp as dp_common
from lsl.reader._gofast import readDRX
from lsl.reader._gofast import syncError as gsyncError
from lsl.reader._gofast import eofError as geofError
from lsl.reader.errors import baseReaderError, syncError, eofError

__version__ = '0.8'
__revision__ = '$Rev: 3021 $'
__all__ = ['FrameHeader', 'FrameData', 'Frame', 'readFrame', 
           'getSampleRate', 'getBeamCount', 'getFramesPerObs', 'FrameSize', 'filterCodes', 
           '__version__', '__revision__', '__all__']

FrameSize = 4128

# List of filter codes and their corresponding sample rates in Hz
filterCodes = {1: 250000, 2: 500000, 3: 1000000, 4: 2000000, 5: 4900000, 6: 9800000, 7: 19600000}


class FrameHeader(object):
    """
    Class that stores the information found in the header of a DRX 
    frame.  All six fields listed in the DP ICD version H are stored as 
    well as the original binary header data.
    """
    
    def __init__(self, frameCount=None, drxID=None, secondsCount=None, decimation=None, timeOffset=None):
        self.frameCount = frameCount
        self.drxID = drxID
        self.secondsCount = secondsCount
        self.decimation = decimation
        self.timeOffset = timeOffset
    
    def parseID(self):
        """
        Parse the DRX ID into a tuple containing the beam (1 through
        4), tunning (1 and 2), and polarization (0 and 1).
        """
        
        beam = self.drxID&7
        tune = (self.drxID>>3)&7
        pol  = (self.drxID>>7)&1

        return (beam, tune, pol)
    
    def getSampleRate(self):
        """
        Return the sample rate of the data in samples/second.
        """
        
        sampleRate = dp_common.fS / self.decimation
        return sampleRate
        
    def getFilterCode(self):
        """
        Function to convert the sample rate in Hz to a filter code.
        """
        
        sampleCodes = {}
        for key in filterCodes:
            value = filterCodes[key]
            sampleCodes[value] = key

        return sampleCodes[self.getSampleRate()]


class FrameData(object):
    """
    Class that stores the information found in the data section of a DRX
    frame.  All three fields listed in the DP ICD version H are stored.
    """

    def __init__(self, timeTag=None, tuningWord=None, flags=None, iq=None):
        self.centralFreq = None
        self.gain = None
        self.timeTag = timeTag
        self.tuningWord = tuningWord
        self.flags = flags
        self.iq = iq
        
    def getCentralFreq(self):
        """
        Function to set the central frequency of the DRX data in Hz.
        """

        return dp_common.fS * self.tuningWord / 2**32

    def setGain(self, gain):
        """
        Function to set the gain of the DRX data.
        """

        self.gain = gain


class Frame(object):
    """
    Class that stores the information contained within a single DRX 
    frame.  It's properties are FrameHeader and FrameData objects.
    """

    def __init__(self, header=None, data=None):
        if header is None:
            self.header = FrameHeader()
        else:
            self.header = header
            
        if data is None:
            self.data = FrameData()
        else:
            self.data = data
            
        self.valid = True

    def parseID(self):
        """
        Convenience wrapper for the Frame.FrameHeader.parseID 
        function.
        """
        
        return self.header.parseID()

    def getSampleRate(self):
        """
        Convenience wrapper for the Frame.FrameHeader.getSampleRate 
        function.
        """
        
        return self.header.getSampleRate()
        
    def getFilterCode(self):
        """
        Convenience wrapper for the Frame.FrameHeader.getFilterCode function.
        """

        return self.header.getFilterCode()

    def getTime(self):
        """
        Function to convert the time tag from samples since the UNIX epoch
        (UTC 1970-01-01 00:00:00) to seconds since the UNIX epoch.
        """

        seconds = (self.data.timeTag - self.header.timeOffset) / dp_common.fS
        
        return seconds
    
    def getCentralFreq(self):
        """
        Convenience wrapper for the Frame.FrameData.getCentralFreq function.
        """

        return self.data.getCentralFreq()

    def setGain(self, gain):
        """
        Convenience wrapper for the Frame.FrameData.setGain function.
        """

        self.data.setGain(gain)

    def __add__(self, y):
        """
        Add the data sections of two frames together or add a number 
        to every element in the data section.
        """
    
        newFrame = copy.deepcopy(self)
        newFrame += y
        return newFrame
            
    def __iadd__(self, y):
        """
        In-place add the data sections of two frames together or add 
        a number to every element in the data section.
        """
        
        try:
            self.data.iq += y.data.iq
        except AttributeError:
            self.data.iq += numpy.complex64(y)
        return self
        
    def __mul__(self, y):
        """
        Multiple the data sections of two frames together or multiply 
        a number to every element in the data section.
        """
        
        newFrame = copy.deepcopy(self)
        newFrame *= y
        return newFrame
            
    def __imul__(self, y):
        """
        In-place multiple the data sections of two frames together or 
        multiply a number to every element in the data section.
        """
        
        try:
            self.data.iq *= y.data.iq
        except AttributeError:
            self.data.iq *= numpy.complex64(y)
        return self
            
    def __eq__(self, y):
        """
        Check if the time tags of two frames are equal or if the time
        tag is equal to a particular value.
        """
        
        tX = self.data.timeTag
        try:
            tY = y.data.timeTag
        except AttributeError:
            tY = y
        
        if tX == tY:
            return True
        else:
            return False
            
    def __ne__(self, y):
        """
        Check if the time tags of two frames are not equal or if the time
        tag is not equal to a particular value.
        """
        
        tX = self.data.timeTag
        try:
            tY = y.data.timeTag
        except AttributeError:
            tY = y
        
        if tX != tY:
            return True
        else:
            return False
            
    def __gt__(self, y):
        """
        Check if the time tag of the first frame is greater than that of a
        second frame or if the time tag is greater than a particular value.
        """
        
        tX = self.data.timeTag
        try:
            tY = y.data.timeTag
        except AttributeError:
            tY = y
        
        if tX > tY:
            return True
        else:
            return False
            
    def __ge__(self, y):
        """
        Check if the time tag of the first frame is greater than or equal to 
        that of a second frame or if the time tag is greater than a particular 
        value.
        """
        
        tX = self.data.timeTag
        try:
            tY = y.data.timeTag
        except AttributeError:
            tY = y
        
        if tX >= tY:
            return True
        else:
            return False
            
    def __lt__(self, y):
        """
        Check if the time tag of the first frame is less than that of a
        second frame or if the time tag is greater than a particular value.
        """
        
        tX = self.data.timeTag
        try:
            tY = y.data.timeTag
        except AttributeError:
            tY = y
        
        if tX < tY:
            return True
        else:
            return False
            
    def __le__(self, y):
        """
        Check if the time tag of the first frame is less than or equal to 
        that of a second frame or if the time tag is greater than a particular 
        value.
        """
        
        tX = self.data.timeTag
        try:
            tY = y.data.timeTag
        except AttributeError:
            tY = y
        
        if tX <= tY:
            return True
        else:
            return False
            
    def __cmp__(self, y):
        """
        Compare two frames based on the time tags.  This is helpful for 
        sorting things.
        """
        
        tX = self.data.timeTag
        tY = y.data.timeTag
        if tY > tX:
            return -1
        elif tX > tY:
            return 1
        else:
            return 0


def readFrame(filehandle, Gain=None, Verbose=False):
    """
    Function to read in a single DRX frame (header+data) and store the 
    contents as a Frame object.  This function wraps readerHeader and 
    readData.
    """
    
    # New Go Fast! (TM) method
    try:
        newFrame = readDRX(filehandle, Frame())
    except gsyncError:
        mark = filehandle.tell() - FrameSize
        raise syncError(location=mark)
    except geofError:
        raise eofError
    
    if Gain is not None:
        newFrame.setGain(Gain)
        
    return newFrame


def getSampleRate(filehandle, nFrames=None, FilterCode=False):
    """
    Find out what the sampling rate/filter code is from a single observations.  
    By default, the rate in Hz is returned.  However, the corresponding filter 
    code can be returned instead by setting the FilterCode keyword to true.
    
    This function is included to make easier to write code for TBN analysis and 
    modify it for DRX data.
    """

    # Save the current position in the file so we can return to that point
    fhStart = filehandle.tell()

    # Read in one frame
    newFrame = readFrame(filehandle)
    
    # Return to the place in the file where we started
    filehandle.seek(fhStart)

    if not FilterCode:
        return newFrame.getSampleRate()
    else:
        return newFrame.getFilterCode()


def getBeamCount(filehandle):
    """
    Find out how many beams are present by examining the first 32 DRX
    records.  Return the number of beams found.
    """

    # Save the current position in the file so we can return to that point
    fhStart = filehandle.tell()

    # Build up the list-of-lists that store ID codes and loop through 32
    # frames.  In each case, parse pull the DRX ID, extract the beam number, 
    # and append the DRX ID to the relevant beam array if it is not already 
    # there.
    beams = []
    for i in range(32):
        cFrame = readFrame(filehandle)
            
        cID = cFrame.header.drxID
        beam = cID&7
        if beam not in beams:
            beams.append(beam)
            
    # Return to the place in the file where we started
    filehandle.seek(fhStart)

    # Return the number of beams found
    return len(beams)


def getFramesPerObs(filehandle):
    """
    Find out how many frames are present per beam by examining the first 
    32 DRX records.  Return the number of frames per observations as a four-
    element tuple, one for each beam.
    """
    
    # Save the current position in the file so we can return to that point
    fhStart = filehandle.tell()
    
    # Build up the list-of-lists that store ID codes and loop through 32
    # frames.  In each case, parse pull the DRX ID, extract the beam number, 
    # and append the DRX ID to the relevant beam array if it is not already 
    # there.
    idCodes = [[], [], [], []]
    for i in range(32):
        cFrame = readFrame(filehandle)
        
        cID = cFrame.header.drxID
        beam = cID&7
        if cID not in idCodes[beam-1]:
            idCodes[beam-1].append(cID)
            
    # Return to the place in the file where we started
    filehandle.seek(fhStart)
    
    # Get the length of each beam list and return them as a tuple
    return (len(idCodes[0]), len(idCodes[1]), len(idCodes[2]), len(idCodes[3]))
