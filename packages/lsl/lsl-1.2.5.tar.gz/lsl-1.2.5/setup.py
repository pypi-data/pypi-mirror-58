# -*- coding: utf-8 -*

# Python3 compatibility
from __future__ import print_function

import os
import imp
import sys
import glob
import tempfile
import unittest
import platform
import warnings
import subprocess
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from setuptools import setup, Command, Extension, Distribution, find_packages, __version__ as stv
from distutils import log
from distutils.command.build import build
try:
    # Attempt to use Cython for building extensions, if available
    from Cython.Distutils.build_ext import build_ext
    # Additionally, assert that the compiler module will load
    # also. Ref #1229.
    __import__('Cython.Compiler.Main')
except ImportError:
    from distutils.command.build_ext import build_ext
    
try:
    import numpy
except ImportError:
    pass
try:
    import multiprocessing
except ImportError:
    pass
import logging


def get_version():
    """Read the VERSION file and return the version number as a string."""

    return open('VERSION').read().strip()


def get_description(filename):
    """Read in a README-type file and return the contents of the DESCRIPTION
    section."""

    desc = ''
    fh = open(filename, 'r')
    lines = fh.readlines()
    fh.close()

    inDescription = False
    for line in lines:
        if line.find('DESCRIPTION') == 0:
            inDescription = True
            continue
        if line.find('REQUIREMENTS') == 0:
            inDescription = False
            break
        if inDescription:
            if line[:3] == '---':
                continue
            desc = ''.join([desc, line])

    return desc


def get_openmp():
    """Try to compile/link an example program to check for OpenMP support.
    
    Based on:
    1) http://stackoverflow.com/questions/16549893/programatically-testing-for-openmp-support-from-a-python-setup-script
    2) https://github.com/lpsinger/healpy/blob/6c3aae58b5f3281e260ef7adce17b1ffc68016f0/setup.py
    """
    
    import shutil
    from distutils import sysconfig
    from distutils import ccompiler
    compiler = ccompiler.new_compiler()
    sysconfig.get_config_vars()
    sysconfig.customize_compiler(compiler)
    cc = compiler.compiler
    
    tmpdir = tempfile.mkdtemp()
    curdir = os.getcwd()
    os.chdir(tmpdir)
    
    fh = open('test.c', 'w')
    fh.write(r"""#include <omp.h>
#include <stdio.h>
int main(void) {
#pragma omp parallel
printf("Hello from thread %d, nthreads %d\n", omp_get_thread_num(), omp_get_num_threads());
return 0;
}
""")
    fh.close()
    
    ccmd = []
    ccmd.extend( cc )
    ccmd.extend( ['-fopenmp', 'test.c', '-o test'] )
    if os.path.basename(cc[0]).find('gcc') != -1:
        ccmd.append( '-lgomp' )
    elif os.path.basename(cc[0]).find('clang') != -1:
        ccmd.extend( ['-L/opt/local/lib/libomp', '-lomp'] )
    try:
        output = subprocess.check_call(ccmd)
        outCFLAGS = ['-fopenmp',]
        outLIBS = []
        if os.path.basename(cc[0]).find('gcc') != -1:
            outLIBS.append( '-lgomp' )
        elif os.path.basename(cc[0]).find('clang') != -1:
            outLIBS.extend( ['-L/opt/local/lib/libomp', '-lomp'] )
            
    except subprocess.CalledProcessError:
        print("WARNING:  OpenMP does not appear to be supported by %s, disabling" % cc[0])
        outCFLAGS = []
        outLIBS = []
        
    finally:
        os.chdir(curdir)
        shutil.rmtree(tmpdir)
        
    return outCFLAGS, outLIBS


def get_fftw():
    """Use pkg-config (if installed) to figure out the C flags and linker flags
    needed to compile a C program with FFTW3 (floating point version).  If FFTW3 
    cannot be found via pkg-config, some 'sane' values are returned."""
    
    try:
        subprocess.check_call(['pkg-config', 'fftw3f', '--exists'])
        
        p = subprocess.Popen(['pkg-config', 'fftw3f', '--modversion'], stdout=subprocess.PIPE)
        outVersion = p.communicate()[0].rstrip().split()
        
        p = subprocess.Popen(['pkg-config', 'fftw3f', '--cflags'], stdout=subprocess.PIPE)
        outCFLAGS = p.communicate()[0].rstrip().split()
        try:
            outCFLAGS = [str(v, 'utf-8') for v in outCFLAGS]
        except TypeError:
            pass
        
        p = subprocess.Popen(['pkg-config', 'fftw3f', '--libs'], stdout=subprocess.PIPE)
        outLIBS = p.communicate()[0].rstrip().split()
        try:
            outLIBS = [str(v, 'utf-8') for v in outLIBS]
        except TypeError:
            pass
            
        if len(outVersion) > 0:
            print("Found FFTW3, version %s" % outVersion[0])
            
    except (OSError, subprocess.CalledProcessError):
        print("WARNING:  FFTW3 cannot be found, using defaults")
        outCFLAGS = []
        outLIBS = ['-lfftw3f', '-lm']
        
    return outCFLAGS, outLIBS


