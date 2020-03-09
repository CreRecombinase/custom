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
#     spack install r-testthat
#
# You can edit this file again by typing:
#
#     spack edit r-testthat
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------
from spack import *
class RTestthat(RPackage):
    'Unit Testing for R'
    homepage = "https://cloud.r-project.org/src/contrib/testthat_2.3.2.tar.gz"
    url      = "https://cloud.r-project.org/src/contrib/testthat_2.3.2.tar.gz"
    version('2.3.2', md5='0e9ed62b4d94f9b7fa1ad353a5372690')
    depends_on('r-assertthat@0.2.1:', type=('build', 'run'))
    depends_on('r-backports@1.1.5:', type=('build', 'run'))
    depends_on('r-callr@3.4.2:', type=('build', 'run'))
    depends_on('r-cli@2.0.2:', type=('build', 'run'))
    depends_on('r-crayon@1.3.4:', type=('build', 'run'))
    depends_on('r-desc@1.2.0:', type=('build', 'run'))
    depends_on('r-digest@0.6.25:', type=('build', 'run'))
    depends_on('r-ellipsis@0.3.0:', type=('build', 'run'))
    depends_on('r-evaluate@0.14:', type=('build', 'run'))
    depends_on('r-fansi@0.4.1:', type=('build', 'run'))
    depends_on('r-glue@1.3.1:', type=('build', 'run'))
    depends_on('r-magrittr@1.5:', type=('build', 'run'))
    depends_on('r-pkgbuild@1.0.6:', type=('build', 'run'))
    depends_on('r-pkgload@1.0.2:', type=('build', 'run'))
    depends_on('r-praise@1.0.0:', type=('build', 'run'))
    depends_on('r-prettyunits@1.1.1:', type=('build', 'run'))
    depends_on('r-processx@3.4.2:', type=('build', 'run'))
    depends_on('r-ps@1.3.2:', type=('build', 'run'))
    depends_on('r-r6@2.4.1:', type=('build', 'run'))
    depends_on('r-rlang@0.4.5:', type=('build', 'run'))
    depends_on('r-rprojroot@1.3-2:', type=('build', 'run'))
    depends_on('r-rstudioapi@0.11:', type=('build', 'run'))
    depends_on('r-withr@2.1.2:', type=('build', 'run'))
