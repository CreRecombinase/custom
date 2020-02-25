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
#     spack install r-lobstr
#
# You can edit this file again by typing:
#
#     spack edit r-lobstr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------
from spack import *
class RLobstr(RPackage):
    'Visualize R Data Structures with Trees'
    homepage = "https://cloud.r-project.org/src/contrib/lobstr_1.1.1.tar.gz"
    url      = "https://cloud.r-project.org/src/contrib/lobstr_1.1.1.tar.gz"
    version('1.1.1', md5='aae694ae9db027b1760cf593eb3400ad')
    depends_on('r-crayon@1.3.4:', type=('build', 'run'))
    depends_on('r-rcpp@1.0.3:', type=('build', 'run'))
    depends_on('r-rlang@0.4.4:', type=('build', 'run'))
