# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gcta(Package):

    """GCTA (Genome-wide Complex Trait Analysis) was originally designed to
    estimate the proportion of phenotypic variance explained by all genome-wide
    SNPs for complex traits (the GREML method), and has subsequently extended
    for many other analyses to better understand the genetic architecture of
    complex traits. GCTA currently supports the following analyses."""

    homepage = "http://cnsgenomics.com/software/gcta/#Overview"
    url = "https://cnsgenomics.com/software/gcta/bin/gcta_1.93.2beta.zip"

    version('1.91.2beta_mac', 'ce0882ad35dd9474ffe40911da369274700af1ecb9916c0a355b7bad14850234')
    version('1.91.2beta', '192efb767be1c7ca9c2dac5d2c2317a97c7a9db1f801168d19ad2a51b98d9b10')
    version('1.93.2beta', '44354f4909666b760ab3cf538dc143ee3feff5540c2ad237a098766ff9829374', preferred=True)

    conflicts('@1.91.2beta', when='platform=darwin')
    conflicts('@1.91.2beta_mac', when='platform=linux')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('gcta64', join_path(prefix.bin, 'gcta64'))
        set_executable(join_path(prefix.bin, 'gcta64'))