def get_atlas():
    """Use NumPy's system_info module to find the location of ATLAS (and 
    cblas)."""
    
    from numpy.distutils.system_info import get_info
    
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore",category=DeprecationWarning)
        sys.stdout = StringIO()
        atlas_info = get_info('atlas_blas', notfound_action=2)
        sys.stdout = sys.__stdout__
        
    atlas_version = ([v[3:-3] for k,v in atlas_info.get('define_macros',[])
                    if k == 'ATLAS_INFO']+[None])[0]
    if atlas_version:
        print("Found ATLAS, version %s" % atlas_version)
        
    try:
        outCFLAGS = ['-I%s' % idir for idir in atlas_info['include_dirs']]
    except KeyError:
        outCFLAGS = []
    try:
        outLIBS = ['-L%s' % ldir for ldir in atlas_info['library_dirs']]
    except KeyError:
        outLIBS = []
    try:
        outLIBS.extend(['-l%s' % lib for lib in atlas_info['libraries']])
    except KeyError:
        pass
        
    return outCFLAGS, outLIBS


def write_version_info():
    """Write the version info to a module in LSL."""
    
    lslVersion = get_version()
    shortVersion = '.'.join(lslVersion.split('.')[:2])
    
    contents = """# -*- coding: utf-8 -*-
# This file is automatically generated by setup.py

import os
import glob
import hashlib

def _get_md5(filename, blockSize=262144):
    with open(filename, 'rb') as fh:
        m = hashlib.md5()
        while True:
            block = fh.read(blockSize)
            if len(block) == 0:
                break
            m.update(block)
            
    return m.hexdigest()

def get_fingerprint():
    \"\"\"
    Return a 'fingerprint' of the current LSL module state that is useful for
    tracking if the module has changed.
    \"\"\"
    
    filenames = []
    for ext in ('.py', '.so'):
        filenames.extend( glob.glob(os.path.join(os.path.dirname(__file__), '*%%s' %% ext)) )
        filenames.extend( glob.glob(os.path.join(os.path.dirname(__file__), '*', '*%%s' %% ext)) )
        
    m = hashlib.md5()
    for filename in filenames:
        m.update(_get_md5(filename))
    return m.hexdigest()

version = '%s'
full_version = '%s'
short_version = '%s'

""" % (lslVersion, lslVersion, shortVersion)
    
    fh = open('lsl/version.py', 'w')
    fh.write(contents)
    fh.close()
    
    return True


# Get the FFTW flags/libs and manipulate the flags and libraries for 
# correlator._core appropriately.  This will, hopefully, fix the build
# problems on Mac
class lsl_build(build):
    user_options = build.user_options \
                   + [('with-atlas=', None, 'Installation path for ATLAS'),] \
                   + [('with-fftw=', None, 'Installation path for FFTW'),]
    
    def initialize_options(self, *args, **kwargs):
        build.initialize_options(self, *args, **kwargs)
        self.with_atlas = None
        self.with_fftw = None
        
    def finalize_options(self, *args, **kwargs):
        build.finalize_options(self, *args, **kwargs)
        
        if self.distribution.has_ext_modules():
            ## Grab the 'build_ext' command
            beco = self.distribution.get_command_obj('build_ext')
            
            ## Grab the ATLAS flags
            if self.with_atlas is not None:
                beco.with_atlas = self.with_atlas
                
            ## Grab the FFTW flags
            if self.with_fftw is not None:
                beco.with_fftw = self.with_fftw


class lsl_build_ext(build_ext):
    user_options = build_ext.user_options \
                   + [('with-atlas=', None, 'Installation path for ATLAS'),] \
                   + [('with-fftw=', None, 'Installation path for FFTW'),]
    
    def initialize_options(self, *args, **kwargs):
        build_ext.initialize_options(self, *args, **kwargs)
        self.with_atlas = None
        self.with_fftw = None
        
    def finalize_options(self, *args, **kwargs):
        build_ext.finalize_options(self, *args, **kwargs)
        self.verbose = True
        
        ## Grab the OpenMP flags
        openmpFlags, openmpLibs = get_openmp()
        
        ## Grab the ATLAS flags
        if self.with_atlas is not None:
            atlasFlags = ['-I%s/include' % self.with_atlas,]
            atlasLibs = ['-L%s/lib' % self.with_atlas, '-lf77blas', '-lcblas', '-latlas']
        else:
            atlasFlags, atlasLibs = get_atlas()
            
        ## Grab the FFTW flags
        if self.with_fftw is not None:
            fftwFlags = ['-I%s/include' % self.with_fftw,]
            fftwLibs = ['-L%s/lib' % self.with_fftw, '-lfftw3f']
        else:
            fftwFlags, fftwLibs = get_fftw()
            
        ## Update the extensions with the additional compilier/linker flags
        for ext in self.extensions:
            ### Compiler flags
            for cflags in (openmpFlags, atlasFlags, fftwFlags):
                try:
                    ext.extra_compile_args.extend( cflags )
                except TypeError:
                    ext.extra_compile_args = cflags
            ### Linker flags
            for ldflags in (openmpLibs, atlasLibs, fftwLibs):
                try:
                    ext.extra_link_args.extend( ldflags )
                except TypeError:
                    ext.extra_link_args = ldflags
                    
        ## HACK: Update the log verbosity - for some reason this gets set to 
        ##       WARN when I replace build_ext
        log.set_threshold(min([log.INFO, log._global_log.threshold]))


