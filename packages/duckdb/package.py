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
#     spack install r-duckdb
#
# You can edit this file again by typing:
#
#     spack edit r-duckdb
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Duckdb(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/cwida/duckdb/archive/v0.2.2.tar.gz"
    git      = "https://github.com/cwida/duckdb.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.2.2', sha256='e2d0d9245f3deb1a337a22fa11c8a5c80eab0ebafd0e8645762ecd89ecc56a30')
    version('0.2.1', sha256='e5f7cd12ed783267a0e14027f68b0c1444023ed94f309cff644d538a38612875')
    version('0.2.0', sha256='dd27bcb9120586a0915e38d113bfab41a085323a8d9965068dc339925b75751e')
    version('0.1.9', sha256='e2ee05eac4bbc103638dc1589c003026d558a980528a1467d9e104d66658714e')
    version('0.1.8', sha256='18a984e80e14136f6a61f482387a6e159f5cafd256884e66cc21d6d7a511e33c')
    version('0.1.7', sha256='07b6db4512cf41647043160dc64dfd919948ca7f96c31c1085ce2c79e2059a1c')
    version('0.1.6', sha256='fdb7b38082dcf55aafd51bea81036bc9efed95a99ac9fa5d76f1f876be909cd1')
    version('0.1.5', sha256='3c766b6667e2f359d1e19dfccbd1e43e9b4e5fb9dfe17f66fdb83c079ad088c6')
    version('0.1.4', sha256='c6a778c66d2e9847bf4b7bb153c4180122fa45223563d90b6d712cfa3d962cc2')
    version('0.1.3', sha256='5dd77d8d2c82cbecffb513934c40427c46355819379097b5a1061717e447f0eb')

    # FIXME: Add dependencies if required.
    depends_on('python@3:', type=('build'))

    # def cmake_args(self, spec, prefix):
    #     # FIXME: Add arguments to pass to install via --configure-args
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
