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
#     spack install qctool
#
# You can edit this file again by typing:
#
#     spack edit qctool
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os

class Qctool(WafPackage):
    """A tool for quality control and analysis of gwas datasets."""

    homepage = "https://enkre.net/cgi-bin/code/qctool/"
    #    url = 'https://enkre.net/cgi-bin/code/qctool/tarball/ade6dc6afb/qctool-ade6dc6afb.tar.gz'
    #url      =  "https://crerecombinase.keybase.pub/qctool_2_0_8.tar.gz"
    url = "https://code.enkre.net/qctool/tarball/release/qctool.tgz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('2.0.8',sha256='9e4090dba156539bcf2300affaee02ca2cbed70e4b07b0853ac8aa82331ebd1e')

    # FIXME: Add dependencies if required.
    depends_on('python@:2.9', type=('build'))
    depends_on('zlib')
    depends_on('blas')
    depends_on('fossil')
    depends_on('lapack')

    # FIXME: Override configure_args(), build_args(),

    @run_before('configure')
    def rename_waf(self):
        os.rename('waf-1.5.18', 'waf')
