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
#     spack install tiledb
#
# You can edit this file again by typing:
#
#     spack edit tiledb
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Tiledb(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/TileDB-Inc/TileDB/archive/1.7.5.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.7.5', sha256='84d7d33454809ef76b1b41592fb602d64d568a6fbb78da1d381116d98a568cdc')
    version('1.7.4', sha256='a87638d804c0cdd24c131e46d9b78094298420fc878292ace27c7b775fb42382')
    version('1.7.3', sha256='f1c4bb58686485af997ba25857e8831668f47e64f9e88b73fa509a4e0b319858')
    version('1.7.2', sha256='85db6825fd8d78fa88f646c83c966caecda89a9c66cac4f3916f548665e0afd1')
    version('1.7.1', sha256='8cc6a178746f024791f9c2624b9b5627c4f2fad72ca0b8023877557a71d151b6')
    version('1.7.0', sha256='bf8a689dd485c0f13b4173fe1f1a573230af2dc3c329329846becab22af48e10')
    version('1.6.3', sha256='12b70176822a04423093db741376d2bf0c3867b535e7dc4ee8dfa9a8444611fc')
    version('1.6.2', sha256='001e49f4a9408f0e9064628ddcde201a5f76cf7a87c5bb17799c45e648001393')
    version('1.6.1', sha256='80127f900cb74b5a629a86c703ababacb7b78a37e5fd89399193f5724afcde01')
    version('1.6.0', sha256='96a0f3cd7a9b5c84c725929ab160431199beb1bcf96f76905ab2b52464bacded')

    # FIXME: Add dependencies if required.
    depends_on('zlib')
    depends_on('zstd')
    depends_on('lz4')
    depends_on('bzip2')
    install_targets = ['install-tiledb']