coreExtraFlags = ['-DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION']
coreExtraLibs = []


# Create the list of extension modules.  We do this here so that we can turn 
# off the DRSU direct module for non-linux system
ExtensionModules = [Extension('reader._gofast', ['lsl/reader/gofast.c', 'lsl/reader/tbw.c', 'lsl/reader/tbn.c', 'lsl/reader/drx.c', 'lsl/reader/drspec.c', 'lsl/reader/vdif.c', 'lsl/reader/tbf.c', 'lsl/reader/cor.c'], include_dirs=[numpy.get_include()], extra_compile_args=['-DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION', '-funroll-loops']),
            Extension('common._fir', ['lsl/common/fir.c'], include_dirs=[numpy.get_include()], libraries=['m'], extra_compile_args=coreExtraFlags, extra_link_args=coreExtraLibs),
            Extension('correlator._spec', ['lsl/correlator/spec.c'], include_dirs=[numpy.get_include()], libraries=['m'], extra_compile_args=coreExtraFlags, extra_link_args=coreExtraLibs), 
            Extension('correlator._stokes', ['lsl/correlator/stokes.c'], include_dirs=[numpy.get_include()], libraries=['m'], extra_compile_args=coreExtraFlags, extra_link_args=coreExtraLibs),
            Extension('correlator._core', ['lsl/correlator/core.c'], include_dirs=[numpy.get_include()], libraries=['m'], extra_compile_args=coreExtraFlags, extra_link_args=coreExtraLibs), 
            Extension('sim._simfast', ['lsl/sim/simfast.c', 'lsl/sim/const.c', 'lsl/sim/j1.c', 'lsl/sim/polevl.c', 'lsl/sim/mtherr.c', 'lsl/sim/sf_error.c'], include_dirs=[numpy.get_include()], libraries=['m'], extra_compile_args=coreExtraFlags, extra_link_args=coreExtraLibs), 
            Extension('misc._wisdom', ['lsl/misc/wisdom.c'],include_dirs=[numpy.get_include()], libraries=['m'], extra_compile_args=coreExtraFlags, extra_link_args=coreExtraLibs), ]

# Update the version information
write_version_info()

# Setup the INSTALL_REQUIRES list and the EXTRA_REQUIRE dictionary and then
# deal with all of the things that can go wrong with old versions of 
# setuptools
#  From:  https://hynek.me/articles/conditional-python-dependencies/
INSTALL_REQUIRES = ['pyfits>=3.2', 'numpy>=1.2', 'scipy>=0.13', 'pyephem>=3.7.5.3', 'aipy>=1.0,<3.0', 'pytz>=2012c']
EXTRA_REQUIRE = {}
if int(stv.split('.')[0], 10) < 18:
    if sys.version_info[:2] < (2,7):
        INSTALL_REQUIRES.append("argparse")
        INSTALL_REQUIRES.append("unittest2")
else:
    EXTRA_REQUIRE[":python_version<'2.7'"] = ["argparse", "unittest2"]

setup(
    cmdclass = {'build': lsl_build, 'build_ext': lsl_build_ext}, 
    name = "lsl", 
    version = get_version(), 
    description = "LWA Software Library", 
    author = "Jayce Dowell", 
    author_email = "jdowell@unm.edu", 
    url = "https://fornax.phys.unm.edu/lwa/trac/", 
    long_description = get_description('README.md'), 
    license = 'GPL',
    classifiers = ['Development Status :: 5 - Production/Stable',
                  'Intended Audience :: Developers',
                  'Intended Audience :: Science/Research',
                  'License :: OSI Approved :: GNU General Public License (GPL)',
                  'Topic :: Scientific/Engineering :: Astronomy',
                  'Programming Language :: Python :: 2',
                  'Programming Language :: Python :: 2.6',
                  'Programming Language :: Python :: 2.7',
                  'Operating System :: MacOS :: MacOS X',
                  'Operating System :: POSIX :: Linux'],
    packages = find_packages(), 
    scripts = glob.glob('scripts/*.py'), 
    python_requires='>=2.6, <3',
    setup_requires = ['numpy>=1.2'], 
    install_requires = INSTALL_REQUIRES, 
    extras_require = EXTRA_REQUIRE, 
    include_package_data = True,  
    ext_package = 'lsl', 
    ext_modules = ExtensionModules,
    zip_safe = False,  
    test_suite = "tests"
) 
