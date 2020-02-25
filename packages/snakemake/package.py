# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Snakemake(PythonPackage):
    """Snakemake is an MIT-licensed workflow management system."""

    homepage = "https://snakemake.readthedocs.io/en/stable/"
    url      = "https://pypi.io/packages/source/s/snakemake/snakemake-3.11.2.tar.gz"

    version('3.11.2', sha256='f7a3b586bc2195f2dce4a4817b7ec828b6d2a0cff74a04e0f7566dcd923f9761')
    version('5.10.0', sha256='a3fa8b12db84938c919996d61be66031bcb99c4b4d017278731324a6112b0d59')

    depends_on('python@3.3:')
    depends_on('py-requests', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-wrapt', type=('build', 'run'))
    depends_on('py-ratelimiter', type=('build', 'run'))
    depends_on('py-pyyaml', type=('build', 'run'))
    depends_on('py-appdirs', type=('build', 'run'))
    depends_on('py-docutils', type=('build', 'run'))
    depends_on('py-jsonschema', type=('build', 'run'))
    depends_on('py-gitpython', type=('build', 'run'))
    depends_on('py-psutil', type=('build', 'run'))
    depends_on('py-nbformat', type=('build', 'run'))
    depends_on('py-toposort', type=('build', 'run'))
    depends_on('py-configargparse',type=('build', 'run'))
    depends_on('py-datrie', type=('build', 'run'))
    depends_on('py-gitdb', type=('build', 'run'))
    depends_on('py-gitdb2', type=('build', 'run'))
    depends_on('py-smmap', type=('build', 'run'))
    depends_on('git@1.7.0:', type=('build', 'run'))
