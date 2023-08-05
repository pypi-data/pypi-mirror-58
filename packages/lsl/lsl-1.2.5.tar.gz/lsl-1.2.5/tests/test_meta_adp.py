# -*- coding: utf-8 -*-

"""Unit test for lsl.common.metabundle"""

import os
import unittest

from lsl.common import metabundleADP
from lsl.common.paths import dataBuild as dataPath


__revision__ = "$Rev: 3046 $"
__version__  = "0.1"
__author__    = "Jayce Dowell"

mdbFile = os.path.join(dataPath, 'tests', 'metadata.tgz')
mdbFileOld0 = os.path.join(dataPath, 'tests', 'metadata-old-0.tgz')
mdbFileOld1 = os.path.join(dataPath, 'tests', 'metadata-old-1.tgz')
mdbFileADP = os.path.join(dataPath, 'tests', 'metadata-adp.tgz')
mdbFileGDB = os.path.join(dataPath, 'tests', 'metadata-gdb.tgz')
mdbFileGDBOld0 = os.path.join(dataPath, 'tests', 'metadata-gdb-old-0.tgz')


class metabundle_tests_adp(unittest.TestCase):
    """A unittest.TestCase collection of unit tests for the lsl.common.metabundle
    module."""
    
    def test_ss(self):
        """Test the session specification utilties."""
        
        ses = metabundleADP.getSessionSpec(mdbFileADP)
        obs = metabundleADP.getObservationSpec(mdbFileADP)
        
        # Check session start time
        self.assertEqual(ses['MJD'], 57774)
        self.assertEqual(ses['MPM'], 29970000)
        
        # Check the duration
        self.assertEqual(ses['Dur'], obs[0]['Dur'] + 10000)
        
        # Check the number of observations
        self.assertEqual(ses['nObs'], len(obs))
    
    def test_os(self):
        """Test the observation specification utilities."""
        
        obs1 = metabundleADP.getObservationSpec(mdbFileADP)
        obs2 = metabundleADP.getObservationSpec(mdbFileADP, selectObs=1)
        
        # Check if the right observation is returned
        self.assertEqual(obs1[0], obs2)
        
        # Check the mode
        self.assertEqual(obs2['Mode'], 1)
        
        # Check the time
        self.assertEqual(obs2['MJD'], 57774)
        self.assertEqual(obs2['MPM'], 29975000)
        
    def test_cs(self):
        """Test the command script utilities."""
        
        cmnds = metabundleADP.getCommandScript(mdbFileADP)
        
        # Check number of command
        self.assertEqual(len(cmnds), 50)
        
        # Check the first and last commands
        self.assertEqual(cmnds[ 0]['commandID'], 'NUL')
        self.assertEqual(cmnds[-2]['commandID'], 'STP')
        self.assertEqual(cmnds[-1]['commandID'], 'ESN')
        
        # Check the counds of DP BAM commands
        nBAM = 0
        for cmnd in cmnds:
            if cmnd['commandID'] == 'BAM':
                nBAM += 1
        self.assertEqual(nBAM, 40)
        
    def test_sm(self):
        """Test the session metadata utilties."""
        
        sm = metabundleADP.getSessionMetaData(mdbFileADP)
        
        # Make sure all of the observations are done
        self.assertEqual(len(sm.keys()), 1)
        
    def test_sdf(self):
        """Test building a SDF from a tarball."""
        
        sdf = metabundleADP.getSessionDefinition(mdbFileADP)
        
    def test_sdm(self):
        """Test the station dynamic MIB utilties."""
        
        sm = metabundleADP.getSDM(mdbFileADP)
        
    def test_metadata(self):
        """Test the observation metadata utility."""
        
        fileInfo = metabundleADP.getSessionMetaData(mdbFileADP)
        self.assertEqual(len(fileInfo.keys()), 1)
        
        # File tag
        self.assertEqual(fileInfo[1]['tag'], '057774_000770030')
        
        # DRSU barcode
        self.assertEqual(fileInfo[1]['barcode'], 'S10TCC13S0016')
        
    def test_aspconfig(self):
        """Test retrieving the ASP configuration."""
        
        # Beginning config.
        aspConfig = metabundleADP.getASPConfigurationSummary(mdbFileADP, which='beginning')
        self.assertEqual(aspConfig['filter'],  0)
        self.assertEqual(aspConfig['at1'],     6)
        self.assertEqual(aspConfig['at2'],     5)
        self.assertEqual(aspConfig['atsplit'],15)
        
        # End config.
        aspConfig = metabundleADP.getASPConfigurationSummary(mdbFileADP, which='End')
        self.assertEqual(aspConfig['filter'],  0)
        self.assertEqual(aspConfig['at1'],     6)
        self.assertEqual(aspConfig['at2'],     5)
        self.assertEqual(aspConfig['atsplit'],15)
        
        # Unknown code
        self.assertRaises(ValueError, metabundleADP.getASPConfigurationSummary, mdbFileADP, 'middle')
        
    def test_aspconfig_gdbm(self):
        """Test retrieving the ASP configuration from a GDBM MIB."""
        
        # Beginning config.
        aspConfig = metabundleADP.getASPConfigurationSummary(mdbFileGDB, which='beginning')
        self.assertEqual(aspConfig['filter'],  0)
        self.assertEqual(aspConfig['at1'],     6)
        self.assertEqual(aspConfig['at2'],     5)
        self.assertEqual(aspConfig['atsplit'],15)
        
        # End config.
        aspConfig = metabundleADP.getASPConfigurationSummary(mdbFileGDB, which='End')
        self.assertEqual(aspConfig['filter'],  0)
        self.assertEqual(aspConfig['at1'],     6)
        self.assertEqual(aspConfig['at2'],     5)
        self.assertEqual(aspConfig['atsplit'],15)
        
        # Unknown code
        self.assertRaises(ValueError, metabundleADP.getASPConfigurationSummary, mdbFileGDB, 'middle')
        
    def test_is_valid(self):
        """Test whether or not isValid works."""
        
        self.assertTrue(metabundleADP.isValid(mdbFileADP))
        self.assertTrue(metabundleADP.isValid(mdbFileGDB))
        self.assertTrue(metabundleADP.isValid(mdbFileGDBOld0))
        
    def test_is_not_valid(self):
        """Test whether or not isValid works on LWA1 files."""
        
        self.assertFalse(metabundleADP.isValid(mdbFile))
        self.assertFalse(metabundleADP.isValid(mdbFileOld0))
        self.assertFalse(metabundleADP.isValid(mdbFileOld1))


class metabundle_adp_test_suite(unittest.TestSuite):
    """A unittest.TestSuite class which contains all of the lsl.common.metabundleADP
    module unit tests."""
    
    def __init__(self):
        unittest.TestSuite.__init__(self)
        
        loader = unittest.TestLoader()
        self.addTests(loader.loadTestsFromTestCase(metabundle_tests_adp))
        
if __name__ == '__main__':
    unittest.main()
