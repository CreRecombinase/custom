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


class RXtensor(RPackage):
    """R package for working with SNP data"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://cloud.r-project.org/src/contrib/xtensor_1.3.1.tar.gz"
    list_url = "https://cloud.r-project.org/src/contrib/Archive/xtensor"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version('0.11.1-0',  md5='3c0783dda50962513f53e028eeaf34c1')
    depends_on('r-rcpp@1.0.3:',type=('build','run'))



    # def configure_args(self, spec, prefix):
    #     # FIXME: Add arguments to pass to install via --configure-args
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
