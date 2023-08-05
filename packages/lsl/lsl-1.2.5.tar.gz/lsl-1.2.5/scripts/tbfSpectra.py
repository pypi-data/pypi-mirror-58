#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Given a TBF file, plot the time averaged spectra for each digitizer input."""

import os
import sys
import math
import ephem
import numpy
import argparse

from lsl.reader import tbf, errors
from lsl.common import stations, metabundleADP
from lsl.astro import unix_to_utcjd, DJD_OFFSET
from lsl.misc import parser as aph

from matplotlib import pyplot as plt


def bestFreqUnits(freq):
    """Given a numpy array of frequencies in Hz, return a new array with the
    frequencies in the best units possible (kHz, MHz, etc.)."""
    
    # Figure out how large the data are
    scale = int(math.log10(freq.max()))
    if scale >= 9:
        divis = 1e9
        units = 'GHz'
    elif scale >= 6:
        divis = 1e6
        units = 'MHz'
    elif scale >= 3:
        divis = 1e3
        units = 'kHz'
    else:
        divis = 1
        units = 'Hz'
        
    # Convert the frequency
    newFreq = freq / divis
    
    # Return units and freq
    return (newFreq, units)


def main(args):
    # Setup the LWA station information
    if args.metadata is not None:
        try:
            station = stations.parseSSMIF(args.metadata)
        except ValueError:
            station = metabundleADP.getStation(args.metadata, ApplySDM=True)
    else:
        station = stations.lwasv
    antennas = station.getAntennas()
    
    fh = open(args.filename, 'rb')
    nFrames = os.path.getsize(args.filename) / tbf.FrameSize
    antpols = len(antennas)
    
    # Read in the first frame and get the date/time of the first sample 
    # of the frame.  This is needed to get the list of stands.
    junkFrame = tbf.readFrame(fh)
    fh.seek(0)
    beginDate = ephem.Date(unix_to_utcjd(junkFrame.getTime()) - DJD_OFFSET)
    
    # Figure out how many frames there are per observation and the number of
    # channels that are in the file
    nFramesPerObs = tbf.getFramesPerObs(fh)
    nChannels = tbf.getChannelCount(fh)
    nSamples = 7840
    
    # Figure out how many chunks we need to work with
    nChunks = nFrames / nFramesPerObs
    
    # Pre-load the channel mapper
    mapper = []
    for i in xrange(2*nFramesPerObs):
        cFrame = tbf.readFrame(fh)
        if cFrame.header.firstChan not in mapper:
            mapper.append( cFrame.header.firstChan )
    fh.seek(-2*nFramesPerObs*tbf.FrameSize, 1)
    mapper.sort()
    
    # Calculate the frequencies
    freq = numpy.zeros(nChannels)
    for i,c in enumerate(mapper):
        freq[i*12:i*12+12] = c + numpy.arange(12)
    freq *= 25e3
    
    # File summary
    print "Filename: %s" % args.filename
    print "Date of First Frame: %s" % str(beginDate)
    print "Frames per Observation: %i" % nFramesPerObs
    print "Channel Count: %i" % nChannels
    print "Frames: %i" % nFrames
    print "==="
    print "Chunks: %i" % nChunks
    
    spec = numpy.zeros((nChannels,256,2))
    norm = numpy.zeros_like(spec)
    for i in xrange(nChunks):
        # Inner loop that actually reads the frames into the data array
        for j in xrange(nFramesPerObs):
            # Read in the next frame and anticipate any problems that could occur
            try:
                cFrame = tbf.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                print "WARNING: Mark 5C sync error on frame #%i" % (int(fh.tell())/tbf.FrameSize-1)
                continue
            if not cFrame.header.isTBF():
                continue
                
            firstChan = cFrame.header.firstChan
            
            # Figure out where to map the channel sequence to
            try:
                aStand = mapper.index(firstChan)
            except ValueError:
                mapper.append(firstChan)
                aStand = mapper.index(firstChan)
            
            # Actually load the data.
            spec[aStand*12:aStand*12+12,:,:] += numpy.abs(cFrame.data.fDomain)**2
            norm[aStand*12:aStand*12+12,:,:] += 1
            
    spec /= norm
    fh.close()
    
    # Reshape and transpose to get it in to a "normal" order
    spec.shape = (spec.shape[0], spec.shape[1]*spec.shape[2])
    spec = spec.T
    
    # Apply the cable loss corrections, if requested
    if False:
        for s in range(spec.shape[0]):
            currGain = antennas[s].cable.gain(freq)
            spec[s,:] /= currGain
                
    # Put the frequencies in the best units possible
    freq, units = bestFreqUnits(freq)
    
    # Deal with the `keep` options
    if args.keep == 'all':
        antpolsDisp = int(numpy.ceil(antpols/20))
        js = [i for i in xrange(antpols)]
    else:
        antpolsDisp = int(numpy.ceil(len(args.keep)*2/20))
        if antpolsDisp < 1:
            antpolsDisp = 1
            
        js = []
        for k in args.keep:
            for i,ant in enumerate(antennas):
                if ant.stand.id == k:
                    js.append(i)
                    
    nPlot = len(js)
    if nPlot < 16:
        if nPlot % 4 == 0 and nPlot != 4:
            figsY = 4
        else:
            figsY = 2
        figsX = int(numpy.ceil(1.0*nPlot/figsY))
    else:
        figsY = 4
        figsX = 4
    figsN = figsX*figsY
    for i in xrange(antpolsDisp):
        # Normal plotting
        fig = plt.figure()
        for k in xrange(i*figsN, i*figsN+figsN):
            try:
                j = js[k]
                currSpectra = numpy.squeeze( numpy.log10(spec[j,:])*10.0 )
            except IndexError:
                break
            ax = fig.add_subplot(figsX, figsY, (k%figsN)+1)
            ax.plot(freq, currSpectra, label='Stand: %i, Pol: %i (Dig: %i)' % (antennas[j].stand.id, antennas[j].pol, antennas[j].digitizer))
            
            ax.set_title('Stand: %i (%i); Dig: %i [%i]' % (antennas[j].stand.id, antennas[j].pol, antennas[j].digitizer, antennas[j].getStatus()))
            ax.set_xlabel('Frequency [%s]' % units)
            ax.set_ylabel('P.S.D. [dB/RBW]')
            ax.set_ylim([-10, 30])
            
        # Save spectra image if requested
        if args.output is not None:
            base, ext = os.path.splitext(args.output)
            outFigure = "%s-%02i%s" % (base, i+1, ext)
            fig.savefig(outFigure)
            
        plt.draw()
        
    print "RBW: %.4f %s" % ((freq[1]-freq[0]), units)
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description='read in a TBF file and create a collection of time-averaged spectra', 
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
            )
    parser.add_argument('filename', type=str, 
                        help='filename to process')
    parser.add_argument('-m', '--metadata', type=str, 
                        help='name of the SSMIF or metadata tarball file to use for mappings')
    parser.add_argument('-q', '--quiet', dest='verbose', action='store_false',
                        help='run %(prog)s in silent mode')
    parser.add_argument('-k', '--keep', type=aph.csv_int_list, default='all', 
                        help='only display the following comma-seperated list of stands')
    parser.add_argument('-o', '--output', type=str, 
                        help='output file name for spectra image')
    args = parser.parse_args()
    main(args)
    
