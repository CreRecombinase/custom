# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install dissect
#
# You can edit this file again by typing:
#
#     spack edit dissect
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Dissect(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "http://www.dissect.ed.ac.uk/download/526/"
    git = "https://github.com/crerecombinase/dissect.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('master',branch='master')
    version('1.15.2', '3c5d784071ff9953b62c98da426d062aa4dfb9f33180a54e26391bd8052e9400',url = 'http://www.dissect.ed.ac.uk/download/526/')


    # FIXME: Add dependencies if required.
    depends_on('scalapack')
    depends_on('boost+iostreams')
    depends_on('mpi')
    depends_on('zstd')
    depends_on('zlib')



    def edit(self, spec, prefix):
        env['DESTDIR'] = prefix+'/'
        env['CXX'] = spec['mpi'].mpicxx
        env['LDFLAGS'] = spec['scalapack'].libs.ld_flags +" "+spec['blas'].libs.ld_flags +" -L"+spec['bgen17'].prefix+"/lib/"
        env['CXXFLAGS'] = spec['mpi']+headers+spec['scalapack'].headers+" -I"+spec['bgen17'].prefix+"/include/"
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter('Makefile')
        # makefile.filter('CXX = mpic++', 'CXX = c++')
        # makefile.filter('MKL_PATH = .*', 'CC = cc')
        # makefile.filter('CXXFLAGS = .*', 'CXXFLAGS = -g -O3 -march=native -mtune=native')
