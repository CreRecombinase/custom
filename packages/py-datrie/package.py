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
#     spack install py-datrie
#
# You can edit this file again by typing:
#
#     spack edit py-datrie
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyDatrie(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://files.pythonhosted.org/packages/f5/a2/49d6db3af61eb139fb8fa2cdff90a4789e8255d227baf8f9a1ec945b4aac/datrie-0.8.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.8', sha256='bdd5da6ba6a97e7cd96eef2e7441c8d2ef890d04ba42694a41c7dffa3aca680c')

    # FIXME: Add dependencies if required.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))

    # def build_args(self, spec, prefix):
    #     # FIXME: Add arguments other than --prefix
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
