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
#     spack install bgen
#
# You can edit this file again by typing:
#
#     spack edit bgen
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Bgen(WafPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url =  "http://code.enkre.net/bgen/tarball/release/bgen.tgz"
    hg      =  "https://enkre.net/cgi-bin/code/bgen"
    version('default',sha256 = '22a5e9254b71a08f233779350472f03c6f32a60cb6e07750305a9115454d7470')

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    # FIXME: Override configure_args(), build_args(),
    # or install_args() if necessary.
    # def install(self, spec, prefix):
    #     """Installs the targets on the system."""
    #     args = self.install_args()
    #     self.waf('install', *args)
    #     mkdirp(prefix.lib)
    #     mkdirp(prefix.include)

    #     with working_dir('build'):
    #         install('genfile',prefix.include)
    #         install('bgen_revision_autogenerated.hpp',prefix.include)
    #         install('libbgen.a',prefix.lib)
