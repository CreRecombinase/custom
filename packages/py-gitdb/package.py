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
#     spack install py-gitdb
#
# You can edit this file again by typing:
#
#     spack edit py-gitdb
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyGitdb(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://files.pythonhosted.org/packages/8f/04/e47faf01c2657d3b1bdf5f9b5a00b618d11ae7765e8e90d5357c37962e07/gitdb-4.0.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('4.0.1', sha256='d82c6b76ce8496c5209adf1c0ab969a6e1a8a31510ceb5f57a206fc7c77c0fea')

    # FIXME: Add dependencies if required.
    depends_on('python@3.4:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))

    # def build_args(self, spec, prefix):
    #     # FIXME: Add arguments other than --prefix
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
