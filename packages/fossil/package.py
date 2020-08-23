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
#     spack install fossil
#
# You can edit this file again by typing:
#
#     spack edit fossil
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Fossil(AutotoolsPackage):
    """Fossil is a simple, high-reliability, distributed software configuration management."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://fossil-scm.org/home/doc/trunk/www/index.wiki"
    url      = "https://fossil-scm.org/home/uv/fossil-src-2.12.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.12.1', sha256='822326ffcfed3748edaf4cfd5ab45b23225dea840304f765d1d55d2e6c7d6603')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    # def configure_args(self):
    #     # FIXME: Add arguments other than --prefix
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
