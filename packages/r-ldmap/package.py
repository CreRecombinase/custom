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
#     spack install r-ldmap
#
# You can edit this file again by typing:
#
#     spack edit r-ldmap
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RLdmap(RPackage):
    """R package for working with SNP data"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/CreRecombinase/ldmap/archive/1.5.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.5.2', sha256='73fa38de7d7431bdf607054195c21b3e548b4ed8bbeec10f8089c5efecbd4e64')

    depends_on('r-rlang@0.4.4:', type=('build', 'run'))
    depends_on('r-vctrs@0.2.2:', type=('build', 'run'))
    depends_on('r-magrittr@1.5:', type=('build', 'run'))
    depends_on('r-bh@1.69.0:', type=('build', 'run'))
    depends_on('r-forcats@0.4.0:', type=('build', 'run'))
    depends_on('r-bit64@0.9-7:', type=('build', 'run'))
    depends_on('r-rcppparallel@4.4.3:', type=('build', 'run'))
    depends_on('r-rcppprogress@0.4.1:', type=('build', 'run'))
    depends_on('r-rcpp@1.0.2:', type=('build', 'run'))


    # def configure_args(self, spec, prefix):
    #     # FIXME: Add arguments to pass to install via --configure-args
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
