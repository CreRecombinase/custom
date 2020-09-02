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
#     spack install simu
#
# You can edit this file again by typing:
#
#     spack edit simu
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Simu(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    git      = "https://github.com/CreRecombinase/simu.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version('0.9.4.1',commit='ad62ee59df12327d140c4f55f00a371a894f6b65',submodules=True)
    #version('0.9.4', commit='a4484f92ce97873a0405cc2ad476f9a41733e7f5',submodules=True)
    # version('0.9.3', sha256='70900ac2de747367127406f042f73929f8ae77b10ef9515e513ff9a4d57b9814',submodues=True)
    # version('0.9.2', sha256='cc489770f2917e032ba7c9e655114b8543482143596b1052addc8645b33e467b',submodules=True)
    # version('0.9',   sha256='756963db708ca07f557e9c4bbc06101f6118abd0e69fc30fb12cb0df1b7c3621',submodules=True)

    # FIXME: Add dependencies if required.
    depends_on('boost')

    # def cmake_args(self):
    #     # FIXME: Add arguments other than
    #     # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
