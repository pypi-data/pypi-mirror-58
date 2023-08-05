#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import math
import time
import argparse
from datetime import datetime

from lsl.reader import tbn
from lsl.common.progress import ProgressBar
from lsl.misc import parser as aph


def fileSplitFunction(fhIn, fhOut, nCaptures, nAntpols):
    pb = ProgressBar(max=nCaptures)
    
    for c in xrange(int(nCaptures)):
        for i in xrange(nAntpols):
            cFrame = fhIn.read(tbn.FrameSize)
            fhOut.write(cFrame)
            
        pb.inc(amount=1)
        if c != 0 and c % 100 == 0:
            sys.stdout.write(pb.show()+'\r')
            sys.stdout.flush()
            
    sys.stdout.write(pb.show()+'\r')
    sys.stdout.write('\n')
    sys.stdout.flush()


def main(args):
    filename = args.filename
    
    sizeB = os.path.getsize(filename)
    
    # Open the file and get some basic info about the data contained
    fh = open(filename, 'rb')
    sampleRate = tbn.getSampleRate(fh)
    nFramesX, nFramesY = tbn.getFramesPerObs(fh)
    
    nCaptures = sizeB / tbn.FrameSize / (nFramesX + nFramesY)
    
    print "Filename:    %s" % filename
    print "Size:        %.1f MB" % (float(sizeB)/1024/1024)
    print "Captures:    %i (%.2f seconds)" % (nCaptures, nCaptures*512/sampleRate)
    print "Stands:      %i (%i x pol., %i y pol.)" % ((nFramesX+nFramesY), nFramesX, nFramesY)
    print "Sample Rate: %.2f kHz" % (sampleRate/1000.0)
    print "==="

    if args.count > 0:
        nCaptures = args.count * sampleRate / 512
    else:
        nCaptures -= args.offset * sampleRate / 512
        args.count = nCaptures * 512 / sampleRate
    nSkip = int(args.offset * sampleRate / 512)

    print "Seconds to Skip:  %.2f (%i captures)" % (args.offset, nSkip)
    print "Seconds to Split: %.2f (%i captures)" % (args.count, nCaptures)

    # Make sure that the first frame in the file is the first frame if a capture 
    # (stand 1, pol 0).  If not, read in as many frames as necessary to get to 
    # the beginning of a complete capture.
    frame = tbn.readFrame(fh)
    stand, pol = frame.parseID()

    skip = 0
    while (2*(stand-1)+pol) != 0:
        frame = tbn.readFrame(fh)
        stand, pol = frame.parseID()
        skip += 1
    fh.seek(fh.tell() - tbn.FrameSize)

    if skip != 0:
        print "Skipped %i frames at the beginning of the file" % skip
    
    for c in list(range(nSkip)):
        if c < nSkip:
            fh.seek(fh.tell() + tbn.FrameSize*(nFramesX+nFramesY))
            continue
            
    nFramesRemaining = (sizeB - fh.tell()) / tbn.FrameSize
    nRecursions = int(nFramesRemaining / (nCaptures*(nFramesX+nFramesY)))
    if not args.recursive:
        nRecursions = 1
        
    scale = int(math.log10(nRecursions)) + 1
    ifString = "Working on #%%%ii of %i (%%s)" % (scale, nRecursions)
    
    for r in xrange(nRecursions):
        if args.date:
            filePos = fh.tell()
            junkFrame = tbn.readFrame(fh)
            fh.seek(filePos)
            
            dt = datetime.utcfromtimestamp(junkFrame.getTime())
            captFilename = "%s_%s.dat" % (os.path.splitext(os.path.basename(filename))[0], dt.isoformat())
        else:
            captFilename = "%s_s%04i_p%%0%ii.dat" % (os.path.splitext(os.path.basename(filename))[0], args.count, scale)
            captFilename = captFilename % r
            if not args.recursive:
                captFilename = "%s_s%04i.dat" % (os.path.splitext(os.path.basename(filename))[0], args.count)
            
        print ifString % (r+1, captFilename)
        
        t0 = time.time()
        fhOut = open(captFilename, 'wb')
        fileSplitFunction(fh, fhOut, nCaptures, nFramesX+nFramesY)
        fhOut.close()
        t1 = time.time()
        print "  Copied %i bytes in %.3f s (%.3f MB/s)" % (os.path.getsize(captFilename), t1-t0, os.path.getsize(captFilename)/1024.0**2/(t1-t0))
    fh.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='split a TBN file into several files', 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
    parser.add_argument('filename', type=str, 
                        help='filename to split')
    parser.add_argument('-c', '--count', type=aph.positive_float, default=10.0, 
                        help='number of seconds to keep')
    parser.add_argument('-o', '--offset', type=aph.positive_or_zero_float, default=0.0, 
                        help='number of seconds to skip before splitting')
    parser.add_argument('-d', '--date', action='store_true', 
                        help='label the split files with a date rather than a sequence number')
    parser.add_argument('-r', '--recursive', action='store_true', 
                        help='recursively split the file')
    args = parser.parse_args()
    main(args)
    
