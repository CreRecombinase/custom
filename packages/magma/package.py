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
#     spack install magma
#
# You can edit this file again by typing:
#
#     spack edit magma
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Magma(MakefilePackage):
    """MAGMA is a tool for gene analysis and generalized gene-set analysis of GWAS data. It can be used to analyse both raw genotype data as well as summary SNP p-values from a previous GWAS or meta-analysis."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://ctg.cncr.nl/software/magma"
    url      = "https://ctg.cncr.nl/software/MAGMA/prog/magma_v1.08_source.zip"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.08', sha256='e0473e986938f1c48a9fe96a003f63d64e6a36e13ae601f5a6d24b86f6147c6f')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    def edit(self,spec,prefix):
        makefile = FileFilter('makefile')
        makefile.filter("CXX = g\+\+","CXX = c++")

    def install(self,spec,prefix):
        mkdirp(prefix.bin)
        install('magma',prefix.bin)

    # def cmake_args(self):
    #     # FIXME: Add arguments other than
    #     # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
