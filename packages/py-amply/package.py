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
#     spack install py-amply
#
# You can edit this file again by typing:
#
#     spack edit py-amply
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyAmply(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/willu47/amply"
    url      = "https://files.pythonhosted.org/packages/7f/11/33cb09557ac838d9488779b79e05a2a3c1f3ce9747cd242ba68332736778/amply-0.1.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.1.2',         sha256='6e5d53af62772790ba82a989a3de72b8ce5c1cd809613c06f7cb061f7ec34dc8')
    version('0.1.1',         sha256='01398021ad8fa8f5b08a91d692f4db1c8b8f4aa8010ebd64572ea5269ceb588d')
    version('0.1.0-alpha.7', sha256='b5efd301a3033dc4e9c834ce19ee83a8bec8140141c8242990400401aa857c2e')
    version('0.1.0-alpha.6', sha256='c3eebd1d61148d9af3447a15222fb83c9579ae34cbeb94e697a744d8578025c7')
    version('0.1.0-alpha.5', sha256='6c214f97d10d3d18229e38c93d262ff9140eb2949a2820b9c79b0774c5f23334')
    version('0.1.0-alpha.4', sha256='a8d7c6cfd54177f8e495c777a3e7d805c964bd837b88e1d03461813167ac53c9')
    version('0.1.0-alpha.3', sha256='521f35faf5144349cc3e14bef65f96ec7a3b1dab623c209d81883b7fb04bd42c')
    version('0.1.0-alpha.2', sha256='3a437f6ccf32eda23901ccd4cf873788396e9c135fe61c31e320533cfc93c177')
    version('0.1.0-alpha',   sha256='68fbd4b4c4857af29f05f15c1963b54f76103f5b3434bdf448ea59a092b514e0')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-setuptools-scm', type='build')
    depends_on('py-pyparsing',        type=('build', 'run'))

    # def build_args(self, spec, prefix):
    #     # FIXME: Add arguments other than --prefix
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
