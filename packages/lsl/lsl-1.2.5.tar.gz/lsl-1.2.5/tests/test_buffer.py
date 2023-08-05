# -*- coding: utf-8 -*-

# Python3 compatiability
from __future__ import division
import sys
if sys.version_info > (3,):
    xrange = range
    
"""
Unit test for the lsl.reader.buffer module.
"""

import os
import unittest

from lsl.common.paths import dataBuild as dataPath
from lsl.reader import tbn, drx, tbf
from lsl.reader import errors
from lsl.reader import buffer


__revision__ = "$Rev: 2470 $"
__version__  = "0.2"
__author__    = "Jayce Dowell"


tbnFile = os.path.join(dataPath, 'tests', 'tbn-test.dat')
drxFile = os.path.join(dataPath, 'tests', 'drx-test.dat')
tbfFile = os.path.join(dataPath, 'tests', 'tbf-test.dat')


class buffer_tests(unittest.TestCase):
    """A unittest.TestCase collection of unit tests for the lsl.reader.buffer
    module."""
    
    #
    # TBN
    #
    
    def test_tbn_default(self):
        """Test the TBN ring buffer with the default values."""
        
        fh = open(tbnFile, 'rb')
        nFpO = tbn.getFramesPerObs(fh)
        nFpO = nFpO[0] + nFpO[1]
        
        # Create the FrameBuffer instance
        frameBuffer = buffer.TBNFrameBuffer(stands=range(1,nFpO//2+1), pols=[0, 1])
        
        # Go
        while True:
            try:
                cFrame = tbn.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                continue
                
            frameBuffer.append(cFrame)
            cFrames = frameBuffer.get()
            
            if cFrames is None:
                continue
            
        fh.close()
        
        # Make sure we have the right number of frames in the buffer
        nFrames = 0
        for key in frameBuffer.buffer.keys():
            nFrames = nFrames + len(frameBuffer.buffer[key])
        self.assertEqual(nFrames, 29)
        
        # Make sure nothing has happened that shouldn't have
        self.assertEqual(frameBuffer.full,    0)
        self.assertEqual(frameBuffer.partial, 0)
        self.assertEqual(frameBuffer.missing, 0)
        self.assertEqual(frameBuffer.dropped, 0)
        
        # Make sure we have the right keys
        for key in frameBuffer.buffer.keys():
            self.assertTrue(key in (119196674956800, 119196675960320))
            
        # Make sure the buffer keys have the right sizes
        self.assertEqual(len(frameBuffer.buffer[119196674956800]), 20)
        self.assertEqual(len(frameBuffer.buffer[119196675960320]),  9)
        
    def test_tbn_small(self):
        """Test a small version of the TBN ring buffer."""
        
        fh = open(tbnFile, 'rb')
        nFpO = tbn.getFramesPerObs(fh)
        nFpO = nFpO[0] + nFpO[1]
        
        # Create the FrameBuffer instance
        frameBuffer = buffer.TBNFrameBuffer(stands=range(1,nFpO//2+1), pols=[0, 1], nSegments=1)
        
        # Go
        while True:
            try:
                cFrame = tbn.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                continue
                
            frameBuffer.append(cFrame)
            cFrames = frameBuffer.get()
            
            if cFrames is None:
                continue
                
            # Make sure the dump has one of the expected time tags
            self.assertTrue(cFrames[0].data.timeTag in (119196674956800, 119196675960320))
            
            # Make sure it has the right number of frames
            self.assertEqual(len(cFrames), nFpO)
            
        fh.close()
        
    def test_tbn_buffer_reorder(self):
        """Test the reorder function of the TBN ring buffer."""
        
        fh = open(tbnFile, 'rb')
        nFpO = tbn.getFramesPerObs(fh)
        nFpO = nFpO[0] + nFpO[1]
        
        # Create the FrameBuffer instance
        frameBuffer = buffer.TBNFrameBuffer(stands=range(1,nFpO//2+1), pols=[0, 1], nSegments=1, ReorderFrames=True)
        
        # Go
        while True:
            try:
                cFrame = tbn.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                continue
                
            frameBuffer.append(cFrame)
            cFrames = frameBuffer.get()
            
            if cFrames is None:
                continue
                
            # Make sure the dump has one of the expected time tags
            self.assertTrue(cFrames[0].data.timeTag in (119196674956800, 119196675960320))
            
            # Make sure it has the right number of frames
            self.assertEqual(len(cFrames), nFpO)
            
            # Check the order
            for i in xrange(1, len(cFrames)):
                pS, pP = cFrames[i-1].parseID()
                cS, cP = cFrames[i].parseID()
                
                pID = pS*2 + pP
                cID = cS*2 + cP
                self.assertTrue(cID > pID)
                
        fh.close()
        
    def test_tbn_buffer_flush(self):
        """Test the TBN ring buffer's flush() function."""
        
        fh = open(tbnFile, 'rb')
        nFpO = tbn.getFramesPerObs(fh)
        nFpO = nFpO[0] + nFpO[1]
        
        # Create the FrameBuffer instance
        frameBuffer = buffer.TBNFrameBuffer(stands=range(1,nFpO//2+1), pols=[0, 1])
        
        # Go
        while True:
            try:
                cFrame = tbn.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                continue
                
            frameBuffer.append(cFrame)
            cFrames = frameBuffer.get()
            
            if cFrames is None:
                continue
                
        fh.close()
        
        # Flush the buffer
        for cFrames in frameBuffer.flush():
            # Make sure the dump has one of the expected time tags
            self.assertTrue(cFrames[0].data.timeTag in (119196674956800, 119196675960320))
            
            # Make sure it has the right number of frames
            self.assertEqual(len(cFrames), nFpO)
            
    def test_tbn_buffer_reorder_flush(self):
        """Test the TBN ring buffer's flush() function with reordering."""
        
        fh = open(tbnFile, 'rb')
        nFpO = tbn.getFramesPerObs(fh)
        nFpO = nFpO[0] + nFpO[1]
        
        # Create the FrameBuffer instance
        frameBuffer = buffer.TBNFrameBuffer(stands=range(1,nFpO//2+1), pols=[0, 1], ReorderFrames=True)
        
        # Go
        while True:
            try:
                cFrame = tbn.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                continue
                
            frameBuffer.append(cFrame)
            cFrames = frameBuffer.get()
            
            if cFrames is None:
                continue
                
        fh.close()
        
        # Flush the buffer
        for cFrames in frameBuffer.flush():
            # Make sure the dump has one of the expected time tags
            self.assertTrue(cFrames[0].data.timeTag in (119196674956800, 119196675960320))
            
            # Make sure it has the right number of frames
            self.assertEqual(len(cFrames), nFpO)
            
            # Check the order
            for i in xrange(1, len(cFrames)):
                pS, pP = cFrames[i-1].parseID()
                cS, cP = cFrames[i].parseID()
                
                pID = pS*2 + pP
                cID = cS*2 + cP
                self.assertTrue(cID > pID)
                
    #
    # DRX
    #
    
    def test_drx_basic(self):
        """Test the DRX ring buffer."""
        
        fh = open(drxFile, 'rb')
        junkFrame = drx.readFrame(fh)
        b,t,p = junkFrame.parseID()
        fh.seek(-drx.FrameSize, 1)
        
        # Create the FrameBuffer instance
        frameBuffer = buffer.DRXFrameBuffer(beams=[b,], tunes=[1, 2], pols=[0, 1], nSegments=2)
        
        # Go
        dumped = []
        while True:
            try:
                cFrame = drx.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                continue

            frameBuffer.append(cFrame)
            cFrames = frameBuffer.get()

            if cFrames is None:
                continue
                
            dumped.append( cFrames[0].data.timeTag )
            
        fh.close()
        
        # Make sure we have the right number of frames in the buffer
        nFrames = 0
        for key in frameBuffer.buffer.keys():
            nFrames = nFrames + len(frameBuffer.buffer[key])
        self.assertEqual(nFrames, 1)
        self.assertEqual(nFrames+len(dumped)*4, 32+1)
        
        # Make sure nothing has happened that shouldn't have
        self.assertEqual(frameBuffer.full,    7)
        self.assertEqual(frameBuffer.partial, 1)
        self.assertEqual(frameBuffer.missing, 1)
        self.assertEqual(frameBuffer.dropped, 0)
        
        # Make sure we have the right keys
        for key in dumped:
            self.assertTrue(key in (257355782095018376, 257355782095059336, 257355782095100296, 257355782095141256, 257355782095182216, 257355782095223176, 257355782095264136, 257355782095305096))
            
        for key in frameBuffer.buffer.keys():
            self.assertTrue(key in (257355782095346056,))
        
        # Make sure the buffer keys have the right sizes
        self.assertEqual(len(frameBuffer.buffer[257355782095346056]), 1)
        
    def test_drx_reorder(self):
        """Test the reorder function of the TBN ring buffer."""
        
        fh = open(drxFile, 'rb')
        junkFrame = drx.readFrame(fh)
        b,t,p = junkFrame.parseID()
        fh.seek(-drx.FrameSize, 1)
        
        # Create the FrameBuffer instance
        frameBuffer = buffer.DRXFrameBuffer(beams=[b,], tunes=[1, 2], pols=[0, 1], nSegments=2, ReorderFrames=True)
        
        # Go
        while True:
            try:
                cFrame = drx.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                continue

            frameBuffer.append(cFrame)
            cFrames = frameBuffer.get()

            if cFrames is None:
                continue
                
            # Make sure it has the right number of frames
            self.assertEqual(len(cFrames), 4)
            
            # Check the order
            for i in xrange(1, len(cFrames)):
                pB, pT, pP = cFrames[i-1].parseID()
                cB, cT, cP = cFrames[i].parseID()
                
                pID = 4*pB + 2*(pT-1) + pP
                cID = 4*cB + 2*(cT-1) + cP
                self.assertTrue(cID > pID)
                
        fh.close()
        
    def test_drx_buffer_flush(self):
        """Test the DRX ring buffer's flush() function."""
        
        fh = open(drxFile, 'rb')
        junkFrame = drx.readFrame(fh)
        b,t,p = junkFrame.parseID()
        fh.seek(-drx.FrameSize, 1)
        
        # Create the FrameBuffer instance
        frameBuffer = buffer.DRXFrameBuffer(beams=[b,], tunes=[1, 2], pols=[0, 1], nSegments=2)
        
        # Go
        while True:
            try:
                cFrame = drx.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                continue

            frameBuffer.append(cFrame)
            cFrames = frameBuffer.get()

            if cFrames is None:
                continue
                
        fh.close()
        
        # Flush the buffer
        for cFrames in frameBuffer.flush():
            # Make sure the dump has one of the expected time tags
            self.assertTrue(cFrames[0].data.timeTag in (257355782095346056,))
            
            # Make sure it has the right number of frames
            self.assertEqual(len(cFrames), 4)
            
    def test_drx_buffer_reorder_flush(self):
        """Test the DRX ring buffer's flush() function with reordering."""
        
        fh = open(drxFile, 'rb')
        junkFrame = drx.readFrame(fh)
        b,t,p = junkFrame.parseID()
        fh.seek(-drx.FrameSize, 1)
        
        # Create the FrameBuffer instance
        frameBuffer = buffer.DRXFrameBuffer(beams=[b,], tunes=[1, 2], pols=[0, 1], nSegments=2, ReorderFrames=True)
        
        # Go
        while True:
            try:
                cFrame = drx.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                continue

            frameBuffer.append(cFrame)
            cFrames = frameBuffer.get()

            if cFrames is None:
                continue
                
            # Make sure it has the right number of frames
            self.assertEqual(len(cFrames), 4)
            
            # Check the order
            for i in xrange(1, len(cFrames)):
                pB, pT, pP = cFrames[i-1].parseID()
                cB, cT, cP = cFrames[i].parseID()
                
                pID = 4*pB + 2*(pT-1) + pP
                cID = 4*cB + 2*(cT-1) + cP
                self.assertTrue(cID > pID)
                
        fh.close()
        
        # Flush the buffer
        for cFrames in frameBuffer.flush():
            # Make sure the dump has one of the expected time tags
            self.assertTrue(cFrames[0].data.timeTag in (257355782095346056,))
            
            # Make sure it has the right number of frames
            self.assertEqual(len(cFrames), 4)
            
            # Check the order
            for i in xrange(1, len(cFrames)):
                pB, pT, pP = cFrames[i-1].parseID()
                cB, cT, cP = cFrames[i].parseID()
                
                pID = 4*pB + 2*(pT-1) + pP
                cID = 4*cB + 2*(cT-1) + cP
                self.assertTrue(cID > pID)
                
    #
    # TBF
    #
    
    def test_tbf_default(self):
        """Test the TBF ring buffer with the default values."""
        
        fh = open(tbfFile, 'rb')
        nFpO = tbf.getFramesPerObs(fh)
        
        # Create the FrameBuffer instance
        frameBuffer = buffer.TBFFrameBuffer(chans=[2348, 2360, 2372, 2384, 2396])
        
        # Go
        while True:
            try:
                cFrame = tbf.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                continue
                
            frameBuffer.append(cFrame)
            cFrames = frameBuffer.get()
            
            if cFrames is None:
                continue
            
        fh.close()
        
        # Make sure we have the right number of frames in the buffer
        nFrames = 0
        for key in frameBuffer.buffer.keys():
            nFrames = nFrames + len(frameBuffer.buffer[key])
        self.assertEqual(nFrames, 5)
        
        # Make sure nothing has happened that shouldn't have
        self.assertEqual(frameBuffer.full,    0)
        self.assertEqual(frameBuffer.partial, 0)
        self.assertEqual(frameBuffer.missing, 0)
        self.assertEqual(frameBuffer.dropped, 0)
        
        # Make sure we have the right keys
        for key in frameBuffer.buffer.keys():
            self.assertTrue(key in (283685766952000000,))
            
        # Make sure the buffer keys have the right sizes
        self.assertEqual(len(frameBuffer.buffer[283685766952000000]), 5)
        
    def test_tbf_small(self):
        """Test a small version of the TBF ring buffer."""
        
        fh = open(tbfFile, 'rb')
        nFpO = tbf.getFramesPerObs(fh)
        
        # Create the FrameBuffer instance
        frameBuffer = buffer.TBFFrameBuffer(chans=[2348, 2360, 2372, 2384, 2396], nSegments=1)
        
        # Go
        while True:
            try:
                cFrame = tbf.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                continue
                
            frameBuffer.append(cFrame)
            cFrames = frameBuffer.get()
            
            if cFrames is None:
                continue
                
            # Make sure the dump has one of the expected time tags
            self.assertTrue(cFrames[0].data.timeTag in (283685766952000000,))
            
            # Make sure it has the right number of frames
            self.assertEqual(len(cFrames), nFpO)
            
        fh.close()
        
    def test_tbf_buffer_reorder(self):
        """Test the reorder function of the TBF ring buffer."""
        
        fh = open(tbfFile, 'rb')
        nFpO = tbf.getFramesPerObs(fh)
        
        # Create the FrameBuffer instance
        frameBuffer = buffer.TBFFrameBuffer(chans=[2348, 2360, 2372, 2384, 2396], ReorderFrames=True)
        
        # Go
        while True:
            try:
                cFrame = tbf.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                continue
                
            frameBuffer.append(cFrame)
            cFrames = frameBuffer.get()
            
            if cFrames is None:
                continue
                
            # Make sure the dump has one of the expected time tags
            self.assertTrue(cFrames[0].data.timeTag in (283685766952000000,))
            
            # Make sure it has the right number of frames
            self.assertEqual(len(cFrames), nFpO)
            
            # Check the order
            for i in xrange(1, len(cFrames)):
                pC = cFrames[i-1].header.firstChan
                cC = cFrames[i].header.firstChan
                
                self.assertTrue(cC > pC)
                
        fh.close()
        
    def test_tbf_buffer_flush(self):
        """Test the TBF ring buffer's flush() function."""
        
        fh = open(tbfFile, 'rb')
        nFpO = tbf.getFramesPerObs(fh)
        
        # Create the FrameBuffer instance
        frameBuffer = buffer.TBFFrameBuffer(chans=[2348, 2360, 2372, 2384, 2396])
        
        # Go
        while True:
            try:
                cFrame = tbf.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                continue
                
            frameBuffer.append(cFrame)
            cFrames = frameBuffer.get()
            
            if cFrames is None:
                continue
                
        fh.close()
        
        # Flush the buffer
        for cFrames in frameBuffer.flush():
            # Make sure the dump has one of the expected time tags
            self.assertTrue(cFrames[0].data.timeTag in (283685766952000000,))
            
            # Make sure it has the right number of frames
            self.assertEqual(len(cFrames), nFpO)
            
    def test_tbf_buffer_reorder_flush(self):
        """Test the TBF ring buffer's flush() function with reordering."""
        
        fh = open(tbfFile, 'rb')
        nFpO = tbf.getFramesPerObs(fh)
        
        # Create the FrameBuffer instance
        frameBuffer = buffer.TBFFrameBuffer(chans=[2348, 2360, 2372, 2384, 2396], ReorderFrames=True)
        
        # Go
        while True:
            try:
                cFrame = tbf.readFrame(fh)
            except errors.eofError:
                break
            except errors.syncError:
                continue
                
            frameBuffer.append(cFrame)
            cFrames = frameBuffer.get()
            
            if cFrames is None:
                continue
                
        fh.close()
        
        # Flush the buffer
        for cFrames in frameBuffer.flush():
            # Make sure the dump has one of the expected time tags
            self.assertTrue(cFrames[0].data.timeTag in (283685766952000000,))
            
            # Make sure it has the right number of frames
            self.assertEqual(len(cFrames), nFpO)
            
            # Check the order
            for i in xrange(1, len(cFrames)):
                pC = cFrames[i-1].header.firstChan
                cC = cFrames[i].header.firstChan
                
                self.assertTrue(cC > pC)


class buffer_test_suite(unittest.TestSuite):
    """A unittest.TestSuite class which contains all of the lsl.reader.buffer 
    unit tests."""
    
    def __init__(self):
        unittest.TestSuite.__init__(self)
        
        loader = unittest.TestLoader()
        self.addTests(loader.loadTestsFromTestCase(buffer_tests)) 


if __name__ == '__main__':
    unittest.main()
