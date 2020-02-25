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
#     spack install r-lifecycle
#
# You can edit this file again by typing:
#
#     spack edit r-lifecycle
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------
from spack import *
class RLifecycle(RPackage):
    'Manage the Life Cycle of your Package Functions'
    homepage = "https://cloud.r-project.org/src/contrib/lifecycle_0.1.0.tar.gz"
    url      = "https://cloud.r-project.org/src/contrib/lifecycle_0.1.0.tar.gz"
    version('0.1.0', md5='a039f080eb1dc67a40ce92ddced20cac')
    depends_on('r-glue@1.3.1:', type=('build', 'run'))
    depends_on('r-rlang@0.4.4:', type=('build', 'run'))
