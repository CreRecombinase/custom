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
#     spack install r-tidyr
#
# You can edit this file again by typing:
#
#     spack edit r-tidyr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------
from spack import *
class RTidyr(RPackage):
    'Tidy Messy Data'
    homepage = "https://cloud.r-project.org/src/contrib/tidyr_1.0.2.tar.gz"
    url      = "https://cloud.r-project.org/src/contrib/tidyr_1.0.2.tar.gz"
    version('1.0.2', md5='9118722418f48877650f6dcf9e160606')
    depends_on('r-assertthat@0.2.1:', type=('build', 'run'))
    depends_on('r-cli@2.0.2:', type=('build', 'run'))
    depends_on('r-crayon@1.3.4:', type=('build', 'run'))
    depends_on('r-digest@0.6.25:', type=('build', 'run'))
    depends_on('r-dplyr@0.8.5:', type=('build', 'run'))
    depends_on('r-ellipsis@0.3.0:', type=('build', 'run'))
    depends_on('r-fansi@0.4.1:', type=('build', 'run'))
    depends_on('r-glue@1.3.1:', type=('build', 'run'))
    depends_on('r-lifecycle@0.2.0:', type=('build', 'run'))
    depends_on('r-lobstr@1.1.1:', type=('build', 'run'))
    depends_on('r-magrittr@1.5:', type=('build', 'run'))
    depends_on('r-pillar@1.4.3:', type=('build', 'run'))
    depends_on('r-pkgconfig@2.0.3:', type=('build', 'run'))
    depends_on('r-purrr@0.3.3:', type=('build', 'run'))
    depends_on('r-r6@2.4.1:', type=('build', 'run'))
    depends_on('r-rcpp@1.0.3:', type=('build', 'run'))
    depends_on('r-rlang@0.4.5:', type=('build', 'run'))
    depends_on('r-stringi@1.4.6:', type=('build', 'run'))
    depends_on('r-tibble@2.1.3:', type=('build', 'run'))
    depends_on('r-tidyselect@1.0.0:', type=('build', 'run'))
    depends_on('r-utf8@1.1.4:', type=('build', 'run'))
    depends_on('r-vctrs@0.2.3:', type=('build', 'run'))
    depends_on('r-zeallot@0.1.0:', type=('build', 'run'))
