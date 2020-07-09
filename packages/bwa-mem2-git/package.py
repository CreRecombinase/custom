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
#     spack install bwa-mem2-git
#
# You can edit this file again by typing:
#
#     spack edit bwa-mem2-git
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class BwaMem2Git(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url=     "https://github.com/bwa-mem2/bwa-mem2/releases/download/v2.0/Source_code_including_submodule.tar.gz"
    git      = "https://github.com/bwa-mem2/bwa-mem2.git"
    version('master',branch='master')
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.0', sha256='23a8aa9d295ed1e042aec255157313b0ddf45ae2271a9b878b5e05a4c1026d38')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    build_targets = ['multi']
    def edit(self, spec, prefix):
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        makefile = FileFilter('Makefile')
        makefile.filter('CC = cc', 'CXX = cxx')

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('bwa-mem2', prefix.bin)
        install('bwa-mem2.avx2', prefix.bin)
        install('bwa-mem2.avx512bw', prefix.bin)
        install('libbwa.a', prefix.lib)
