# -*- coding: utf-8 -*-

"""Unit test for lsl.common.metabundle"""

import os
import unittest

from lsl.common import metabundle
from lsl.common.paths import dataBuild as dataPath


__revision__ = "$Rev: 3046 $"
__version__  = "0.4"
__author__    = "Jayce Dowell"

mdbFile = os.path.join(dataPath, 'tests', 'metadata.tgz')
mdbFileOld0 = os.path.join(dataPath, 'tests', 'metadata-old-0.tgz')
mdbFileOld1 = os.path.join(dataPath, 'tests', 'metadata-old-1.tgz')
mdbFileADP = os.path.join(dataPath, 'tests', 'metadata-adp.tgz')
mdbFileGDB = os.path.join(dataPath, 'tests', 'metadata-gdb.tgz')
mdbFileGDBOld0 = os.path.join(dataPath, 'tests', 'metadata-gdb-old-0.tgz')

class metabundle_tests(unittest.TestCase):
    """A unittest.TestCase collection of unit tests for the lsl.common.metabundle
    module."""
    
    def test_ss(self):
        """Test the session specification utilties."""
        
        ses = metabundle.getSessionSpec(mdbFile)
        obs = metabundle.getObservationSpec(mdbFile)
        
        # Check session start time
        self.assertEqual(ses['MJD'], 56742)
        self.assertEqual(ses['MPM'], 4914000)
        
        # Check the duration
        self.assertEqual(ses['Dur'], obs[0]['Dur'] + 10000)
        
        # Check the number of observations
        self.assertEqual(ses['nObs'], len(obs))
    
    def test_os(self):
        """Test the observation specification utilities."""
        
        obs1 = metabundle.getObservationSpec(mdbFile)
        obs2 = metabundle.getObservationSpec(mdbFile, selectObs=1)
        
        # Check if the right observation is returned
        self.assertEqual(obs1[0], obs2)
        
        # Check the mode
        self.assertEqual(obs2['Mode'], 1)
        
        # Check the time
        self.assertEqual(obs2['MJD'], 56742)
        self.assertEqual(obs2['MPM'], 4919000)
        
    def test_cs(self):
        """Test the command script utilities."""
        
        cmnds = metabundle.getCommandScript(mdbFile)
        
        # Check number of command
        self.assertEqual(len(cmnds), 150)
        
        # Check the first and last commands
        self.assertEqual(cmnds[ 0]['commandID'], 'NUL')
        self.assertEqual(cmnds[-2]['commandID'], 'OBE')
        self.assertEqual(cmnds[-1]['commandID'], 'ESN')
        
        # Check the counds of DP BAM commands
        nBAM = 0
        for cmnd in cmnds:
            if cmnd['commandID'] == 'BAM':
                nBAM += 1
        self.assertEqual(nBAM, 143)
        
    def test_sm(self):
        """Test the session metadata utilties."""
        
        sm = metabundle.getSessionMetaData(mdbFile)
        
        # Make sure all of the observations are done
        self.assertEqual(len(sm.keys()), 1)
        
    def test_sdf(self):
        """Test building a SDF from a tarball."""
        
        sdf = metabundle.getSessionDefinition(mdbFile)
        
    def test_sdm(self):
        """Test the station dynamic MIB utilties."""
        
        sm = metabundle.getSDM(mdbFile)
        
    def test_metadata(self):
        """Test the observation metadata utility."""
        
        fileInfo = metabundle.getSessionMetaData(mdbFile)
        self.assertEqual(len(fileInfo.keys()), 1)
        
        # File tag
        self.assertEqual(fileInfo[1]['tag'], '056742_000440674')
        
        # DRSU barcode
        self.assertEqual(fileInfo[1]['barcode'], 'S15TCV23S0001')
        
    def test_aspconfig(self):
        """Test retrieving the ASP configuration."""
        
        # Beginning config.
        aspConfig = metabundle.getASPConfigurationSummary(mdbFile, which='beginning')
        self.assertEqual(aspConfig['filter'],  1)
        self.assertEqual(aspConfig['at1'],    13)
        self.assertEqual(aspConfig['at2'],    13)
        self.assertEqual(aspConfig['atsplit'],15)
        
        # End config.
        aspConfig = metabundle.getASPConfigurationSummary(mdbFile, which='End')
        self.assertEqual(aspConfig['filter'],  1)
        self.assertEqual(aspConfig['at1'],    13)
        self.assertEqual(aspConfig['at2'],    13)
        self.assertEqual(aspConfig['atsplit'],15)
        
        # Unknown code
        self.assertRaises(ValueError, metabundle.getASPConfigurationSummary, mdbFile, 'middle')
        
    def test_is_valid(self):
        """Test whether or not isValid works."""
        
        self.assertTrue(metabundle.isValid(mdbFile))
        
    def test_is_not_valid(self):
        """Test whether or not isValid works on LWA-SV files."""
        
        self.assertFalse(metabundle.isValid(mdbFileADP))
        self.assertFalse(metabundle.isValid(mdbFileGDB))
        self.assertFalse(metabundle.isValid(mdbFileGDBOld0))


