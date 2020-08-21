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
#     spack install py-snakepipes
#
# You can edit this file again by typing:
#
#     spack edit py-snakepipes
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PySnakepipes(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/maxplanck-ie/snakepipes/archive/2.1.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.1.2', sha256='b8307ea201925738dd4b412e664348b09b7f3d75d532aee79a21a45bd71c6d32')

    # FIXME: Add dependencies if required.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    #depends_on('py-setuptools', type='build')
    depends_on('snakemake@5.13.0:',type=('build','run'))
    depends_on('py-psutil',type=('build','run'))
    depends_on('py-pandas',type=('build','run'))
    depends_on('py-fuzzywuzzy',type=('build','run'))
    depends_on('py-pyyaml@5.1:',type=('build','run'))



    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
