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
#     spack install py-pulp
#
# You can edit this file again by typing:
#
#     spack edit py-pulp
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyPulp(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/coin-or/pulp/archive/2.3.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.3',    sha256='fcb2246faf8377b806073ce12aa182f91702a2c8c8a53594a2baed59d0ebc77c')
    version('2.2',    sha256='f5d2d10244fc4f1bb6d4fa0ff10db2605e557ef203bfa01c24f60758bef0c5ed')
    version('1.6.10', sha256='44d18aebcacb6dae73c83822319576a2a9c15bc8fb519f01c405ccc110a88e40')
    version('1.6.7',  sha256='b241148ad476d473c0a1553269d3903423ab860f291f6091a2ffc3358604b6c9')
    version('1.6.4',  sha256='466410c5e49402c434ca91c5063abf0ae4ff93099720873391f4100eb81edac1')
    version('1.6.3',  sha256='7657b395b9f4345559d5be1f22892a13cb41d58f86724ddc1fd6223781c039e7')
    version('1.6.2',  sha256='7a1217012db4696f4761c6155ae75c380932b0447ba14b6b8713ca11c0161143')
    version('1.6.1',  sha256='a8528438677ed05100d940e1cebbf5da862f197518e1880fe493b38d2126a37c')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    # depends_on('py-setuptools', type='build')
    depends_on('py-amply@0.1.2:',        type=('build', 'run'))

    # def build_args(self, spec, prefix):
    #     # FIXME: Add arguments other than --prefix
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