class metabundle_tests_old_0(unittest.TestCase):
    """A unittest.TestCase collection of unit tests for the lsl.common.metabundle
    module based on the tarball format supported in LSL 0.5.x."""
    
    def test_ss(self):
        """Test the session specification utilties."""
        
        ses = metabundle.getSessionSpec(mdbFileOld0)
        obs = metabundle.getObservationSpec(mdbFileOld0)
        
        # Check session start time
        self.assertEqual(ses['MJD'], 56013)
        self.assertEqual(ses['MPM'], 25855000)
        
        # Check the duration
        self.assertEqual(ses['Dur'], obs[0]['Dur'] + 10000)
        
        # Check the number of observations
        self.assertEqual(ses['nObs'], len(obs))
        
    def test_os(self):
        """Test the observation specification utilities."""
        
        obs1 = metabundle.getObservationSpec(mdbFileOld0)
        obs2 = metabundle.getObservationSpec(mdbFileOld0, selectObs=1)
        
        # Check if the right observation is returned
        self.assertEqual(obs1[0], obs2)
        
        # Check the mode
        self.assertEqual(obs2['Mode'], 1)
        
        # Check the time
        self.assertEqual(obs2['MJD'], 56013)
        self.assertEqual(obs2['MPM'], 25860000)
        
    def test_cs(self):
        """Test the command script utilities."""
        
        cmnds = metabundle.getCommandScript(mdbFileOld0)
        
        # Check number of command
        self.assertEqual(len(cmnds), 491)
        
        # Check the first and last commands
        self.assertEqual(cmnds[ 0]['commandID'], 'NUL')
        self.assertEqual(cmnds[-2]['commandID'], 'OBE')
        self.assertEqual(cmnds[-1]['commandID'], 'ESN')
        
        # Check the counds of DP BAM commands
        nBAM = 0
        for cmnd in cmnds:
            if cmnd['commandID'] == 'BAM':
                nBAM += 1
        self.assertEqual(nBAM, 484)
        
    def test_sm(self):
        """Test the session metadata utilties."""
        
        sm = metabundle.getSessionMetaData(mdbFileOld0)
        
        # Make sure all of the observations are done
        self.assertEqual(len(sm.keys()), 1)
        
    def test_sdf(self):
        """Test building a SDF from a tarball."""
        
        sdf = metabundle.getSessionDefinition(mdbFileOld0)
        
    def test_sdm(self):
        """Test the station dynamic MIB utilties."""
        
        sm = metabundle.getSDM(mdbFileOld0)
        
    def test_is_valid(self):
        """Test whether or not isValid works."""
        
        self.assertTrue(metabundle.isValid(mdbFileOld0))


