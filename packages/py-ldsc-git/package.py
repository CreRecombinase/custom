
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
#     spack install py-ldsc-git
#
# You can edit this file again by typing:
#
#     spack edit py-ldsc-git
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyLdscGit(PythonPackage):
    """FIXME: Put a proper description of your package here."""
    homepage = "https://github.com/xinhe-lab/ldsc"
    url      = "git@github.com:xinhe-lab/ldsc.git"
    git      = "https://github.com/xinhe-lab/ldsc.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['CreRecombinase', 'github_user2']
    version('1.0.4', commit='bb8eeb9fe76ab208f5d3de9b57eb03e3fc48572b')
    version('1.0.3', commit='5fe055aed5e862f6c27f23ea5f646a8665646ff1')


    # FIXME: Add dependencies if required.
    depends_on('python@:2.9', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-pybedtools@0.6.9', type=('build', 'run'))
    depends_on('py-numpy@1.12.1', type=('build', 'run'))
    depends_on('py-bitarray@0.8.1', type=('build', 'run'))
    depends_on('py-scipy@0.18.1', type=('build', 'run'))
    depends_on('py-pandas@0.20.0', type=('build', 'run'))

    # depends_on('py-foo',        type=('build', 'run'))

    # def build_args(self, spec, prefix):
    #     # FIXME: Add arguments other than --prefix
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
