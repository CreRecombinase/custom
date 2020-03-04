# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
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
#     spack install r-rhdf5lib
#
# You can edit this file again by typing:
#
#     spack edit r-rhdf5lib
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------
from spack import *
class RRhdf5lib(RPackage):
    'hdf5 library as an R package'
    homepage = "https://bioconductor.org/packages/3.9/bioc/src/contrib/Rhdf5lib_1.6.3.tar.gz"
    url      = "https://bioconductor.org/packages/3.9/bioc/src/contrib/Rhdf5lib_1.6.3.tar.gz"
    version('1.6.3', md5='1257d1377dcd9916065d485de4dd0f9c')