class metabundle_tests_old_1(unittest.TestCase):
    """A unittest.TestCase collection of unit tests for the lsl.common.metabundle
    module."""
    
    def test_ss(self):
        """Test the session specification utilties."""
        
        ses = metabundle.getSessionSpec(mdbFileOld1)
        obs = metabundle.getObservationSpec(mdbFileOld1)
        
        # Check session start time
        self.assertEqual(ses['MJD'], 56492)
        self.assertEqual(ses['MPM'], 68995000)
        
        # Check the duration
        self.assertEqual(ses['Dur'], obs[0]['Dur'] + 10000)
        
        # Check the number of observations
        self.assertEqual(ses['nObs'], len(obs))
        
    def test_os(self):
        """Test the observation specification utilities."""
        
        obs1 = metabundle.getObservationSpec(mdbFileOld1)
        obs2 = metabundle.getObservationSpec(mdbFileOld1, selectObs=1)
        
        # Check if the right observation is returned
        self.assertEqual(obs1[0], obs2)
        
        # Check the mode
        self.assertEqual(obs2['Mode'], 1)
        
        # Check the time
        self.assertEqual(obs2['MJD'], 56492)
        self.assertEqual(obs2['MPM'], 69000000)
        
    def test_cs(self):
        """Test the command script utilities."""
        
        cmnds = metabundle.getCommandScript(mdbFileOld1)
        
        # Check number of command
        self.assertEqual(len(cmnds), 8)
        
        # Check the first and last commands
        self.assertEqual(cmnds[ 0]['commandID'], 'NUL')
        self.assertEqual(cmnds[-2]['commandID'], 'OBE')
        self.assertEqual(cmnds[-1]['commandID'], 'ESN')
        
        # Check the counds of DP BAM commands
        nBAM = 0
        for cmnd in cmnds:
            if cmnd['commandID'] == 'BAM':
                nBAM += 1
        self.assertEqual(nBAM, 1)
        
    def test_sm(self):
        """Test the session metadata utilties."""
        
        sm = metabundle.getSessionMetaData(mdbFileOld1)
        
        # Make sure all of the observations are done
        self.assertEqual(len(sm.keys()), 1)
        
    def test_sdf(self):
        """Test building a SDF from a tarball."""
        
        sdf = metabundle.getSessionDefinition(mdbFileOld1)
        
    def test_sdm(self):
        """Test the station dynamic MIB utilties."""
        
        sm = metabundle.getSDM(mdbFileOld1)
        
    def test_metadata(self):
        """Test the observation metadata utility."""
        
        fileInfo = metabundle.getSessionMetaData(mdbFileOld1)
        self.assertEqual(len(fileInfo.keys()), 1)
        
        # File tag
        self.assertEqual(fileInfo[1]['tag'], '056492_000000094')
        
        # DRSU barcode
        self.assertEqual(fileInfo[1]['barcode'], 'S10TCC13S0007')
        
    def test_aspconfig(self):
        """Test retrieving the ASP configuration."""
        
        # Beginning config.
        aspConfig = metabundle.getASPConfigurationSummary(mdbFileOld1, which='beginning')
        self.assertEqual(aspConfig['filter'],  3)
        self.assertEqual(aspConfig['at1'],     0)
        self.assertEqual(aspConfig['at2'],     0)
        self.assertEqual(aspConfig['atsplit'], 0)
        
        # End config.
        aspConfig = metabundle.getASPConfigurationSummary(mdbFileOld1, which='End')
        self.assertEqual(aspConfig['filter'],  1)
        self.assertEqual(aspConfig['at1'],    13)
        self.assertEqual(aspConfig['at2'],    13)
        self.assertEqual(aspConfig['atsplit'], 0)
        
        # Unknown code
        self.assertRaises(ValueError, metabundle.getASPConfigurationSummary, mdbFileOld1, 'middle')
        
    def test_is_valid(self):
        """Test whether or not isValid works."""
        
        self.assertTrue(metabundle.isValid(mdbFileOld1))


class metabundle_test_suite(unittest.TestSuite):
    """A unittest.TestSuite class which contains all of the lsl.common.metabundle
    module unit tests."""
    
    def __init__(self):
        unittest.TestSuite.__init__(self)
        
        loader = unittest.TestLoader()
        self.addTests(loader.loadTestsFromTestCase(metabundle_tests))        
        self.addTests(loader.loadTestsFromTestCase(metabundle_tests_old_0))
        self.addTests(loader.loadTestsFromTestCase(metabundle_tests_old_1))
        
if __name__ == '__main__':
    unittest.main()
