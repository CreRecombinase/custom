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
#     spack install r-susier-git
#
# You can edit this file again by typing:
#
#     spack edit r-susier-git
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RSusierGit(RPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    git      = "https://github.com/stephenslab/susieR.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('master',  branch='master')
    # FIXME: Add dependencies if required.
    depends_on('r-matrix', type=('build', 'run'))
    depends_on('r-matrixstats', type=('build', 'run'))
    depends_on('r-expm', type=('build', 'run'))
    depends_on('r-wavethresh', type=('build', 'run'))
