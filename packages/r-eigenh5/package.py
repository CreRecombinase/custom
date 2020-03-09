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
#     spack install r-eigenh5
#
# You can edit this file again by typing:
#
#     spack edit r-eigenh5
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class REigenh5(RPackage):
    """R package for working with SNP data"""
    homepage = "https://www.example.com"
    git      = "https://github.com/CreRecombinase/eigenh5.git"
    url = "https://github.com/CreRecombinase/EigenH5/archive/2.0.2.tar.gz"
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version('2.0.7',sha256='879ea24c104b3b1ca49f5ad5ba4251320ac5119c8c6ad32c885a86a958342e79')
    version('2.0.3',sha256='30203bad5f3f7562c92e672e368a65ed8633f6ff39c45f441d789a7d476aa6aa')
    version('master',  branch='master')
    version('2.0.2',sha256='56af487038fc7e9f29a47963fb8ae3067a66190d0e1d720a303e16ef77e0acdf')
    depends_on('r-rcpp@1.0.3:',type=('build','run'))
    depends_on('r-rcppeigen@0.3.3.7.0:',type=('build','run'))
    depends_on('r-bh@1.72.0-3:',type=('build','run'))
    depends_on('r-dplyr@0.8.4:',type=('build','run'))
    depends_on('r-progress@1.2.2:',type=('build','run'))
    depends_on('r-tidyr@1.0.2:',type=('build','run'))
    depends_on('r-stringr@1.4.0:',type=('build','run'))
    depends_on('r-purrr@0.3.3:',type=('build','run'))
    depends_on('r-magrittr@1.5:',type=('build','run'))
    depends_on('r-fs@1.3.1:',type=('build','run'))
    depends_on('r-readr@1.3.1:',type=('build','run'))
    depends_on('r-rlang@0.4.4:',type=('build','run'))
    depends_on('r-rcpp@1.0.3:',type=('build','run'))
    depends_on('r-rcppeigen@0.3.3.7.0:',type=('build','run'))
    depends_on('r-rcppprogress@0.4.1:',type=('build','run'))
    depends_on('r-bh@1.72.0-3:',type=('build','run'))
    depends_on('r-xtensor@0.11.1-0:',type=('build','run'))
    depends_on('hdf5@1.10.6:+hl~mpi', type=('build', 'run'))
    depends_on('zstd@1.4.3:', type=('build', 'run'))


    # def configure_args(self, spec, prefix):
    #     # FIXME: Add arguments to pass to install via --configure-args
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
