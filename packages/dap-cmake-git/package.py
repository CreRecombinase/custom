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
#     spack install dap-cmake-git
#
# You can edit this file again by typing:
#
#     spack edit dap-cmake-git
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class DapCmakeGit(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    git      = "https://github.com/CreRecombinase/dap_cmake.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('master', branch='master')
    depends_on('boost@1.72.0:',type=('build','run'))
    depends_on('gsl@2.5:',type=('build','run'))
    # FIXME: Add dependencies if required.
    # depends_on('foo')

    # def cmake_args(self):
    #     # FIXME: Add arguments other than
    #     # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
